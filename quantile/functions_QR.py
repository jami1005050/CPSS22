from random import random

import numpy
import sys
import matplotlib.pyplot as plt
import csv
from utility.common import *
import pandas as pd
import random
#-0.1275 or -0.1025 0.0975 #hyper parameter 6
#-0.13 or -0.1075  0.0975 #hyper parameter 8
#-0.12 or -0.09  0.09 #hyper parameter 4
#l1(-0.09 or -065 0.065) l2(-0.08 0.08) #hyper parameter 2
upper_limit = 0.0675
lower_limit = -0.0651580041643599
random.seed(42)
def calculateTmax_ruc_QR(rucFrame):
    global maxThreshold1
    max_candidate = max(rucFrame)
    maxSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0000, max_candidate, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            # print(row)
            if (row > 0):
                if (row <  taoThreshold):
                    # temp = abs(taoThreshold- row)/2
                    # costSum += pow(temp, 2)
                    costSum += abs(taoThreshold - row) / 2
                    costCount = costCount + 1
                else:
                    # temp = abs(taoThreshold - row)*2
                    # pSum += pow(temp, 2)
                    pSum += abs(taoThreshold - row) * 2
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            if (maxSum > taoSumDiff):
                # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold*(-1))
                maxSum = taoSumDiff
                maxThreshold1 = taoThreshold
        # print("Cost Count: ",costCount," penalty count: ",penaltyCount)
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    # w = csv.writer(open("../data/loss_vs_tmax_l1_fgav_UNCON_2.csv", "w"))
    # for key, val in difference.items():
    #     w.writerow([key, val])
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    #
    # fig = plt.figure()
    # plt.plot(x, y)
    # fig.suptitle('Cost - Penalty Plotting', fontsize=20)
    # plt.xlabel('Standard Limit')
    # plt.ylabel('Loss')
    # # fig.savefig('test.jpg')
    # plt.show()
    # print(minThreshold)
    return maxThreshold1, maxSum

