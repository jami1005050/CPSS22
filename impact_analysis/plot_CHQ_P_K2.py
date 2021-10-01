#Plot benign Comparison
import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib.ticker
from sklearn.preprocessing import MinMaxScaler
SMALL_SIZE = 12
MEDIUM_SIZE = 12
BIGGER_SIZE = 22
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/result_data/impact/impact_poisoned_C_K2_small_step_del.json')
f_H = open('../test_H/result/impact/impact_poisoned_H_K2_small_step_del.json')
f_Q = open('../test_QP/result/impact/impact_poisoned_Q_k2_Small_step_del.json')
f_QL2 = open('../test_QP/result/impact/impact_poisoned_Q_k2_L2_small_step_del.json')
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
result_frame['romax']= pd.to_numeric(result_frame['romax'])
result_frame['del_avg']= pd.to_numeric(result_frame['del_avg'])
# result_frame['epsilon']= pd.to_numeric(result_frame['epsilon'])
# print(result_frame[result_frame['epsilon'] == str(0.012840280834311983)])
# print(result_frame[result_frame['impact_H'] < result_frame['impact_C']])
print(len(result_frame))
te = result_frame[result_frame['impact_H'] < result_frame['impact_C']]
te.to_csv('Quantile_HC_.006.csv')
print(te)
for index,r in te.iterrows():
    print(r.romax,' ',r.epsilon,' ',r.del_avg,' ',r.impact_H,' ',r.impact_C)

impact= result_frame[ ( result_frame['romax'] == 6 ) &( result_frame['epsilon'] == str(0.012840280834311983))
                      & ( result_frame['del_avg'] == 90)]# ( result_frame['epsilon'] == str(0.06714763183) )
impact_FIX_RO = result_frame[ ( result_frame['romax'] == 2 )&
                              (result_frame['del_avg'] > 50) &
                              (result_frame['del_avg'] < 300)
                              ]# ( result_frame['epsilon'] == str(0.06714763183) )

