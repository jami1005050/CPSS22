#region Import and Global Variable
import matplotlib.ticker
import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib
#impact_x m4m6 impact_y m7m9 impact m10m12
SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #

impact_l1_ded = pd.read_csv('impact_SA_l1_ded_M4M12_Frame.csv')
impact_l2_ded = pd.read_csv('impact_SA_l2_ded_M4M12_Frame.csv')
impact_Q_C_ded = pd.read_csv('impact_SA_QC_ded_M4M12_Frame.csv')
impact_NQ_C_ded = pd.read_csv('impact_SA_NQC_ded_M4M12_Frame.csv')
impact_Q_H_ded = pd.read_csv('impact_SA_QH_ded_M4M12_Frame.csv')
impact_NQ_H_ded = pd.read_csv('impact_SA_NQH_ded_M4M12_Frame.csv')

impact_l1_ded['impact_m'] = impact_l1_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_l2_ded['impact_m']= impact_l2_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_C_ded['impact_m'] = impact_Q_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_C_ded['impact_m'] = impact_NQ_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_H_ded['impact_m'] = impact_Q_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_H_ded['impact_m'] = impact_NQ_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)

impact_l1_ded['efa_m'] = impact_l1_ded[['efa_x', 'efa_y','efa']].mean(axis=1)
impact_l2_ded['efa_m']=  impact_l2_ded[['efa_x', 'efa_y','efa']].mean(axis=1)
impact_Q_C_ded['efa_m'] = impact_Q_C_ded[['efa_x', 'efa_y','efa']].mean(axis=1)
impact_NQ_C_ded['efa_m'] = impact_NQ_C_ded[['efa_x', 'efa_y','efa']].mean(axis=1)
impact_Q_H_ded['efa_m'] = impact_Q_H_ded[['efa_x', 'efa_y','efa']].mean(axis=1)
impact_NQ_H_ded['efa_m'] = impact_NQ_H_ded[['efa_x', 'efa_y','efa']].mean(axis=1)

m_efa_l1 = impact_l1_ded[impact_l1_ded['ro_max']==6]['efa_m'].mean()
m_efa_l2 = impact_l2_ded[impact_l2_ded['ro_max']==6]['efa_m'].mean()
m_efa_QC = impact_Q_C_ded[impact_Q_C_ded['ro_max']==6]['efa_m'].mean()
m_efa_NQC = impact_NQ_C_ded[impact_NQ_C_ded['ro_max']==6]['efa_m'].mean()
m_efa_QH = impact_Q_H_ded[impact_Q_H_ded['ro_max']==6]['efa_m'].mean()
m_efa_NQH = impact_NQ_H_ded[impact_NQ_H_ded['ro_max']==6]['efa_m'].mean()
print('m_efa_l1: ',m_efa_l1,' m_efa_l2: ',m_efa_l2,' m_efa_QC: ',m_efa_QC,' m_efa_NQC: ',m_efa_NQC,' m_efa_QH: ',m_efa_QH,' m_efa_NQH: ',m_efa_NQH)
#endregion
#region 3D Plot
# impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 32 )&
#                                   ( impact_Q_C_ded['ro_mal'] == 0.40)]
# impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 32 )&
#                                    ( impact_NQ_C_ded['ro_mal'] == 0.40)]
#
# print(len(impactNQCded_VDTE),' ',len(impactQCded_VDTE))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# p = ax.plot_trisurf(impactQCded_VDTE['del_avg_te'],
#                impactQCded_VDTE['epsilon'],
#                impactQCded_VDTE['impact_m'],label ='QC',color='tab:olive', alpha = 1.0) #alpha=0.5,
#
# q= ax.plot_trisurf(impactNQCded_VDTE['del_avg_te'],
#                impactNQCded_VDTE['epsilon'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
#                impactNQCded_VDTE['impact_m'],label='NQC',color='tab:blue', alpha = 1.0)#alpha=0.5,
# p._facecolors2d = p._facecolor3d
# p._edgecolors2d = p._edgecolor3d
#
# q._facecolors2d = q._facecolor3d
# q._edgecolors2d = q._edgecolor3d
# ax.set_xlabel('$\delta_{avg}^{(p)}$',labelpad=10)
# ax.set_ylabel(r'$\rho_{mal}^{(p)}$',labelpad=10)
# ax.set_zlabel('Impact',labelpad=10)
# # ax.set_xlim3d(min(impactNQCded_VDTE['del_avg_te']),max(impactNQCded_VDTE['del_avg_te']))
# # ax.set_ylim3d(min(impactNQCded_VDTE['ro_mal']),max(impactNQCded_VDTE['ro_mal']))
# # ax.set_zlim3d(min(impactNQCded_VDTE['impact_m']),1700)
# ax.xaxis.set_major_locator(plt.MaxNLocator(2))
# ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# # ax.zaxis.set_major_locator(plt.MaxNLocator(3))
# ax.view_init(elev= 20, azim=-30.)
# # fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
# plt.legend()
# plt.show()


