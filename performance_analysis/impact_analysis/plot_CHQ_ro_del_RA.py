#here we have done the impact anlyasis for different romal and del avg in the test set

#Plot benign Comparison
import matplotlib.ticker
import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib

SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../../test_C/result_data/impact/impact_poisoned_ro_del_CRA.json')
f_H = open('../../test_H/result/impact/impact_poisoned_ro_del_HRA.json')
f_Q = open('../../test_QP/result/impact/impact_poisoned_ro_del_QRA.json')
f_QL2 = open('../../test_QP/result/impact/impact_poisoned_ro_del_L2_QRA.json')
impact_dict_QL2 = json.load(f_QL2)
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        for key2 in impact_dict_C[key][key1].keys():
            Efa_C = impact_dict_C[key][key1][key2]['0.006']['Efa']
            Efa_H = impact_dict_H[key][key1][key2]['0.006']['Efa']
            Efa_Q = impact_dict_Q[key][key1][key2]['Efa']
            Efa_QL2 = impact_dict_QL2[key][key1][key2]['Efa']
            impact_C = impact_dict_C[key][key1][key2]['0.006']['impact']
            impact_H = impact_dict_H[key][key1][key2]['0.006']['impact']
            impact_Q = impact_dict_Q[key][key1][key2]['impact']
            impact_QL2 = impact_dict_QL2[key][key1][key2]['impact']
            days_Q = impact_dict_Q[key][key1][key2]['days_undetected']
            days_QL2 = impact_dict_QL2[key][key1][key2]['days_undetected']
            days_H = impact_dict_H[key][key1][key2]['0.006']['days_undetected']
            days_C = impact_dict_C[key][key1][key2]['0.006']['days_undetected']
            if (Efa_Q > 365): Efa_Q = 365
            if (Efa_H > 365): Efa_H = 365
            if (Efa_C > 365): Efa_C = 365
            if (Efa_QL2 > 365): Efa_QL2 = 365
            temp = {'tr_del_avg': key, 'del_avg': key1, 'romal':key2,'impact_C': impact_C, 'days_Q': days_Q, 'days_H': days_H,
                    'days_C': days_C, 'impact_QL2': impact_QL2, 'days_QL2': days_QL2, 'Efa_QL2': Efa_QL2,
                    'impact_Q': impact_Q, 'impact_H': impact_H, 'Efa_Q': Efa_Q, 'Efa_C': Efa_C, 'Efa_H': Efa_H}
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

result_frame['tr_del_avg']= pd.to_numeric(result_frame['tr_del_avg'])
result_frame['del_avg']= pd.to_numeric(result_frame['del_avg'])
result_frame['romal']= pd.to_numeric(result_frame['romal'])

impact= result_frame[( result_frame['tr_del_avg'] == 175 )&
                        ( result_frame['del_avg'] == 190)
                        &( result_frame['romal'] >0.30)]#
impact_FIX_TR_DEL = result_frame[( result_frame['del_avg'] == 180 )  ]
# impact_FIX_TR_DEL = result_frame[( result_frame['tr_del_avg'] == 100 )  ]
# impact_FIX_TE_DEL = result_frame[( result_frame['del_avg'] == 190)  ]
# impact_FIX_ROMAL = result_frame[( result_frame['romal'] == 0.20 ) ]

# temp_df = impact[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]

f_C = open('../../test_C/result_data/impact/impact_poisoned_ro_del_nonQ_CRA.json')
f_H = open('../../test_H/result/impact/impact_poisoned_ro_del_nonQ_HRA.json')
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        for key2 in impact_dict_C[key][key1].keys():
            Efa_C = impact_dict_C[key][key1][key2]['0.006']['Efa']
            Efa_H = impact_dict_H[key][key1][key2]['0.006']['Efa']
            impact_C = impact_dict_C[key][key1][key2]['0.006']['impact']
            impact_H = impact_dict_H[key][key1][key2]['0.006']['impact']
            days_H = impact_dict_H[key][key1][key2]['0.006']['days_undetected']
            days_C = impact_dict_C[key][key1][key2]['0.006']['days_undetected']
            if (Efa_H > 365): Efa_H = 365
            if (Efa_C > 365): Efa_C = 365
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

result_frame['tr_del_avg']= pd.to_numeric(result_frame['tr_del_avg'])
result_frame['del_avg']= pd.to_numeric(result_frame['del_avg'])
result_frame['romal']= pd.to_numeric(result_frame['romal'])
impact_nQ= result_frame[( result_frame['tr_del_avg'] == 175 )&
                        ( result_frame['del_avg'] == 190)
                        &( result_frame['romal'] > 0.30)]#
