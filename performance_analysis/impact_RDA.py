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

impact_l1_ded = pd.read_csv('impact_RA_l1_ded_M4M12_Frame.csv')
impact_l2_ded = pd.read_csv('impact_RA_l2_ded_M4M12_Frame.csv')
impact_Q_C_ded = pd.read_csv('impact_RA_QC_ded_M4M12_Frame.csv')
impact_NQ_C_ded = pd.read_csv('impact_RA_NQC_ded_M4M12_Frame.csv')
impact_Q_H_ded = pd.read_csv('impact_RA_QH_ded_M4M12_Frame.csv')
impact_NQ_H_ded = pd.read_csv('impact_RA_NQH_ded_M4M12_Frame.csv')

impact_l1_ded['impact_m'] = impact_l1_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_l2_ded['impact_m']= impact_l2_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_C_ded['impact_m'] = impact_Q_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_C_ded['impact_m'] = impact_NQ_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_H_ded['impact_m'] = impact_Q_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_H_ded['impact_m'] = impact_NQ_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)

#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# p = ax.plot_trisurf(impact_Q_C_ded['del_avg_tr'],
#                impact_Q_C_ded['ro_mal'],
#                impact_Q_C_ded['impact'],label ='QC',color='tab:olive') #alpha=0.5,
#
# q= ax.plot_trisurf(impact_NQ_C_ded['del_avg_tr'],
#                impact_NQ_C_ded['ro_mal'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
#                impact_NQ_C_ded['impact'],label='NQC',color='tab:blue')#alpha=0.5,
# p._facecolors2d = p._facecolor3d
# p._edgecolors2d = p._edgecolor3d
#
# q._facecolors2d = q._facecolor3d
# q._edgecolors2d = q._edgecolor3d
# ax.set_xlabel('$\delta_{avg}^{(p)}$',labelpad=10)
# ax.set_ylabel(r'$\rho_{mal}^{(p)}$',labelpad=10)
# ax.set_zlabel('Impact',labelpad=10)
# ax.set_xlim3d(min(impact_NQ_C_ded['del_avg_tr']),max(impact_NQ_C_ded['del_avg_tr']))
# ax.set_ylim3d(min(impact_NQ_C_ded['ro_mal']),max(impact_NQ_C_ded['ro_mal']))
# ax.set_zlim3d(min(impact_NQ_C_ded['impact']),1700)
# ax.xaxis.set_major_locator(plt.MaxNLocator(2))
# ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# # ax.zaxis.set_major_locator(plt.MaxNLocator(3))
# ax.view_init(elev=20, azim=130.)
# # fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
# plt.legend()
# plt.show()

# impactl1ded_VTRD = impact_l1_ded[( impact_l1_ded['del_avg_tr'] == 100 )&
#                                  ( impact_l1_ded['del_avg_te'] == 120)&
#                                  (( impact_l1_ded['ro_mal'] > 0.20)& ( impact_l1_ded['ro_mal'] < 0.70))]
# impactl2ded_VTRD = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 100) &
#                                  (impact_l2_ded['del_avg_te'] == 120)&
#                                  (( impact_l2_ded['ro_mal'] > 0.20)& ( impact_l2_ded['ro_mal'] < 0.70))]
# impactQCded_VTRD = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 100) &
#                                   (impact_Q_C_ded['del_avg_te'] == 120)&
#                                   (( impact_Q_C_ded['ro_mal'] > 0.20)& ( impact_Q_C_ded['ro_mal'] < 0.70))]
# impactNQCded_VTRD = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 100) &
#                                     (impact_NQ_C_ded['del_avg_te'] == 120)&
#                                     (( impact_NQ_C_ded['ro_mal'] > 0.20)& ( impact_NQ_C_ded['ro_mal'] < 0.70))]
# impactQHded_VTRD = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 100) &
#                                   (impact_Q_H_ded['del_avg_te'] == 120)&
#                                   (( impact_Q_H_ded['ro_mal'] > 0.20)& ( impact_Q_H_ded['ro_mal'] < 0.70))]
# impactNQHded_VTRD = impact_NQ_H_ded[( impact_NQ_H_ded['del_avg_tr'] == 100 )&
#                                     ( impact_NQ_H_ded['del_avg_te'] == 120)&
#                                     (( impact_NQ_H_ded['ro_mal'] > 0.20)& ( impact_NQ_H_ded['ro_mal'] < 0.70))]