# print(impact_NQ_C_ded[impact_NQ_C_ded['impact_m'] >impact_NQ_H_ded['impact_m']])
#endregion
#region Large Scale Attack
#region LS Evasion Plot
impactl1ded_VDTE = impact_l1_ded[( impact_l1_ded['ro_max'] == 32 )&
                                 (impact_l1_ded['epsilon'] == 0.00035)&
                                 ( impact_l1_ded['ro_mal'] == 0.40)&
                                 (impact_l1_ded['del_avg_te'] <120)]#
impactl2ded_VDTE = impact_l2_ded[( impact_l2_ded['ro_max'] == 32)&
                                 (impact_l2_ded['epsilon'] == 0.00035)&
                                 ( impact_l2_ded['ro_mal'] == 0.40)&
                                 (impact_l2_ded['del_avg_te'] <120)]
impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 32 )&
                                  (impact_Q_C_ded['epsilon'] == 0.00060)&
                                  ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                  (impact_Q_C_ded['del_avg_te'] <120)]
impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 32 )&
                                   (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.30)&
                                   (impact_NQ_C_ded['del_avg_te'] <120)]
impactQHded_VDTE = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 32)&
                                  (impact_Q_H_ded['epsilon'] == 0.00035)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.40)&
                                  (impact_Q_H_ded['del_avg_te'] <120)]
impactNQHded_VDTE = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 32) &
                                    (impact_NQ_H_ded['epsilon'] == 0.00060)&
                                    (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                    (impact_NQ_H_ded['del_avg_te'] <120)
                                    ]

# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_max'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_mal'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['ro_max']>=20)&(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['epsilon'].value_counts()) #['epsilon'].unique().tolist()
# #
# # plt.plot(impactl1ded_VDTE['del_avg_te'],impactl1ded_VDTE['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# # plt.plot(impactl2ded_VDTE['del_avg_te'],impactl2ded_VDTE['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VDTE['del_avg_te'],impactQCded_VDTE['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VDTE['del_avg_te'],impactNQCded_VDTE['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# # plt.plot(impactQHded_VDTE['del_avg_te'],impactQHded_VDTE['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# # plt.plot(impactNQHded_VDTE['del_avg_te'],impactNQHded_VDTE['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Evasion Strength($\delta_{avg}^{(te)}$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#endregion
#region LS Impact Bar Plot

impactl1ded_VDTE = impact_l1_ded[( impact_l1_ded['ro_max'] == 24 )&
                                 (impact_l1_ded['epsilon'] == 0.0001)&
                                 ( impact_l1_ded['ro_mal'] == 0.30)&
                                 (impact_l1_ded['del_avg_te'] ==60)]['impact_m'].tolist()#
impactl2ded_VDTE = impact_l2_ded[( impact_l2_ded['ro_max'] == 24)&
                                 (impact_l2_ded['epsilon'] == 0.0001)&
                                 ( impact_l2_ded['ro_mal'] == 0.30)&
                                 (impact_l2_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 24 )&
                                  (impact_Q_C_ded['epsilon'] == 0.0001)&
                                  ( impact_Q_C_ded['ro_mal'] == 0.30)&
                                  (impact_Q_C_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 32 )&
                                   (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.30)&
                                   (impact_NQ_C_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactQHded_VDTE = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 24)&
                                  (impact_Q_H_ded['epsilon'] == 0.0001)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.30)&
                                  (impact_Q_H_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactNQHded_VDTE = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 32) &
                                    (impact_NQ_H_ded['epsilon'] == 0.00060)&
                                    (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                    (impact_NQ_H_ded['del_avg_te'] ==60)
                                    ]['impact_m'].tolist()
# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VDTE[0],impactl2ded_VDTE[0],impactQCded_VDTE[0],impactQHded_VDTE[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])