impact_nQ_FIX_TR_DEL = result_frame[( result_frame['del_avg'] == 180 )  ]
# impact_nQ_FIX_TR_DEL = result_frame[( result_frame['tr_del_avg'] == 100 )  ]
# impact_nQ_FIX_TE_DEL = result_frame[( result_frame['del_avg'] == 190)  ]
# impact_nQ_FIX_ROMAL = result_frame[( result_frame['romal'] == 0.20 ) ]
# temp_df = impact_nQ[['del_avg','Efa_Q','Efa_H','Efa_C','impact_Q','impact_H','impact_C']]
#region tesitng del avg varies
# plt.ylim(5,150)
# fig = plt.subplots(figsize=(12, 6))
# plt.plot(impact_nQ['romal'],impact_nQ['impact_H'],marker ='>',color = 'r',label = 'NQH')
# plt.plot(impact_nQ['romal'],impact_nQ['impact_C'],marker ='^',color = 'tab:orange',label = 'NQC',linestyle =':')
plt.plot(impact['romal'],impact['impact_Q'],marker ='<',color = 'b',label ="QL1",linestyle ='--')
plt.plot(impact['romal'],impact['impact_QL2'],marker ='D',color = 'tab:olive',label ="QL2",linestyle ='-.')
plt.plot(impact['romal'],impact['impact_H'],marker ='>',color = 'r',label = 'QH',linestyle =':')
plt.plot(impact['romal'],impact['impact_C'],marker ='^',color = 'g',label = 'QC',linestyle ='--',dashes=(5, 5))
plt.xlabel(r'$\rho_{mal}^{(P)}$')
# plt.xticks( rotation=90 )
plt.ylabel("Impact")
# plt.xlim(0,170)
# loc = matplotlib.ticker.LinearLocator(numticks=5)
# plt.gca().xaxis.set_major_locator(loc)
plt.legend()

plt.show()
#endregion
# print(impact)
# print(impact_nQ)
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
impact_nQ_FIX_TR_DEL['impact_H'] = pd.to_numeric(impact_nQ_FIX_TR_DEL['impact_H'])
impact_nQ_FIX_TR_DEL['impact_C'] = pd.to_numeric(impact_nQ_FIX_TR_DEL['impact_C'])
impact_FIX_TR_DEL['impact_C'] = pd.to_numeric(impact_FIX_TR_DEL['impact_C'])
p = ax.plot_trisurf(impact_FIX_TR_DEL['tr_del_avg'],
               impact_FIX_TR_DEL['romal'],
               impact_FIX_TR_DEL['impact_C'],label ='QC',color='tab:olive') #alpha=0.5,
# # ax = fig.add_subplot(122, projection='3d')
# r = ax.plot_trisurf(impact_nQ_FIX_TR_DEL['tr_del_avg'],
#                impact_nQ_FIX_TR_DEL['romal'],
#                impact_nQ_FIX_TR_DEL['impact_H'], #alpha=0.5,
#                     label ='NQH',color='red')
# # ax = fig.add_subplot(123, projection='3d')
#
q= ax.plot_trisurf(impact_nQ_FIX_TR_DEL['tr_del_avg'],
               impact_nQ_FIX_TR_DEL['romal'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
               impact_nQ_FIX_TR_DEL['impact_C'],label='NQC',color='tab:blue')#alpha=0.5,
p._facecolors2d = p._facecolor3d
p._edgecolors2d = p._edgecolor3d

q._facecolors2d = q._facecolor3d
q._edgecolors2d = q._edgecolor3d
#
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
ax.set_xlabel('$\delta_{avg}^{(p)}$',labelpad=10)
ax.set_ylabel(r'$\rho_{mal}^{(p)}$',labelpad=10)
ax.set_zlabel('Impact',labelpad=10)
ax.set_xlim3d(min(impact_nQ_FIX_TR_DEL['tr_del_avg']),max(impact_nQ_FIX_TR_DEL['tr_del_avg']))
ax.set_ylim3d(min(impact_nQ_FIX_TR_DEL['romal']),max(impact_nQ_FIX_TR_DEL['romal']))
ax.set_zlim3d(min(impact_nQ_FIX_TR_DEL['impact_C']),300)
ax.xaxis.set_major_locator(plt.MaxNLocator(2))
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# ax.zaxis.set_major_locator(plt.MaxNLocator(3))
ax.view_init(elev=20, azim=-30.)
# fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
plt.legend()
plt.show()
#small size of trainign poisoning has best outcome