def calculateTmin_ruc_QR(rucFrame):
    global minThreshold
    minSum = sys.float_info.max
    min_candidate = min(rucFrame)
    difference = dict()
    for taoThreshold in numpy.arange(min_candidate, 0.00, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            if (row < 0):
                # print(row)
                if (row > ( taoThreshold)):
                    # temp = abs(taoThreshold*(-1) - row)/2
                    # costSum += pow(temp, 2)
                    costSum += abs(taoThreshold - row) / 2
                    costCount = costCount + 1
                else:
                    # temp = abs(taoThreshold*(-1) - row)*2
                    # pSum += pow(temp, 2)
                    pSum += abs(taoThreshold - row) * 2
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            if (minSum > taoSumDiff):
                # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold*(-1))
                minSum = taoSumDiff
                minThreshold = taoThreshold
        # print("Cost Count: ",costCount," penalty count: ",penaltyCount)
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    # w = csv.writer(open("../data/loss_vs_tmin_l1_fgav_UNCON_2.csv", "w"))
    # for key, val in difference.items():
    #     w.writerow([key, val])
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    #
    # fig = plt.figure()
    # plt.plot(x, y)
    # fig.suptitle('Cost - Penalty Plotting', fontsize=20)
    # plt.xlabel('Standard Limit')
    # plt.ylabel('Loss')
    # # fig.savefig('test.jpg')
    # plt.show()
    # print(minThreshold)
    return minThreshold,minSum

def calculateTmax_QR(rucFrame, keys):
    # maxSum = (-1)*sys.float_info.max  #commented puposefully as the algorithm says if
    # the difference between cost and penalty is min
    maxSum = sys.float_info.max
    # print("maxSum: ",maxSum)
    maxRuc2014 = rucFrame['ruc2014'].max()
    maxRuc2015 = rucFrame['ruc2015'].max()
    maxThreshold = max(maxRuc2015, maxRuc2014)
    # print("maxThreshold: ", maxThreshold)
    difference = dict()
    for taoThreshold in numpy.arange(0.0000, .500, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame.itertuples():
            for key in keys:
                if (getattr(row, "ruc" + key) > 0):  # previously It was greater equal
                    # tdsc says to iterate only non zero items
                    if (getattr(row, "ruc" + key) < taoThreshold):
                        temp = abs(taoThreshold - getattr(row, "ruc" + key))/2
                        costSum += pow(temp,2)
                        # costSum += abs(taoThreshold - getattr(row, "ruc" + key)) / 2
                        costCount = costCount + 1
                    else:
                        temp = abs(taoThreshold - getattr(row, "ruc" + key))*2
                        pSum += pow(temp,2)
                        # pSum += abs(taoThreshold - getattr(row, "ruc" + key)) * 2
                        penaltyCount = penaltyCount + 1
        if (pSum != 0 and costSum != 0):
            # taoSumDiff = abs(costSum - pSum+ (costCount-penaltyCount)*taoThreshold)
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold)
            # print("Cost Sum: ", costSum," psum: ",pSum," maxSum: ",maxSum," taoDifference: ",taoSumDiff)
            if (maxSum > taoSumDiff):
                # print("this is executing")
                maxSum = taoSumDiff
                maxThreshold = taoThreshold
        # print("Cost Count: ",costCount," penalty count: ",penaltyCount)
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    fig = plt.figure()
    plt.plot(x, y)
    # fig.suptitle('Cost - Penalty Plotting', fontsize=20)
    plt.xlabel('Standard Limit')
    plt.ylabel('Cost - Penalty')
    # fig.savefig('test.jpg')
    plt.show()
    return maxThreshold

def calculateTmin_QR(rucFrame, keys):
    minSum = sys.float_info.max
    minRuc2014 = rucFrame['ruc2014'].min()
    minRuc2015 = rucFrame['ruc2015'].min()
    minThreshold = min(minRuc2015, minRuc2014)
    # print("minThreshold: ",minThreshold)
    difference = dict()
    for taoThreshold in numpy.arange(0.0025, .500, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame.itertuples():
            # print(row)
            for key in keys:
                if (getattr(row, "ruc" + key) < 0):
                    if (getattr(row, "ruc" + key) > ((-1) * taoThreshold)):
                        temp = abs(taoThreshold*(-1) - getattr(row, "ruc" + key))/2
                        costSum += pow(temp, 2)
                        # costSum += abs(taoThreshold*(-1) - getattr(row, "ruc" + key)) / 2
                        costCount = costCount + 1
                    else:
                        temp = abs(taoThreshold*(-1) - getattr(row, "ruc" + key))*2
                        pSum += pow(temp, 2)
                        # pSum += abs(taoThreshold*(-1) - getattr(row, "ruc" + key)) * 2
                        penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            # print("Both are not zero at least once")
            # taoSumDiff = abs(costSum - pSum + (costCount-penaltyCount)*taoThreshold)
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            if (minSum > taoSumDiff):
                # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold*(-1))
                minSum = taoSumDiff
                minThreshold = taoThreshold * (-1)
        # print("Cost Count: ",costCount," penalty count: ",penaltyCount)
    lists = (difference.items())  # sorted by key, return a list of tuples
    w = csv.writer(open("free_of_attack_loss_old.csv", "w"))
    for key, val in difference.items():
        w.writerow([key, val])
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    #
    fig = plt.figure()
    plt.plot(x, y)
    # fig.suptitle('Cost - Penalty Plotting', fontsize=20)
    plt.xlabel('Standard Limit')
    plt.ylabel('Loss')
    # fig.savefig('test.jpg')
    plt.show()
    return minThreshold

def get_loss_for_fix_target_min_QR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    std_limit_array = []
    loss_array = []
    rucFrame_array = []
    target_t_min = -0.17
    target_ruc_num = 0
    is_visited = False
    day_frame_array = []
    # data_frame_array =  []  # to keep the dataframes here
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        # data_frame_array.append(sorted_non_zero_ruc)
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    # data_frame_array_merged = reduce(lambda left, right: pd.merge(left, right, on=['day']), data_frame_array) #merging the dataframes
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # df = pd.DataFrame(merged_array_1, columns=['RUC'])
    # df.to_csv("RUC_min.csv")
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] > lower_limit):
            temp = abs(lower_limit - merged_array[l])/2
            costSum += pow(temp, 2)
            # costSum += abs(lower_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            temp = abs(lower_limit - merged_array[l])*2
            pSum += pow(temp, 2)
            # pSum += abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = (-1)*1
        else:sign = 1
        # print(sign)
        costSum = 0
        pSum = 0
        cost_count = 0
        penalty_count = 0
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.15
        tmin, minSum  = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
        std_limit_array.append(tmin*(-1))
        loss_array.append(minSum)
        if((tmin < target_t_min) and (is_visited == False)):
            is_visited = True
            target_ruc_num = i
            print("For altering: ", i ,"Number of RUCs from ",len(non_zero_ruc_array_copied)," we can reach the targeted max")
            # break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] > lower_limit):
                # temp = abs(lower_limit - non_zero_ruc_array_copied[l])/2
                # costSum += pow(temp, 2)
                costSum += abs(lower_limit - non_zero_ruc_array_copied[l]) / 2
                cost_count = cost_count + 1
            else:
                # temp = abs(lower_limit - non_zero_ruc_array_copied[l])*2
                # pSum += pow(temp, 2)
                pSum += abs(lower_limit - non_zero_ruc_array_copied[l]) * 2
                penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # print("Loss When points are taken according to the order of gradient")
    print("taget ruc number: ",target_ruc_num)
    df = pd.DataFrame(std_limit_array,columns=['std_limit'])
    df1 = pd.DataFrame(loss_array,columns=['loss'])
    merged_fr = pd.concat([df['std_limit'],df1['loss']],axis = 1, keys = ['std_limit','loss'])
    # print(merged_fr)
    # merged_fr.to_csv("std_hyper_2_QR_l1.csv")
    # return non_zero_ruc_array_copied

    # create some x data and some integers for the y axis
    # y = numpy.array(std_limit_array)
    # x = numpy.arange(len(std_limit_array))
    #
    # # plot the data
    # plt.plot(x, y)
    # plt.xlabel("Number of ruc")
    # plt.ylabel("Standard Limit")
    # plt.show()
    return y,target_ruc_num