# plt.bar(["NQC","NQH"],
#         [impactNQCded_VDTE[0],impactNQHded_VDTE[0]],
#         color=['tab:green','tab:olive'])

# plt.bar(["QC","NQC"],
#         [impactQCded_VDTE[0],impactNQCded_VDTE[0]],
#         color=[ 'cyan','tab:green'])
# plt.ylabel('Impact(USD)')
# plt.ylim(50,70)
# plt.legend()
# plt.show()



#endregion
#region LS Varying Epsilon Plot

impactl1ded_VEPS_LS = impact_l1_ded[( impact_l1_ded['ro_max'] == 32 )&
                                 ( impact_l1_ded['ro_mal'] == 0.40)&
                                 (impact_l1_ded['del_avg_te'] ==60)]#
impactl2ded_VEPS_LS = impact_l2_ded[( impact_l2_ded['ro_max'] == 32)&
                                 ( impact_l2_ded['ro_mal'] == 0.40)&
                                 (impact_l2_ded['del_avg_te'] ==60)]
impactQCded_VEPS_LS = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 40 )&
                                  ( impact_Q_C_ded['ro_mal'] == 0.20)&
                                  (impact_Q_C_ded['del_avg_te'] ==20)&
                                       (impact_NQ_H_ded['epsilon'] <=.005)]
impactNQCded_VEPS_LS= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 40 )&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.20)&
                                   (impact_NQ_C_ded['del_avg_te'] ==20)&
                                       (impact_NQ_H_ded['epsilon'] <=.005)]
impactQHded_VEPS_LS = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 32)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.40)&
                                  (impact_Q_H_ded['del_avg_te'] ==60)]
impactNQHded_VEPS_LS = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 28) &
                                    (impact_NQ_H_ded['ro_mal'] == 0.20)&
                                    (impact_NQ_H_ded['del_avg_te'] ==20)&
                                       (impact_NQ_H_ded['epsilon'] <=.005)]

# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_max'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_mal'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['epsilon'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['ro_max']>=20)&(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])][['ro_max','ro_mal','del_avg_te']].value_counts()) #['epsilon'].unique().tolist()
# #
# plt.plot(impactl1ded_VEPS_LS['epsilon'],impactl1ded_VEPS_LS['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o',markevery = 5)
# plt.plot(impactl2ded_VEPS_LS['epsilon'],impactl2ded_VEPS_LS['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<',markevery = 5)
# plt.plot(impactQCded_VEPS_LS['epsilon'],impactQCded_VEPS_LS['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VEPS_LS['epsilon'],impactNQCded_VEPS_LS['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# plt.plot(impactQHded_VEPS_LS['epsilon'],impactQHded_VEPS_LS['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v',markevery = 5)
# plt.plot(impactNQHded_VEPS_LS['epsilon'],impactNQHded_VEPS_LS['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Poisoning Strength($\epsilon$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()

#endregion
#endregion

#region Medium Scale Attack
#region MS Evasion Plot
impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 10 )&
                                   (impact_l1_ded['epsilon'] == 0.00485)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] < 140)]#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 10)&
                                   (impact_l2_ded['epsilon'] == 0.00485)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] < 140)]
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 16 )&
                                   (impact_Q_C_ded['epsilon'] == 0.0036)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 16 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00485)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]#&( impact_NQ_C_ded['del_avg_te']< 140)]
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 10)&
                                    (impact_Q_H_ded['epsilon'] == 0.00485)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] < 140)]
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 16) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0036)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                      (( impact_NQ_H_ded['del_avg_te']< 140)&( impact_NQ_H_ded['del_avg_te']>=60))]

# plt.plot(impactl1ded_VROMAL['del_avg_te'],impactl1ded_VROMAL['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# plt.plot(impactl2ded_VROMAL['del_avg_te'],impactl2ded_VROMAL['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VROMAL['del_avg_te'],impactQCded_VROMAL['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VROMAL['del_avg_te'],impactNQCded_VROMAL['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# # plt.plot(impactQHded_VROMAL['del_avg_te'],impactQHded_VROMAL['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# # plt.plot(impactNQHded_VROMAL['del_avg_te'],impactNQHded_VROMAL['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Evasion Strength$\delta_{te}$')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#endregion
#region bar--plot MS

impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 10 )&
                                   (impact_l1_ded['epsilon'] == 0.00485)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] == 90)]['impact_m'].tolist()#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 10)&
                                   (impact_l2_ded['epsilon'] == 0.00485)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] == 90)]['impact_m'].tolist()
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 16 )&
                                   (impact_Q_C_ded['epsilon'] == 0.0036)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]['impact_m'].tolist()
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 16 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00485)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']==90))]['impact_m'].tolist()
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 10)&
                                    (impact_Q_H_ded['epsilon'] == 0.00485)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] == 90)]['impact_m'].tolist()
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 16) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0036)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                      (( impact_NQ_H_ded['del_avg_te']==90))]['impact_m'].tolist()

# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VROMAL[0],impactl2ded_VROMAL[0],impactQCded_VROMAL[0],impactQHded_VROMAL[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])

# plt.bar(["QC","NQC"],
#         [impactQCded_VROMAL[0],impactNQCded_VROMAL[0]],
#         color=[ 'cyan','tab:green'])
# plt.ylabel('Impact(USD)')
# # plt.ylim(80,160)
# # plt.legend()
# plt.show()


#endregion
#region MS Varying Epsilon Plot
impactl1ded_VEPS_MS = impact_l1_ded[( impact_l1_ded['ro_max'] == 10 )&
                                 ( impact_l1_ded['ro_mal'] == 0.30)&
                                 (impact_l1_ded['del_avg_te'] ==90)]#
impactl2ded_VEPS_MS = impact_l2_ded[( impact_l2_ded['ro_max'] == 10)&
                                 ( impact_l2_ded['ro_mal'] == 0.30)&
                                 (impact_l2_ded['del_avg_te'] ==90)]
impactQCded_VEPS_MS = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 16 )&
                                  ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                  (impact_Q_C_ded['del_avg_te'] ==80)]
impactNQCded_VEPS_MS= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 16 )&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.40)&
                                   (impact_NQ_C_ded['del_avg_te'] ==80)]
impactQHded_VEPS_MS = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 10)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.30)&
                                  (impact_Q_H_ded['del_avg_te'] ==90)]
impactNQHded_VEPS_MS = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 16) &
                                    (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                    (impact_NQ_H_ded['del_avg_te'] ==80)]

# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_max'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_mal'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['epsilon'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['ro_max']<=20)&(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])][['ro_max','ro_mal','del_avg_te']].value_counts()) #['epsilon'].unique().tolist()
# #
# plt.plot(impactl1ded_VEPS_MS['epsilon'],impactl1ded_VEPS_MS['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o',markevery = 5)
# plt.plot(impactl2ded_VEPS_MS['epsilon'],impactl2ded_VEPS_MS['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<',markevery = 5)
# plt.plot(impactQCded_VEPS_MS['epsilon'],impactQCded_VEPS_MS['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>',markevery = 5)
# plt.plot(impactNQCded_VEPS_MS['epsilon'],impactNQCded_VEPS_MS['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o',markevery = 5)
# plt.plot(impactQHded_VEPS_MS['epsilon'],impactQHded_VEPS_MS['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v',markevery = 5)
# plt.plot(impactNQHded_VEPS_MS['epsilon'],impactNQHded_VEPS_MS['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D',markevery = 5)
# plt.xlabel(r'Poisoning Strength($\epsilon$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#endregion
#endregion
#region Small Scale Attack
#region SS Evasion Plot
impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 4 )&
                                   (impact_l1_ded['epsilon'] == 0.0156)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] < 140)]#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 4)&
                                   (impact_l2_ded['epsilon'] == 0.0156)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] < 140)]
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 4 )&
                                   (impact_Q_C_ded['epsilon'] == 0.00060)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_Q_C_ded['del_avg_te']< 150)&( impact_Q_C_ded['del_avg_te']>60))]
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 4 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']< 150)&( impact_NQ_C_ded['del_avg_te']>60))]
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 4)&
                                    (impact_Q_H_ded['epsilon'] == 0.0156)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] < 140)]
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 4) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0156)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                      (impact_NQ_H_ded['del_avg_te'] < 140)]


#(impact_Q_C_ded['ro_max']==4)&

