#here we have done the impact anlyasis for different romal and del avg in the test set

#Plot benign Comparison
import matplotlib.ticker
import matplotlib.pyplot as plt
import json
import pandas as pd

SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/impact_poisoned_ro_del_CRA.json' )
f_H = open('../test_H/impact_poisoned_ro_del_HRA.json' )
# f_Q = open('../test_QP/impact_poisoned_QRA_small_step_del.json' )
# f_QL2 = open('../test_QP/impact_poisoned_QRA_L2_small_step_del.json' )
# impact_dict_QL2 = json.load(f_QL2)
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
# impact_dict_Q = json.load(f_Q)

result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        for key2 in impact_dict_C[key][key1].keys():
            Efa_C = impact_dict_C[key][key1][key2]['0.006']['Efa']
            Efa_H = impact_dict_H[key][key1][key2]['0.006']['Efa']
            # Efa_Q = impact_dict_Q[key][key1]['Efa']
            # Efa_QL2 = impact_dict_QL2[key][key1]['Efa']
            impact_C = impact_dict_C[key][key1][key2]['0.006']['impact']
            impact_H = impact_dict_H[key][key1][key2]['0.006']['impact']
            # impact_Q = impact_dict_Q[key][key1]['impact']
            # impact_QL2 = impact_dict_QL2[key][key1]['impact']
            # days_Q = impact_dict_Q[key][key1]['days_undetected']
            # days_QL2 = impact_dict_QL2[key][key1]['days_undetected']
            days_H = impact_dict_H[key][key1][key2]['0.006']['days_undetected']
            days_C = impact_dict_C[key][key1][key2]['0.006']['days_undetected']
            # if (Efa_Q > 365): Efa_Q = 365
            if (Efa_H > 365): Efa_H = 365
            if (Efa_C > 365): Efa_C = 365
            # if (Efa_QL2 > 365): Efa_QL2 = 365
            # temp = {'tr_del_avg': key, 'del_avg': key1, 'impact_C': impact_C, 'days_Q': days_Q, 'days_H': days_H,
            #         'days_C': days_C, 'impact_QL2': impact_QL2, 'days_QL2': days_QL2, 'Efa_QL2': Efa_QL2,
            #         'impact_Q': impact_Q, 'impact_H': impact_H, 'Efa_Q': Efa_Q, 'Efa_C': Efa_C, 'Efa_H': Efa_H}
            temp = {'tr_del_avg': key, 'del_avg': key1, 'impact_C': impact_C, 'days_H': days_H,
                    'days_C': days_C,  'romal':key2,
                     'impact_H': impact_H,'Efa_C': Efa_C, 'Efa_H': Efa_H}

            result.append(temp)

result_frame = pd.DataFrame(result)
groups = result_frame.groupby('tr_del_avg')
color_list = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
i = 0
for key,group in groups:
    # print(group[['tr_del_avg','del_avg','impact_Q','impact_H','impact_C']])
    # print(group[['tr_del_avg','del_avg','days_Q','impact_Q']])
    # print(group[['tr_del_avg','del_avg','days_H','impact_H']])
    # print(group[['tr_del_avg','del_avg','days_C','impact_C']])
    # temp_df = group[['Efa_Q', 'Efa_H', 'Efa_C', 'impact_Q', 'impact_H', 'impact_C']]
    i = i+1
#region impact when testing delavg varies
impact= result_frame[ ( result_frame['tr_del_avg'] == str(100) )
                    & ( result_frame['romal'] == str(0.70)) ]#( result_frame['tr_del_avg'] == str(175) )
# temp_df = impact[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]