def get_loss_for_contraint_romax_min_QR_signed(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] > lower_limit):
            temp = abs(lower_limit - merged_array[l])/2
            costSum += pow(temp, 2)
            # costSum += abs(lower_limit - merged_array[l]) / 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) /2
            cost_count = cost_count+ 1
        else:
            temp = abs(lower_limit - merged_array[l])*2
            pSum += pow(temp, 2)
            # pSum += abs(lower_limit - merged_array[l]) * 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        # cost_norm = costSum
        # penalty_norm = pSum
        # if (cost_count > 0):
        #     cost_norm = costSum / cost_count
        # if (penalty_count > 0):
        #     penalty_norm = pSum / penalty_count
        # costFunction[l] = abs(cost_norm - penalty_norm)
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients_signed(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    print("Total RUC count: ",len(non_zero_ruc_array_copied))
    min = numpy.min(non_zero_ruc_array_copied)
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = -1
        else:sign = 1
        costSum = 0
        pSum = 0
        # if (min > (non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07)):
        #     continue
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07451427573
        # print(i,"th gradient: ",gradients[index_of_sorted_list[i]]," residual: ",non_zero_ruc_array_copied[index_of_sorted_list[i]])
        ruc_count = ruc_count + 1
        if(ruc_count >= ROMAX):
            tmin, minSum  = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
            print("tmin after ROMAX QR: ",tmin)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] > lower_limit):
                temp = abs(lower_limit - non_zero_ruc_array_copied[l])/2
                costSum += pow(temp, 2)
                # costSum += abs(lower_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                temp = abs(lower_limit - non_zero_ruc_array_copied[l])*2
                pSum += pow(temp, 2)
                # pSum += abs(lower_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_min_QR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] >= lower_limit):
            # temp = abs(lower_limit - merged_array[l])/2
            # costSum += pow(temp, 2)
            costSum += abs(lower_limit - merged_array[l]) / 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) /2
            cost_count = cost_count+ 1
        else:
            # temp = abs(lower_limit - merged_array[l])*2
            # pSum += pow(temp, 2)
            pSum += abs(lower_limit - merged_array[l]) * 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        # cost_norm = costSum
        # penalty_norm = pSum
        # if (cost_count > 0):
        #     cost_norm = costSum / cost_count
        # if (penalty_count > 0):
        #     penalty_norm = pSum / penalty_count
        # costFunction[l] = abs(cost_norm - penalty_norm)
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    # print("length min: ",len(non_zero_ruc_array_copied))
    # min = numpy.min(non_zero_ruc_array_copied)
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = -1
        else:sign = 1
        costSum = 0
        pSum = 0
        # if (min > (non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07)):
        #     continue
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.12
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07451427573
        # print(i,"th gradient: ",gradients[index_of_sorted_list[i]]," residual: ",non_zero_ruc_array_copied[index_of_sorted_list[i]])
        ruc_count = ruc_count + 1
        if(ruc_count > ROMAX):
            tmin, minSum  = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
            print("tmin after ROMAX QR: ",tmin)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] > lower_limit):
                # temp = abs(lower_limit - non_zero_ruc_array_copied[l])/2
                # costSum += pow(temp, 2)
                costSum += abs(lower_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                # temp = abs(lower_limit - non_zero_ruc_array_copied[l])*2
                # pSum += pow(temp, 2)
                pSum += abs(lower_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    # print(lists)
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # tmin, minSum = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
    # print("tmin after ROMAX QR: ", tmin)
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_min_Random(rucFrame, keys):
    sorted_frame = dict()
    rucFrame_array = []
    for key in keys:
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    non_zero_ruc_array_copied = merged_array.copy()
    randomlist = []
    for i in range(0, 10):
        n = random.randint(0, (len(non_zero_ruc_array_copied)-1))
        randomlist.append(n)
    for ind in randomlist :
        non_zero_ruc_array_copied[ind] = non_zero_ruc_array_copied[ind] - 0.12
    tmin, minSum = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
    print("tmin after ROMAX QR: ", tmin)
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_min_QR_RUC_order(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    non_zero_ruc_array_copied = merged_array.copy()
    min = numpy.min(non_zero_ruc_array_copied)
    for i in range(len(non_zero_ruc_array_copied)):
        costSum = 0
        pSum = 0
        # if (min > (non_zero_ruc_array_copied[i] - 0.07)):
        #     continue
        non_zero_ruc_array_copied[i] = non_zero_ruc_array_copied[i] - 0.08
        ruc_count = ruc_count + 1
        if(ruc_count > ROMAX):
            tmin, minSum  = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
            print("tmin after ROMAX QR: ",tmin)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] > lower_limit):
                temp = abs(lower_limit - non_zero_ruc_array_copied[l])/2
                costSum += pow(temp, 2)
                # costSum += abs(lower_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                temp = abs(lower_limit - non_zero_ruc_array_copied[l])*2
                pSum += pow(temp, 2)
                # pSum += abs(lower_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_max_QR_signed(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key], ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] < upper_limit):
            temp = abs(upper_limit - merged_array[l])/2
            costSum += pow(temp, 2)
            # costFunction[l] = abs(upper_limit - merged_array[l]) /2
            # costSum += abs(upper_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            temp = abs(upper_limit - merged_array[l])*2
            pSum += pow(temp, 2)
            # pSum += abs(upper_limit - merged_array[l]) * 2
            # costFunction[l] = abs(upper_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        # cost_norm = costSum
        # penalty_norm = pSum
        # if (cost_count > 0):
        #     cost_norm = costSum / cost_count
        # if (penalty_count > 0):
        #     penalty_norm = pSum / penalty_count
        # costFunction[l] = abs(cost_norm - penalty_norm)
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients_signed(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    max = numpy.max(non_zero_ruc_array_copied)
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = -1
        else:sign = 1
        costSum = 0
        pSum = 0
        # if (max < (non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07)):
        #     continue
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07451427573
        # print("After: ",non_zero_ruc_array_copied[index_of_sorted_list[i]])

        ruc_count = ruc_count + 1
        if(ruc_count >= ROMAX):
            tmax, maxSum  = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
            print("tmax after ROMAX QR: ",tmax)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] < upper_limit):
                temp = abs(upper_limit - non_zero_ruc_array_copied[l])/2
                costSum += pow(temp, 2)
                # costSum += abs(upper_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                temp = abs(upper_limit - non_zero_ruc_array_copied[l])*2
                pSum += pow(temp, 2)
                # pSum += abs(upper_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_max_QR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key], ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] < upper_limit):
            # temp = abs(upper_limit - merged_array[l])/2
            # costSum += pow(temp, 2)
            costSum += abs(upper_limit - merged_array[l]) / 2
            # costFunction[l] = abs(upper_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            # temp = abs(upper_limit - merged_array[l])*2
            # pSum += pow(temp, 2)
            costFunction[l] = abs(upper_limit - merged_array[l]) * 2
            # pSum += abs(upper_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        # cost_norm = costSum
        # penalty_norm = pSum
        # if (cost_count > 0):
        #     cost_norm = costSum / cost_count
        # if (penalty_count > 0):
        #     penalty_norm = pSum / penalty_count
        # costFunction[l] = abs(cost_norm - penalty_norm)
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    print("length max: ",len(non_zero_ruc_array_copied))
    max = numpy.max(non_zero_ruc_array_copied)
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = -1
        else:sign = 1
        costSum = 0
        pSum = 0
        # if (max < (non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07)):
        #     continue
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.12
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07451427573
        ruc_count = ruc_count + 1
        if(ruc_count > ROMAX):
            tmax, maxSum  = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
            print("tmax after ROMAX QR: ",tmax)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] < upper_limit):
                # temp = abs(upper_limit - non_zero_ruc_array_copied[l])/2
                # costSum += pow(temp, 2)
                costSum += abs(upper_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                # temp = abs(upper_limit - non_zero_ruc_array_copied[l])*2
                # pSum += pow(temp, 2)
                pSum += abs(upper_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # tmax, maxSum = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
    # print("tmax after ROMAX QR: ", tmax)
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_max_QR_RUC_order(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key], ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    # print("Days")
    # print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    non_zero_ruc_array_copied = merged_array.copy()
    max = numpy.max(non_zero_ruc_array_copied)
    for i in range(len(non_zero_ruc_array_copied)):
        costSum = 0
        pSum = 0
        # if (max < (non_zero_ruc_array_copied[i] + 0.07)):
        #     continue
        non_zero_ruc_array_copied[i] = non_zero_ruc_array_copied[i] + 0.08
        ruc_count = ruc_count + 1
        if(ruc_count > ROMAX):
            tmax, maxSum  = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
            print("tmax after ROMAX QR: ",tmax)
            break
        for l in range(len(non_zero_ruc_array_copied)):
            if (non_zero_ruc_array_copied[l] < upper_limit):
                temp = abs(upper_limit - non_zero_ruc_array_copied[l])/2
                costSum += pow(temp, 2)
                # costSum += abs(upper_limit - non_zero_ruc_array_copied[l]) / 2
                # cost_count = cost_count + 1
            else:
                temp = abs(upper_limit - non_zero_ruc_array_copied[l])*2
                pSum += pow(temp, 2)
                # pSum += abs(upper_limit - non_zero_ruc_array_copied[l]) * 2
                # penalty_count = penalty_count + 1
        taoSumDiff = abs(pSum - costSum)
        difference[i] = taoSumDiff
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return non_zero_ruc_array_copied

def get_loss_for_contraint_romax_max_Random(rucFrame, keys):
    sorted_frame = dict()
    rucFrame_array = []
    for key in keys:
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key],ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    non_zero_ruc_array_copied = merged_array.copy()
    randomlist = []
    for i in range(0, 10):
        n = random.randint(0, (len(non_zero_ruc_array_copied)-1))
        randomlist.append(n)
    # print("Length Of the random list: ",len(randomlist))
    for ind in randomlist:
        non_zero_ruc_array_copied[ind] = non_zero_ruc_array_copied[ind] + 0.12
    tmax, maxSum = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
    print("tmax after ROMAX QR: ", tmax)
    return non_zero_ruc_array_copied