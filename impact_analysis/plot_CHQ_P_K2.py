#Plot benign Comparison
import matplotlib.pyplot as plt
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

SMALL_SIZE = 12
MEDIUM_SIZE = 12
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/impact_poisoned_C_K2.json' )
f_H = open('../test_H/impact_poisoned_H_K2.json' )
f_Q = open('../test_QP/impact_poisoned_Q_k2.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        # print(impact_dict_C[key][key1].keys())
        for key2 in impact_dict_C[key][key1]['0.006'].keys():
            Efa_C = impact_dict_C[key][key1]['0.006'][key2]['Efa']
            Efa_H = impact_dict_H[key][key1]['0.006'][key2]['Efa']
            Efa_Q = impact_dict_Q[key][key1][key2]['Efa']
            impact_C = impact_dict_C[key][key1]['0.006'][key2]['impact']
            impact_H = impact_dict_H[key][key1]['0.006'][key2]['impact']
            impact_Q = impact_dict_Q[key][key1][key2]['impact']
            if(Efa_Q>365):Efa_Q = 365
            if(Efa_H>365):Efa_H = 365
            if(Efa_C>365):Efa_C = 365
            temp = {'romax':key,'epsilon':key1,'del_avg':key2,'impact_C':impact_C,
                    'impact_Q':impact_Q,'impact_H':impact_H,'Efa_Q':Efa_Q,'Efa_C':Efa_C,'Efa_H':Efa_H}
            result.append(temp)


result_frame = pd.DataFrame(result)
temp_scaled = result_frame.copy(deep=True)
min_max_scaler = MinMaxScaler()
temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']] = min_max_scaler.fit_transform(temp_scaled[['impact_Q','impact_H','impact_C','Efa_Q', 'Efa_H', 'Efa_C']])
# print(temp_scaled)
temp_scaled.to_csv('scaled_Q.csv')
groups = result_frame.groupby('del_avg')
# 2         0.04301103139  small large perturbation

color_list = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
i = 0
for key,group in groups:
    # temp_df = group[group['romax']==str(2)][['Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
    # print(temp_df.to_latex())
    print(group[['romax','epsilon','del_avg','impact_Q','impact_H','impact_C']])

    # foucsed_frame = group[(group['epsilon']==str(0.04301103139)) & (group['romax']==str(2))]
    # print(foucsed_frame)
    # plt.scatter(foucsed_frame['Efa_Q'],foucsed_frame['impact_Q'],marker ='<',color = 'b')
    # plt.scatter(foucsed_frame['Efa_H'],foucsed_frame['impact_H'],marker ='>',color = 'r')
    # plt.scatter(foucsed_frame['Efa_C'],foucsed_frame['impact_C'],marker ='^',color = 'g')
    # plt.impact_analysis([foucsed_frame['Efa_Q'],foucsed_frame['Efa_H'],foucsed_frame['Efa_C']],
    #          [foucsed_frame['impact_Q'],foucsed_frame['impact_H'],foucsed_frame['impact_C']],color = color_list[i],label=key)
    i = i+1
    # break

# print(result_frame[result_frame['romax']== str(2)])
#region bar plot
impact= result_frame[ ( result_frame['romax'] == str(6) ) & ( result_frame['epsilon'] == str(0.012840280834311983) ) & ( result_frame['del_avg'] == str(100) ) ]
# print(impact)
# plt.bar(["QL1","H","C"], [impact.at[180,'impact_Q'],impact.at[180,'impact_H'],impact.at[180,'impact_C']],color=[ 'violet','blue','cyan'])
# plt.ylabel("Impact")
# plt.ylim(30,85)
# plt.show()
#endregion

#region line plot with varying epsilon
# impact= result_frame[ ( result_frame['romax'] == str(2) )  & ( result_frame['del_avg'] == str(100) ) ]
# impact['epsilon'] = impact['epsilon'].astype(float)
#
# impact.round(decimals=4)
# print(impact)
# plt.ylim(5,150)
# plt.plot(impact['epsilon'],impact['impact_Q'],marker ='<',color = 'b',label ="Q")
# plt.plot(impact['epsilon'],impact['impact_H'],marker ='>',color = 'r',label = 'H')
# plt.plot(impact['epsilon'],impact['impact_C'],marker ='^',color = 'g',label = 'C')
# plt.xlabel("Epsilon")
# plt.xticks( rotation=90 )
# plt.ylabel("Impact")
# plt.legend()
# plt.show()
#endregion

#region line plot with varying romax
# impact= result_frame[ ( result_frame['epsilon'] == str(0.05507933161) )  & ( result_frame['del_avg'] == str(100) ) ]
# print(impact)
# plt.ylim(5,150)
# plt.plot(impact['romax'],impact['impact_Q'],marker ='<',color = 'b',label ="Q")
# plt.plot(impact['romax'],impact['impact_H'],marker ='>',color = 'r',label = 'H')
# plt.plot(impact['romax'],impact['impact_C'],marker ='^',color = 'g',label = 'C')
# plt.xlabel("romax")
# # plt.xticks( rotation=90 )
# plt.ylabel("Impact")
# plt.legend()
# plt.show()
#endregion