# plt.plot(impactl1ded_VTRD['ro_mal'],impactl1ded_VTRD['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker ='o')
# plt.plot(impactl2ded_VTRD['ro_mal'],impactl2ded_VTRD['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VTRD['ro_mal'],impactQCded_VTRD['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker ='<')
# plt.plot(impactNQCded_VTRD['ro_mal'],impactNQCded_VTRD['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker ='o')
# plt.plot(impactQHded_VTRD['ro_mal'],impactQHded_VTRD['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker='v')
# plt.plot(impactNQHded_VTRD['ro_mal'],impactNQHded_VTRD['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker ='D')
# plt.xlabel(r'$\rho^{mal}$')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()

impactl1ded_VTED = impact_l1_ded[( impact_l1_ded['del_avg_te'] == 100 )&
                                 ( impact_l1_ded['ro_mal'] == 0.60)&
                                 ((impact_l1_ded['del_avg_tr'] <= 200)&(impact_l1_ded['del_avg_tr'] > 50)) ]
impactl2ded_VTED = impact_l2_ded[(impact_l2_ded['del_avg_te'] == 100) &
                                 (impact_l2_ded['ro_mal'] == 0.60)&
                                 ((impact_l2_ded['del_avg_tr'] <= 200)&(impact_l2_ded['del_avg_tr'] > 50) )]
impactQCded_VTED = impact_Q_C_ded[(impact_Q_C_ded['del_avg_te'] == 100) &
                                  (impact_Q_C_ded['ro_mal'] == 0.60)&
                                  ((impact_Q_C_ded['del_avg_tr'] <= 200)&(impact_Q_C_ded['del_avg_tr'] > 50) )]
impactNQCded_VTED = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_te'] == 100) &
                                    (impact_NQ_C_ded['ro_mal'] == 0.60)&
                                    ((impact_NQ_C_ded['del_avg_tr'] <= 200)&(impact_NQ_C_ded['del_avg_tr']>50) )]
impactQHded_VTED = impact_Q_H_ded[(impact_Q_H_ded['del_avg_te'] == 100) &
                                  (impact_Q_H_ded['ro_mal'] == 0.60)&
                                  ((impact_Q_H_ded['del_avg_tr'] <= 200)& (impact_Q_H_ded['del_avg_tr'] > 50)) ]
impactNQHded_VTED = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_te'] == 100) &
                                    (impact_NQ_H_ded['ro_mal'] == 0.60)&
                                    ((impact_NQ_H_ded['del_avg_tr'] <= 200)&(impact_NQ_H_ded['del_avg_tr'] >50) )]

#
# plt.plot(impactl1ded_VTED['del_avg_tr'],impactl1ded_VTED['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker ='o')
# plt.plot(impactl2ded_VTED['del_avg_tr'],impactl2ded_VTED['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker ='<')
# plt.plot(impactQCded_VTED['del_avg_tr'],impactQCded_VTED['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker ='>')
# # plt.plot(impactNQCded_VTED['del_avg_tr'],impactNQCded_VTED['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker ='o')
# plt.plot(impactQHded_VTED['del_avg_tr'],impactQHded_VTED['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker ='v')
# # plt.plot(impactNQHded_VTED['del_avg_tr'],impactNQHded_VTED['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker ='D')
# plt.xlabel(r'Poisoning Strength($\delta_{avg}^{(p)}$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()


impactl1ded_Fix_RO_MAX = impact_l1_ded[(impact_l1_ded['del_avg_tr'] == 200) &
                                       ( impact_l1_ded['ro_mal'] == 0.50)&
                                       (impact_l1_ded['del_avg_te'] <=150)]#
impactl2ded_Fix_RO_MAX = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 200) &
                                       ( impact_l2_ded['ro_mal'] == 0.50)&
                                       (impact_l2_ded['del_avg_te'] <=150)]