# plt.plot(impactl1ded_VROMAL['del_avg_te'],impactl1ded_VROMAL['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# plt.plot(impactl2ded_VROMAL['del_avg_te'],impactl2ded_VROMAL['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VROMAL['del_avg_te'],impactQCded_VROMAL['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VROMAL['del_avg_te'],impactNQCded_VROMAL['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# # plt.plot(impactQHded_VROMAL['del_avg_te'],impactQHded_VROMAL['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# # plt.plot(impactNQHded_VROMAL['del_avg_te'],impactNQHded_VROMAL['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Evasion Strength ($\delta_{te}$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#endregion
#region bar--plot SA
impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 4 )&
                                   (impact_l1_ded['epsilon'] == 0.0156)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] == 60)]['impact_m'].tolist()#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 4)&
                                   (impact_l2_ded['epsilon'] == 0.0156)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] == 60)]['impact_m'].tolist()
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 4 )&
                                   (impact_Q_C_ded['epsilon'] == 0.00060) &
                                   (impact_Q_C_ded['ro_mal'] == 0.30) &
                                   (impact_Q_C_ded['del_avg_te'] == 100)]['impact_m'].tolist()
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 4 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      ( impact_NQ_C_ded['del_avg_te']== 100)]['impact_m'].tolist()
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 4)&
                                    (impact_Q_H_ded['epsilon'] == 0.0156)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] == 60)]['impact_m'].tolist()
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 4) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0156)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                      (impact_NQ_H_ded['del_avg_te'] == 60)]['impact_m'].tolist()

# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VROMAL[0],impactl2ded_VROMAL[0],impactQCded_VROMAL[0],impactQHded_VROMAL[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])
#
# plt.bar(["QC","NQC"],
#         [impactQCded_VROMAL[0],impactNQCded_VROMAL[0]],
#         color=['cyan', 'tab:green'])#'tab:olive'
# plt.ylabel('Impact(USD)')
# plt.ylim(90,115)
# # plt.legend()
# plt.show()

#endregion
#region SS Varying Epsilon Plot

impactl1ded_VEPS_MS = impact_l1_ded[( impact_l1_ded['ro_max'] == 4 )&
                                 ( impact_l1_ded['ro_mal'] == 0.30)&
                                 (impact_l1_ded['del_avg_te'] ==60)]#
impactl2ded_VEPS_MS = impact_l2_ded[( impact_l2_ded['ro_max'] == 4)&
                                 ( impact_l2_ded['ro_mal'] == 0.30)&
                                 (impact_l2_ded['del_avg_te'] ==60)]
impactQCded_VEPS_MS = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 4 )&
                                  ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                  (impact_Q_C_ded['del_avg_te'] ==70)&
                                  (impact_Q_C_ded['epsilon'] <0.005)]
impactNQCded_VEPS_MS= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 4 )&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.30)&
                                   (impact_NQ_C_ded['del_avg_te'] ==80)&
                                    (impact_NQ_H_ded['epsilon'] <0.006)]
impactQHded_VEPS_MS = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 4)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.30)&
                                  (impact_Q_H_ded['del_avg_te'] ==60)]
impactNQHded_VEPS_MS = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 4) &
                                    (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                    (impact_NQ_H_ded['del_avg_te'] ==80)&
                                    (impact_NQ_H_ded['epsilon'] <0.006)]

# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_NQ_H_ded['impact_m'])]['ro_max'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_NQ_H_ded['impact_m'])]['ro_mal'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_NQ_H_ded['impact_m'])]['epsilon'].unique().tolist())
# print(impact_NQ_C_ded[(impact_NQ_C_ded['ro_max']<10)&(impact_NQ_C_ded['impact_m'] < impact_NQ_H_ded['impact_m'])][['ro_max','ro_mal','del_avg_te']].value_counts()) #['epsilon'].unique().tolist()
# #
# plt.plot(impactl1ded_VEPS_MS['epsilon'],impactl1ded_VEPS_MS['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o',markevery = 5)
# plt.plot(impactl2ded_VEPS_MS['epsilon'],impactl2ded_VEPS_MS['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<',markevery = 5)
# plt.plot(impactQCded_VEPS_MS['epsilon'],impactQCded_VEPS_MS['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VEPS_MS['epsilon'],impactNQCded_VEPS_MS['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# plt.plot(impactQHded_VEPS_MS['epsilon'],impactQHded_VEPS_MS['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v',markevery = 5)
# plt.plot(impactNQHded_VEPS_MS['epsilon'],impactNQHded_VEPS_MS['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Poisoning Strength($\epsilon$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#endregion
#endregion