impact['epsilon'] = impact['epsilon'].astype(float)
impact['epsilon'].round(decimals=3)
temp_df = impact[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
# print(temp_df.to_latex())

# print("******Non Quantile*******")
f_C = open('../test_C/result_data/impact/impact_poisoned_C_non_Q_K2_small_step_del.json')
f_H = open('../test_H/result/impact/impact_poisoned_H_non_Q_K2_small_step_del.json')
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
    # print(group[['romax','epsilon','del_avg','impact_Q','impact_H','impact_C']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_Q', 'impact_Q']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_H', 'impact_H']])
    # print(group[['romax', 'epsilon', 'del_avg', 'days_C', 'impact_C']])
    # print(temp_df.to_latex())
    i = i+1
    # break
result_frame['romax']= pd.to_numeric(result_frame['romax'])
result_frame['del_avg']= pd.to_numeric(result_frame['del_avg'])
# result_frame['epsilon']= pd.to_numeric(result_frame['epsilon'])
# print(result_frame[result_frame['impact_H'] > result_frame['impact_C']])
print("Non Quantile")
print(len(result_frame))
te = result_frame[result_frame['impact_H'] < result_frame['impact_C']]
print(te)
te.to_csv('Non_Quantile_HC_beta_.006.csv')
for index,r in te.iterrows():
    print(r.romax,' ',r.epsilon,' ',r.del_avg,' ',r.impact_H,' ',r.impact_C)
impact_nQ= result_frame[ ( result_frame['romax'] == 6 ) & ( result_frame['epsilon'] == str( 0.012840280834311983 ))
                         & ( result_frame['del_avg'] ==90)  ] # ( result_frame['epsilon'] == str( 0.06714763183) )&
impact_nQ_FIX_RO = result_frame[ ( result_frame['romax'] == 2 ) &
                                 ( result_frame['del_avg'] > 50 ) &
                                 ( result_frame['del_avg'] < 300)]# ( result_frame['epsilon'] == str(0.06714763183) )
impact_nQ_FIX_RO['epsilon'] = impact_nQ_FIX_RO['epsilon'].astype(float)
impact_nQ_FIX_RO['epsilon'].round(decimals=3)
temp_df = impact_nQ[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
# print(temp_df.to_latex())
# region tesitng del avg varies Or Epsilon varies
# # plt.ylim(5,150)
# # fig = plt.subplots(figsize=(16, 8))
# # plt.plot(impact_nQ['epsilon'],impact_nQ['impact_H'],marker ='>',color = 'c',label = 'NQH')
# plt.plot(impact_nQ['del_avg'],impact_nQ['impact_C'],marker ='^',color = 'tab:orange',label = 'NQC',linestyle = '-.')
# plt.plot(impact['del_avg'],impact['impact_Q'],marker ='<',color = 'b',label ="QL1",linestyle = '--')
# # plt.plot(impact['del_avg'],impact['impact_QL2'],marker ='D',color = 'tab:olive',label ="QL2",linestyle = '-.')
# # plt.plot(impact['del_avg'],impact['impact_H'],marker ='>',color = 'r',label = 'QH',linestyle = ':')
# # plt.plot(impact['del_avg'],impact['impact_C'],marker ='^',color = 'g',label = 'QC',linestyle ='--',dashes=(5, 1))
#
# plt.xlabel(r'Test $\delta_{avg}$')
# # plt.xticks( rotation=45 )
# plt.ylabel("Impact")
# loc = matplotlib.ticker.LinearLocator(numticks=8)
# plt.gca().xaxis.set_major_locator(loc)
# plt.legend()
# plt.show()
#endregion

# region Bar plot
index_ar = impact.index
# print(impact)
# plt.bar(["QL1","QL2","QH","QC","NQH","NQC"],
#         [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C'],
#          impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],color=[ 'violet','blue','cyan','tab:orange','tab:green','tab:olive'])

plt.bar(["QL1","QL2","QH","QC"],
        [impact.at[index_ar[0],'impact_Q'],impact.at[index_ar[0],'impact_QL2'],impact.at[index_ar[0],'impact_H'],impact.at[index_ar[0],'impact_C']],
        color=[ 'violet','blue','cyan','tab:orange'])
# plt.bar(["QC","NQH","NQC"],
#         [impact.at[index_ar[0],'impact_C'],impact_nQ.at[index_ar[0],'impact_H'],impact_nQ.at[index_ar[0],'impact_C']],
#         color=['violet','tab:green','tab:olive'])

plt.ylabel("Impact")
plt.ylim(660,720)
plt.show()
#endregion


#3D plot

# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# X = []
# Y = []
# Z = []
# for index,row in impact_nQ_FIX_RO.iterrows():
#     X.append(int(row.del_avg))
#     Y.append(float(row.epsilon))
#     Z.append(float(row.impact_Q))
# x = np.reshape(X, (10, 26))
# y = np.reshape(Y, (10, 26))
# z = np.reshape(Z, (10, 26))
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# c1 = ax.plot_surface(x, y, z,label='h')
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# # h._facecolors2d=h._facecolors3d
# c1._facecolors2d = c1._facecolor3d
# c1._edgecolors2d = c1._edgecolor3d# plt.show()
# print(impact_nQ_FIX_RO)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.xaxis.labelpad=20
# ax.yaxis.labelpad=20
# ax.zaxis.labelpad=20
# ax.dist = 13
impact_nQ_FIX_RO['del_avg'] = pd.to_numeric(impact_nQ_FIX_RO['del_avg'])
impact_nQ_FIX_RO['impact_H'] = pd.to_numeric(impact_nQ_FIX_RO['impact_H'])
impact_nQ_FIX_RO['impact_C'] = pd.to_numeric(impact_nQ_FIX_RO['impact_C'])
impact_nQ_FIX_RO['impact_Q'] = pd.to_numeric(impact_nQ_FIX_RO['impact_Q'])
p = ax.plot_trisurf(impact_FIX_RO['del_avg'],
               impact_FIX_RO['epsilon'],
               impact_FIX_RO['impact_C'],label ='QC',color='tab:olive',alpha=0.45,)

# r = ax.plot_trisurf(impact_nQ_FIX_RO['del_avg'],
#                impact_nQ_FIX_RO['epsilon'],
#                impact_nQ_FIX_RO['impact_H'],label ='NQH',color='red',alpha=0.5,)

q= ax.plot_trisurf(impact_nQ_FIX_RO['del_avg'],
               impact_nQ_FIX_RO['epsilon'],
               impact_nQ_FIX_RO['impact_C'],label='NQC',color='tab:blue',alpha=0.75,)
p._facecolors2d = p._facecolor3d
p._edgecolors2d = p._edgecolor3d

q._facecolors2d = q._facecolor3d
q._edgecolors2d = q._edgecolor3d

# r._facecolors2d = r._facecolor3d
# r._edgecolors2d = r._edgecolor3d
# ax.scatter3D(impact_nQ_FIX_RO['del_avg'],
#                impact_nQ_FIX_RO['epsilon'],
#                impact_nQ_FIX_RO['impact_Q'],
#                  marker='^',label ='QL1')
#
# ax.scatter3D(impact_nQ_FIX_RO['del_avg'],
#                impact_nQ_FIX_RO['epsilon'],
#                impact_nQ_FIX_RO['impact_C'],
#                  marker='>',label='C')
ax.set_xlabel('$\delta_{avg}^e$',labelpad=10)
ax.set_ylabel('$\epsilon$',labelpad=10)
ax.set_zlabel('Impact',labelpad=10)
ax.set_xlim3d(min(impact_nQ_FIX_RO['del_avg']),max(impact_nQ_FIX_RO['del_avg']))
ax.set_ylim3d(min(impact_nQ_FIX_RO['epsilon']),max(impact_nQ_FIX_RO['epsilon']))
ax.set_zlim3d(min(impact_FIX_RO['impact_C']),1400)
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
ax.zaxis.set_major_locator(plt.MaxNLocator(5))
ax.view_init(elev=20., azim=-120.)
# fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
plt.legend()
plt.show()