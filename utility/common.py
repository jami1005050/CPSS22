import numpy
import pandas as pd
from random import randint, sample

from sklearn.model_selection import GroupShuffleSplit

from utility.constant import *
from scipy import stats
import matplotlib.pyplot as plt

def read_data(filePath, year):
    file = pd.read_csv(filePath)  # read file from the abs dir
    file['localminute'] = pd.to_datetime(file['localminute'].str.slice(0, 19))
    # print('use: ',file['use'])
    file['use'] = file['use'] * 1000
    mask_less_50 = (file['use'] <= 50)
    df = file.loc[mask_less_50]
    file.loc[mask_less_50, 'use'] = df['use'].apply(lambda x: randint(20, 50))
    file_data = file.loc[
        file['localminute'].dt.year == int(year)].copy()  # removing extra entries outside the year data
    return file_data

def box_cox_transformation(data):
    for key in data.keys():
        data[key].use = stats.boxcox(data[key].use, lmbda=LAMBDA, alpha=None)
    return data

def calculate_gradients(costFunction, non_zero_ruc_array):#param1- output param2-input of a loss function
    f = numpy.array(costFunction, dtype = float)
    x = numpy.array(non_zero_ruc_array,dtype=float)
    dx = numpy.gradient(x)
    gradients = numpy.gradient(f,x)
    for i in range(len(gradients)):
        if(numpy.isnan(gradients[i])):
            gradients[i] = gradients[0]
    index_of_sorted_list = sorted(range(len(gradients)), key=lambda k: gradients[k], reverse=True)
    print(index_of_sorted_list)
    return index_of_sorted_list,gradients

def calculateAMAndHM(data):
    frame_array = []
    for key in data.keys():
        dateRatioArray = []
        day = 1
        yearlyData = data[key]  # yearly data
        monthwisegroupData = yearlyData.groupby(pd.Grouper(key='localminute', freq='1M'))  # monthwise grouping the data
        for key, monthlydata in monthwisegroupData:  # iterate each month data
            if len(monthlydata) > 0:  # check if there is data for the month
                daywisegroupData = monthlydata.groupby(
                    pd.Grouper(key='localminute', freq='1D'))  # group the montly data by day
                for key, dailyData in daywisegroupData:  # iterate each day of the month
                    if len(daywisegroupData) > 0:  # check if the day wise data count is greater than zero
                        hourwiseGroupData = dailyData.groupby(
                            pd.Grouper(key='localminute', freq='1H'))  # group the daily data into hourlwise
                        hourwiseSumAM = 0
                        hourwiseSumHM = 0
                        for key, hourlyData in hourwiseGroupData:  # iterate each hourly data of the day
                            if len(hourlyData) > 0:  # check if the hour has data count greater than zero
                                am_sum = 0
                                hm_sum = 0
                                for row in hourlyData.itertuples():
                                    if (getattr(row, "use") > 0):
                                        am_sum += getattr(row, "use")  # calculate arithmatic sum
                                        hm_sum += 1 / getattr(row, "use")  # calculate harmonic sum
                                N = len(hourlyData.dataid.unique())
                                hourlyAttackHM = N / hm_sum  # harmonic mean hourly
                                hourlyAttackAM = am_sum / N  # arithmatic mean hourly
                                hourwiseSumAM += hourlyAttackAM
                                hourwiseSumHM += hourlyAttackHM
                        year = int(key.year)
                        month = key.month
                        daywiseRatioMean = hourwiseSumHM / hourwiseSumAM  # use the ratio means of 24 hours of a day to calculate day wise ratio means
                        temp = {'year': year, 'month': month, 'day': day, 'ratio' + str(key.year): daywiseRatioMean}
                        day = day + 1
                        # print(temp)
                        dateRatioArray.append(temp)
        dateRatioFrame = pd.DataFrame(dateRatioArray)
        frame_array.append(dateRatioFrame)
        plot = dateRatioFrame.plot(kind="line", x="day", y="ratio"+str(key.year), color="blue",
                                   xlim=(START, END),
                                   ylim =(.85, 1.00),
                                   title =str(key.year)+ ' ratio plot vs day')#08/17
    plt.show()
    return frame_array

def calculate_safe_margin(data_frame, mad, threshold):
    data_frame['margin_high'] = data_frame['mean_ratio'] + threshold * mad
    data_frame['margin_low'] = data_frame['mean_ratio'] - threshold * mad
    return data_frame

