#Plot benign Comparison
import matplotlib.pyplot as plt
import json
import pandas as pd

SMALL_SIZE = 12
MEDIUM_SIZE = 12
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/impact_poisoned_CRA_non_Q.json' )
f_H = open('../test_H/impact_poisoned_HRA_non_Q.json' )
f_Q = open('../test_QP/impact_poisoned_QRA.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        # print(impact_dict_C[key][key1].keys())
        Efa_C = impact_dict_C[key][key1]['0.006']['Efa']
        Efa_H = impact_dict_H[key][key1]['0.006']['Efa']
        Efa_Q = impact_dict_Q[key][key1]['Efa']
        impact_C = impact_dict_C[key][key1]['0.006']['impact']
        impact_H = impact_dict_H[key][key1]['0.006']['impact']
        impact_Q = impact_dict_Q[key][key1]['impact']
        if(Efa_Q>365):Efa_Q = 365
        if(Efa_H>365):Efa_H = 365
        if(Efa_C>365):Efa_C = 365
        temp = {'tr_del_avg':key,'del_avg':key1,'impact_C':impact_C,
                'impact_Q':impact_Q,'impact_H':impact_H,'Efa_Q':Efa_Q,'Efa_C':Efa_C,'Efa_H':Efa_H}
        result.append(temp)


result_frame = pd.DataFrame(result)
groups = result_frame.groupby('tr_del_avg')
# 2         0.04301103139  small large perturbation

color_list = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
i = 0
for key,group in groups:
    print(group[['Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']])

    # foucsed_frame = group[(group['epsilon']==str(0.04301103139)) & (group['romax']==str(2))]
    # print(foucsed_frame)
    # plt.scatter(foucsed_frame['Efa_Q'],foucsed_frame['impact_Q'],marker ='<',color = 'b')
    # plt.scatter(foucsed_frame['Efa_H'],foucsed_frame['impact_H'],marker ='>',color = 'r')
    # plt.scatter(foucsed_frame['Efa_C'],foucsed_frame['impact_C'],marker ='^',color = 'g')
    # plt.impact_analysis([foucsed_frame['Efa_Q'],foucsed_frame['Efa_H'],foucsed_frame['Efa_C']],
    #          [foucsed_frame['impact_Q'],foucsed_frame['impact_H'],foucsed_frame['impact_C']],color = color_list[i],label=key)
    i = i+1
# plt.xlabel("Efa")
# plt.ylabel("Impact")
# plt.legend()
# plt.show()