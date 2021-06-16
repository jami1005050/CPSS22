#Plot benign Comparison
import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib.ticker
from sklearn.preprocessing import MinMaxScaler
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/impact_poisoned_C_K2_small_step_del.json' )
f_H = open('../test_H/impact_poisoned_H_K2_small_step_del.json' )
f_Q = open('../test_QP/impact_poisoned_Q_k2_Small_step_del.json' )
f_QL2 = open('../test_QP/impact_poisoned_Q_k2_L2_small_step_del.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
impact_dict_QL2 = json.load(f_QL2)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        # print(impact_dict_C[key][key1].keys())
        for key2 in impact_dict_C[key][key1]['0.006'].keys():
            Efa_C = impact_dict_C[key][key1]['0.006'][key2]['Efa']
            Efa_H = impact_dict_H[key][key1]['0.006'][key2]['Efa']
            Efa_Q = impact_dict_Q[key][key1][key2]['Efa']
            Efa_QL2 = impact_dict_QL2[key][key1][key2]['Efa']
            impact_C = impact_dict_C[key][key1]['0.006'][key2]['impact']
            impact_H = impact_dict_H[key][key1]['0.006'][key2]['impact']
            impact_Q = impact_dict_Q[key][key1][key2]['impact']
            impact_QL2 = impact_dict_QL2[key][key1][key2]['impact']
            days_Q = impact_dict_Q[key][key1][key2]['days_undetected']
            days_QL2 = impact_dict_QL2[key][key1][key2]['days_undetected']
            days_H = impact_dict_H[key][key1]['0.006'][key2]['days_undetected']
            days_C = impact_dict_C[key][key1]['0.006'][key2]['days_undetected']
            if(Efa_Q>365):Efa_Q = 365
            if(Efa_H>365):Efa_H = 365
            if(Efa_C>365):Efa_C = 365
            temp = {'romax':key,'epsilon':key1,'del_avg':key2,'impact_C':impact_C,
                    'days_Q':days_Q,'days_QL2':days_QL2,'days_H':days_H,'days_C':days_C,
                    'impact_Q':impact_Q,'impact_QL2':impact_QL2,'impact_H':impact_H,
                    'Efa_Q':Efa_Q,'Efa_QL2':Efa_QL2,'Efa_C':Efa_C,'Efa_H':Efa_H}
            result.append(temp)

result_frame = pd.DataFrame(result)
# temp_scaled = result_frame.copy(deep=True)
# min_max_scaler = MinMaxScaler()
# temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']] = min_max_scaler.fit_transform(temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']])
# print(temp_scaled)
# temp_scaled.to_csv('scaled_Q.csv')
groups = result_frame.groupby(['romax','epsilon'])
# 2         0.04301103139  small large perturbation

color_list = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
i = 0
for key,group in groups:#[group['romax']==str(2)]
    # temp_df = group[['Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
    # print(temp_df.to_latex())
    # print(group[['romax','epsilon','del_avg','impact_Q','impact_H','impact_C']])
    # print(group[['romax','epsilon','del_avg', 'days_Q', 'impact_Q']])
    # print(group[['romax','epsilon','del_avg', 'days_H', 'impact_H']])
    # print(group[['romax','epsilon','del_avg', 'days_C', 'impact_C']])
    # foucsed_frame = group[(group['epsilon']==str(0.04301103139)) & (group['romax']==str(2))]
    # print(foucsed_frame)
    # plt.scatter(foucsed_frame['Efa_Q'],foucsed_frame['impact_Q'],marker ='<',color = 'b')
    # plt.scatter(foucsed_frame['Efa_H'],foucsed_frame['impact_H'],marker ='>',color = 'r')
    # plt.scatter(foucsed_frame['Efa_C'],foucsed_frame['impact_C'],marker ='^',color = 'g')
    # plt.impact_analysis([foucsed_frame['Efa_Q'],foucsed_frame['Efa_H'],foucsed_frame['Efa_C']],
    #          [foucsed_frame['impact_Q'],foucsed_frame['impact_H'],foucsed_frame['impact_C']],color = color_list[i],label=key)
    i = i+1
    break

impact= result_frame[ ( result_frame['romax'] == str(6) ) &( result_frame['epsilon'] == str( 0.012840280834311983) )& ( result_frame['del_avg'] == str(130))]# ( result_frame['epsilon'] == str(0.06714763183) )

impact['epsilon'] = impact['epsilon'].astype(float)
impact['epsilon'].round(decimals=3)
temp_df = impact[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
print(temp_df.to_latex())

print("******Non Quantile*******")
f_C = open('../test_C/impact_poisoned_C_non_Q_K2_small_step_del.json' )
f_H = open('../test_H/impact_poisoned_H_non_Q_K2_small_step_del.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        for key2 in impact_dict_C[key][key1]['0.006'].keys():
            Efa_C = impact_dict_C[key][key1]['0.006'][key2]['Efa']
            Efa_H = impact_dict_H[key][key1]['0.006'][key2]['Efa']
            Efa_Q = impact_dict_Q[key][key1][key2]['Efa']
            Efa_QL2 = impact_dict_QL2[key][key1][key2]['Efa']
            impact_C = impact_dict_C[key][key1]['0.006'][key2]['impact']
            impact_H = impact_dict_H[key][key1]['0.006'][key2]['impact']
            impact_Q = impact_dict_Q[key][key1][key2]['impact']
            impact_QL2 = impact_dict_QL2[key][key1][key2]['impact']
            days_Q = impact_dict_Q[key][key1][key2]['days_undetected']
            days_QL2 = impact_dict_QL2[key][key1][key2]['days_undetected']
            days_H = impact_dict_H[key][key1]['0.006'][key2]['days_undetected']
            days_C = impact_dict_C[key][key1]['0.006'][key2]['days_undetected']
            if (Efa_Q > 365): Efa_Q = 365
            if (Efa_H > 365): Efa_H = 365
            if (Efa_C > 365): Efa_C = 365
            temp = {'romax': key, 'epsilon': key1, 'del_avg': key2, 'impact_C': impact_C,
                    'days_Q': days_Q, 'days_QL2': days_QL2, 'days_H': days_H, 'days_C': days_C,
                    'impact_Q': impact_Q, 'impact_QL2': impact_QL2, 'impact_H': impact_H,
                    'Efa_Q': Efa_Q, 'Efa_QL2': Efa_QL2, 'Efa_C': Efa_C, 'Efa_H': Efa_H}
            result.append(temp)

result_frame = pd.DataFrame(result)
# temp_scaled = result_frame.copy(deep=True)
# min_max_scaler = MinMaxScaler()
# temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']] = min_max_scaler.fit_transform(temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']])
# # print(temp_scaled)
# temp_scaled.to_csv('scaled_nonQ.csv')
groups = result_frame.groupby(['romax','epsilon'])
i = 0
for key,group in groups:#[group['romax'] == str(2)]
    # temp_df = group[['Efa_Q', 'Efa_H', 'Efa_C', 'impact_Q', 'impact_H', 'impact_C']]
    print(group[['romax','epsilon','del_avg','impact_Q','impact_H','impact_C']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_Q', 'impact_Q']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_H', 'impact_H']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_C', 'impact_C']])
    # print(temp_df.to_latex())
    i = i+1
    # break

impact_nQ= result_frame[ ( result_frame['romax'] == str(6) ) & ( result_frame['epsilon'] == str( 0.012840280834311983) ) & ( result_frame['del_avg'] ==str(130))  ] # ( result_frame['epsilon'] == str( 0.06714763183) )&
# print(impact_nQ)
impact_nQ['epsilon'] = impact_nQ['epsilon'].astype(float)
impact_nQ['epsilon'].round(decimals=3)
temp_df = impact_nQ[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
print(temp_df.to_latex())
#region tesitng del avg varies Or Epsilon varies
# plt.ylim(5,150)
# fig = plt.subplots(figsize=(16, 8))
# plt.plot(impact_nQ['epsilon'],impact_nQ['impact_H'],marker ='>',color = 'c',label = 'NQH')
plt.plot(impact_nQ['del_avg'],impact_nQ['impact_C'],marker ='^',color = 'tab:orange',label = 'NQC',linestyle = '-.')
plt.plot(impact['del_avg'],impact['impact_Q'],marker ='<',color = 'b',label ="QL1",linestyle = '--')
# plt.plot(impact['del_avg'],impact['impact_QL2'],marker ='D',color = 'tab:olive',label ="QL2",linestyle = '-.')
# plt.plot(impact['del_avg'],impact['impact_H'],marker ='>',color = 'r',label = 'QH',linestyle = ':')
# plt.plot(impact['del_avg'],impact['impact_C'],marker ='^',color = 'g',label = 'QC',linestyle ='--',dashes=(5, 1))

plt.xlabel(r'Test $\delta_{avg}$')
# plt.xticks( rotation=45 )
plt.ylabel("Impact")
loc = matplotlib.ticker.LinearLocator(numticks=8)
plt.gca().xaxis.set_major_locator(loc)
plt.legend()
plt.show()
#endregion

# region Bar plot
index_ar = impact.index
print(impact)
plt.bar(["QL1","QL2","QH","QC","NQH","NQC"],
        [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C'],
         impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],color=[ 'violet','blue','cyan','tab:orange','tab:green','tab:olive'])

# # plt.bar(["QL1","QL2","QH","QC"],
# #         [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C']],
# #         color=[ 'violet','blue','cyan','tab:orange'])
#
# # plt.bar(["QC","NQH","NQC"],
# #         [impact.at[index_ar[0],'impact_C'],impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],
# #         color=['violet','tab:green','tab:olive'])
#
plt.ylabel("Impact")
# plt.ylim(120,160)
plt.show()
#endregion