def perform_additive_attack(file_data, romal, delavg, START_DATE, END_DATE):
    file_data_copied = {}
    for key in file_data.keys():
        file_data_copied[key] = file_data[key].copy()
    attack_window_data = file_data_copied[str(ATTACK_YEAR)]
    allMeters = attack_window_data.dataid.unique()
    # print("Number of meteres", len(allMeters))
    numberofitems = (len(allMeters) * romal)
    # print("number of items to sample", numberofitems)
    compromisedMeters = sample(allMeters.tolist(), int(numberofitems))
    # print("Number of compromised meteres", len(compromisedMeters))
    mask = (attack_window_data['localminute'] >= START_DATE) & \
           (attack_window_data['localminute'] <= END_DATE) & \
           (attack_window_data['dataid'].isin(compromisedMeters))
    df = attack_window_data.loc[mask]
    # print(file_data_copied[str(ATTACK_YEAR)].loc[mask])
    # print(file_data_copied[str(ATTACK_YEAR)])

    # df2 = attack_window_data.loc[mask] # this is for checking if the del avg is working
    # iterate each row of the dataframe and add a random number with use value
    # for row in attack_window_data.loc[mask].itertuples():
    #     print(row)
    # setattr(row,'use',getattr(row,'use')+ randint(200, 600))
    # df['use'] = df['use'].apply(lambda x: x + randint(200, 600))
    # attack_window_data.loc[mask, 'use'] = df['use'].apply(lambda x: x + randint(1400, 1600)) #commented out on purpose to check the effect of various results
    # print("Before attack with del avg: ",delavg)
    # print(attack_window_data.loc[mask, 'use'] )
    s = delavg - 50
    e = delavg + 50
    attack_window_data.loc[mask, 'use'] = df['use'].apply(lambda x: x + randint(s, e))
    # print(file_data_copied[str(ATTACK_YEAR)].loc[mask])
    # print("attack winodw data for del avg:",delavg)
    # print(attack_window_data.loc[mask, 'use'] )
    # df3 =  attack_window_data.loc[mask] # this is for checking if the del avg is working
    # df_combined = df2 # this is for checking if the del avg is working
    # df_combined['use'] = df3['use']-df2['use'] # this is for checking if the del avg is working
    # print(df_combined.groupby(['dataid']).mean()) # this is for checking if the del avg is working
    # print("df_combined: ",df_combined)
    # print(file_data_copied[str(ATTACK_YEAR)])
    return file_data_copied, numberofitems
    # commented#12.47 08/17/2020
    # attack_window_data.loc[mask, 'use'] = randint(0, 50)
    # return file_data_copied#12.47 08/17/2020

def perform_deductive_attack(file_data, romal, delavg, START_DATE, END_DATE):
    file_data_copied = {}
    for key in file_data.keys():
        file_data_copied[key] = file_data[key].copy()
    attack_window_data = file_data_copied[str(ATTACK_YEAR)]
    allMeters = attack_window_data.dataid.unique()
    print("Number of meteres", len(allMeters))
    numberofitems = (len(allMeters) * romal)
    print("number of items to sample", numberofitems)
    compromisedMeters = sample(allMeters.tolist(), int(numberofitems))
    print("Number of compromised meteres", len(compromisedMeters))
    mask = (attack_window_data['localminute'] >= START_DATE) & \
           (attack_window_data['localminute'] <= END_DATE) & \
           (attack_window_data['dataid'].isin(compromisedMeters))
    df = attack_window_data.loc[mask]
    s = delavg - 50
    e = delavg + 50
    attack_window_data.loc[mask, 'use'] = df['use'].apply(lambda x: x - randint(s, e))
    return file_data_copied, numberofitems

def perform_camouflage_attack(file_data, romal, delavg, START_DATE, END_DATE):
    file_data_copied = {}
    for key in file_data.keys():
        file_data_copied[key] = file_data[key].copy()
    attack_window_data = file_data_copied[str(ATTACK_YEAR)]
    allMeters = attack_window_data.dataid.unique()
    print("Number of meteres", len(allMeters))
    numberofitems = (len(allMeters) * romal)
    # print("number of items to sample", numberofitems)
    compromisedMeters = sample(allMeters.tolist(), int(numberofitems))
    mask = (attack_window_data['localminute'] >= START_DATE) & \
           (attack_window_data['localminute'] < END_DATE) & \
           (attack_window_data['dataid'].isin(compromisedMeters))
    df = attack_window_data.loc[mask]
    gss = GroupShuffleSplit(n_splits=1, test_size=0.5)
    idx1, idx2 = next(gss.split(df, groups=df.dataid))
    df1, df2 = df.iloc[idx1], df.iloc[idx2]
    s = delavg - 50
    e = delavg + 50
    df1['use'] = df1['use'].apply(lambda x: x - randint(s, e))
    df2['use'] = df2['use'].apply(lambda x: x + randint(s, e))
    df.iloc[idx1] = df1
    df.iloc[idx2] = df2
    attack_window_data.loc[mask, 'use'] = df['use']
    return file_data_copied, numberofitems