f_C = open('../test_C/impact_poisoned_ro_del_nonQ_CRA.json' )
f_H = open('../test_H/impact_poisoned_ro_del_nonQ_HRA.json' )
# f_Q = open('../test_QP/impact_poisoned_QRA_small_step_del.json' )
# f_QL2 = open('../test_QP/impact_poisoned_QRA_L2_small_step_del.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
# impact_dict_Q = json.load(f_Q)
# impact_dict_QL2 = json.load(f_QL2)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        for key2 in impact_dict_C[key][key1].keys():
            # print(impact_dict_C[key][key1].keys())
            Efa_C = impact_dict_C[key][key1][key2]['0.006']['Efa']
            Efa_H = impact_dict_H[key][key1][key2]['0.006']['Efa']
            # Efa_Q = impact_dict_Q[key][key1]['Efa']
            # Efa_QL2 = impact_dict_QL2[key][key1]['Efa']
            impact_C = impact_dict_C[key][key1][key2]['0.006']['impact']
            impact_H = impact_dict_H[key][key1][key2]['0.006']['impact']
            # impact_Q = impact_dict_Q[key][key1]['impact']
            # impact_QL2 = impact_dict_QL2[key][key1]['impact']
            # days_Q = impact_dict_Q[key][key1]['days_undetected']
            # days_QL2 = impact_dict_QL2[key][key1]['days_undetected']
            days_H = impact_dict_H[key][key1][key2]['0.006']['days_undetected']
            days_C = impact_dict_C[key][key1][key2]['0.006']['days_undetected']
            # if (Efa_Q > 365): Efa_Q = 365
            if (Efa_H > 365): Efa_H = 365
            if (Efa_C > 365): Efa_C = 365
            # if (Efa_QL2 > 365): Efa_QL2 = 365
            # temp = {'tr_del_avg': key, 'del_avg': key1, 'impact_C': impact_C, 'days_Q': days_Q, 'days_H': days_H,
            #         'days_C': days_C,'impact_QL2': impact_QL2,'days_QL2': days_QL2,'Efa_QL2': Efa_QL2,
            #         'impact_Q': impact_Q, 'impact_H': impact_H, 'Efa_Q': Efa_Q, 'Efa_C': Efa_C, 'Efa_H': Efa_H}
            temp = {'tr_del_avg': key, 'del_avg': key1, 'impact_C': impact_C, 'days_H': days_H,'romal':key2,
                    'days_C': days_C,'impact_H': impact_H, 'Efa_C': Efa_C, 'Efa_H': Efa_H}

            result.append(temp)

result_frame = pd.DataFrame(result)
groups = result_frame.groupby('tr_del_avg')
i = 0
print("***********Non Quantile**********")
for key,group in groups:
    # print(group[['tr_del_avg','del_avg','impact_Q','impact_H','impact_C']])
    # print(group[['tr_del_avg', 'del_avg', 'days_Q', 'impact_Q']])
    # print(group[['tr_del_avg', 'del_avg', 'days_H', 'impact_H']])
    # print(group[['tr_del_avg', 'del_avg', 'days_C', 'impact_C']])
    # temp_df = group[['Efa_Q', 'Efa_H', 'Efa_C', 'impact_Q', 'impact_H', 'impact_C']]
    i = i+1

impact_nQ= result_frame[( result_frame['tr_del_avg'] == str(100) )
                        & (result_frame['romal'] == str(0.70)) ]#( result_frame['tr_del_avg'] == str(175) )#&
# temp_df = impact_nQ[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
#region tesitng del avg varies
# plt.ylim(5,150)
# fig = plt.subplots(figsize=(12, 6))
plt.plot(impact_nQ['del_avg'],impact_nQ['impact_H'],marker ='>',color = 'c',label = 'NQH',markevery = 5)
plt.plot(impact_nQ['del_avg'],impact_nQ['impact_C'],marker ='^',color = 'tab:orange',label = 'NQC',markevery = 5)
# plt.plot(impact['del_avg'],impact['impact_Q'],marker ='<',color = 'b',label ="QL1")
# plt.plot(impact['del_avg'],impact['impact_QL2'],marker ='D',color = 'tab:olive',label ="QL1")
plt.plot(impact['del_avg'],impact['impact_H'],marker ='>',color = 'r',label = 'QH',markevery = 5)
plt.plot(impact['del_avg'],impact['impact_C'],marker ='^',color = 'g',label = 'QC',markevery = 5)
plt.xlabel(r'$\delta_{avg}$')
plt.xticks( rotation=90 )
plt.ylabel("Impact")
# plt.xlim(0,170)
loc = matplotlib.ticker.LinearLocator(numticks=10)
plt.gca().xaxis.set_major_locator(loc)
plt.legend()

plt.show()
#endregion
print(impact)
print(impact_nQ)
index_ar = impact.index
#region bar plot
# # plt.bar(["QL1","QL2","QH","QC","NQH","NQC"],
# #         [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C'],
# #          impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],color=[ 'violet','blue','cyan','tab:orange','tab:green','tab:olive'])
# plt.bar(["QH","QC","NQH","NQC"],
#         [impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C'],
#          impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],color=['cyan','tab:orange','tab:green','tab:olive'])
#
# # plt.bar(["QL1","QL2","QH","QC"],
# #         [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C']],
# #         color=[ 'violet','blue','cyan','tab:orange'])
#
# # plt.bar(["QC","NQH","NQC"],
# #         [impact.at[index_ar[0],'impact_C'],impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],
# #         color=['violet','tab:green','tab:olive'])
# plt.ylabel("Impact")
# # plt.ylim(1100,1150)
# plt.show()
#endregion