impactQCded_Fix_RO_MAX = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 200) &
                                        ( impact_Q_C_ded['ro_mal'] == 0.50)&
                                        (impact_Q_C_ded['del_avg_te'] <=150)]
impactNQCded_Fix_RO_MAX = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 200) &
                                          ( impact_NQ_C_ded['ro_mal'] == 0.50)&
                                          (impact_NQ_C_ded['del_avg_te'] <=150)]
impactQHded_Fix_RO_MAX = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 200) &
                                        ( impact_Q_H_ded['ro_mal'] == 0.50)&
                                        (impact_Q_H_ded['del_avg_te'] <=150)]
impactNQHded_Fix_RO_MAX = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_tr'] == 200) &
                                          (impact_NQ_H_ded['ro_mal'] == 0.50)&
                                          (impact_NQ_H_ded['del_avg_te'] <=150) ]

plt.plot(impactl1ded_Fix_RO_MAX['del_avg_te'],impactl1ded_Fix_RO_MAX['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker ='o')
plt.plot(impactl2ded_Fix_RO_MAX['del_avg_te'],impactl2ded_Fix_RO_MAX['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker ='<')
plt.plot(impactQCded_Fix_RO_MAX['del_avg_te'],impactQCded_Fix_RO_MAX['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker ='>')
# plt.plot(impactNQCded_Fix_RO_MAX['del_avg_te'],impactNQCded_Fix_RO_MAX['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker ='o')
plt.plot(impactQHded_Fix_RO_MAX['del_avg_te'],impactQHded_Fix_RO_MAX['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker ='v')
# plt.plot(impactNQHded_Fix_RO_MAX['del_avg_te'],impactNQHded_Fix_RO_MAX['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
plt.xlabel(r'Evasion Strength($\delta_{avg}^{(te)}$)')
plt.ylabel('Impact(USD)')
plt.legend()
plt.show()


#region RA--BAR--PLOT

impactl1ded_Fix_RO_MAX = impact_l1_ded[(impact_l1_ded['del_avg_tr'] == 250) &
                                       ( impact_l1_ded['ro_mal'] == 0.40)&
                                       (impact_l1_ded['del_avg_te'] ==150)]['impact_m'].tolist()#
impactl2ded_Fix_RO_MAX = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 250) &
                                       ( impact_l2_ded['ro_mal'] == 0.40)&
                                       (impact_l2_ded['del_avg_te'] ==150)]['impact_m'].tolist()
impactQCded_Fix_RO_MAX = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 250) &
                                        ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                        (impact_Q_C_ded['del_avg_te'] ==150)]['impact_m'].tolist()
impactNQCded_Fix_RO_MAX = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 250) &
                                          ( impact_NQ_C_ded['ro_mal'] == 0.40)&
                                          (impact_NQ_C_ded['del_avg_te'] ==150)]['impact_m'].tolist()
impactQHded_Fix_RO_MAX = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 250) &
                                        ( impact_Q_H_ded['ro_mal'] == 0.40)&
                                        (impact_Q_H_ded['del_avg_te'] ==150)]['impact_m'].tolist()
impactNQHded_Fix_RO_MAX = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_tr'] == 250) &
                                          (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                          (impact_NQ_H_ded['del_avg_te'] ==150) ]['impact_m'].tolist()

# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_Fix_RO_MAX[0],impactl2ded_Fix_RO_MAX[0],impactQCded_Fix_RO_MAX[0],impactQHded_Fix_RO_MAX[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])

plt.bar(["QC","NQC"],
        [impactQCded_Fix_RO_MAX[0],impactNQCded_Fix_RO_MAX[0]],
        color=[ 'cyan','tab:green'])

# plt.bar(["NQC","NQH"],
#         [impactNQCded_Fix_RO_MAX[0],impactNQHded_Fix_RO_MAX[0]],
#         color=[ 'tab:green','tab:olive'])
plt.ylabel('Impact(USD)')
# plt.ylim(1200,2600)
# plt.legend()
plt.show()

#endregion