def calculate_nabla(ratio_frame, keys):
    nabla = []
    for row in ratio_frame.itertuples():
        temp = {}
        for key in keys:
            if (getattr(row, 'ratio' + key) > getattr(row, 'margin_high')):
                temp.update({'nabla' + key: (getattr(row, 'ratio' + key) - getattr(row, 'margin_high'))})
            elif (getattr(row, 'ratio' + key) < getattr(row, 'margin_low')):
                temp.update({'nabla' + key: (getattr(row, 'ratio' + key) - getattr(row, 'margin_low'))})
            else:
                temp.update({'nabla' + key: 0})
        temp.update({'day': row.day})
        nabla.append(temp)
    nabla_frame = pd.DataFrame(nabla)
    return nabla_frame

def calculate_ruc(nabla_frame, keys):
    ruc_arry = []
    for row in nabla_frame.itertuples():
        temp = {}
        if (row.day <= SLIDING_FRAME):
            for key in keys:
                temp.update({'ruc' + key: getattr(row, 'nabla' + key)})
            temp.update({'day': row.day})
            ruc_arry.append(temp)
        else:
            for key in keys:
                sliding_frame_rows = nabla_frame.loc[(nabla_frame['day'] <= row.day)
                                                     & (nabla_frame['day'] > (row.day - SLIDING_FRAME))]
                ruc = 0
                count = 0
                for row1 in sliding_frame_rows.itertuples():
                    ruc = ruc + getattr(row1, 'nabla' + key)
                    count = count +1
                temp.update({'ruc' + key: ruc})
            temp.update({'day': row.day})
            ruc_arry.append(temp)
    ruc_frame = pd.DataFrame(ruc_arry)
    return ruc_frame

def testing_attacked_threshold(residual_frame,max_threshold_org,min_threshold_org,
                               max_threshold_att,min_threshold_att):
    first_detected_org = 0
    first_detected_att = 0
    false_alarm_tier2_org = 0
    false_alarm_tier2_att = 0
    tier1_anomaly = 0
    tier2_for_att = 0
    tier2_for_org = 0
    for row in residual_frame.itertuples():
        if not(getattr(row,"ratio2016") <= getattr(row,'margin_high') and
               getattr(row,'ratio2016') >= getattr(row,'margin_low')):
            tier1_anomaly = tier1_anomaly + 1
            if float(getattr(row,"ruc2016"))!= float(0):
                if(float(getattr(row,"ruc2016"))> float(max_threshold_org) or float(getattr(row,"ruc2016")) < float(min_threshold_org)):
                    print("day",getattr(row, "day"),' ',getattr(row,"ruc2016"),' ', max_threshold_org,' ', min_threshold_org)
                    if(getattr(row,"day") > int(91) and getattr(row,"day")<int(181) ): # 91 = attack start day 181 = attack end day
                        if int(tier2_for_org) == int(0):
                            first_detected_org = getattr(row, "day")
                        tier2_for_org = tier2_for_org +1
                    else:
                        false_alarm_tier2_org = false_alarm_tier2_org + 1
                if (float(getattr(row,"ruc2016")) > float(max_threshold_att) or float(getattr(row,"ruc2016")) < float(min_threshold_att)):
                    print("day",getattr(row, "day"),' ',getattr(row,"ruc2016"),' ',max_threshold_att,' ',min_threshold_att)
                    if (getattr(row,"day") > int(91) and getattr(row,"day")<int(181)):
                        if int(tier2_for_att) == int(0) :
                            first_detected_att = getattr(row, "day")
                        tier2_for_att = tier2_for_att +1
                    else:
                        false_alarm_tier2_att = false_alarm_tier2_att + 1
    print("Tier 1 Detection: ",tier1_anomaly,"\n",
          "Tier 2 Detection for altered threshold: ",tier2_for_att,"\n",
          "Tier 2 Detection for Org Threshold: ",tier2_for_org,
          "First Detected org: ",first_detected_org,
          "First Detected atta: ",first_detected_att,
        "false_alarm_tier2_org: ", false_alarm_tier2_org,
        "false_alarm_tier2_att: ", false_alarm_tier2_att
        )
    return tier2_for_org,tier2_for_att, first_detected_org,first_detected_att,false_alarm_tier2_org,false_alarm_tier2_att

