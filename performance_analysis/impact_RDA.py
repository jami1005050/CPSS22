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

impact_l1_ded = pd.read_csv('../test_QP/impact_test/impact_RA_L1_ded.csv')
impact_l2_ded = pd.read_csv('../test_QP/impact_test/impact_RA_L2_ded.csv')
impact_Q_C_ded = pd.read_csv('../test_C/impact_test/impact_RA_Q_C_ded.csv')
impact_NQ_C_ded = pd.read_csv('../test_C/impact_test/impact_RA_NQ_C_ded.csv')
impact_Q_H_ded = pd.read_csv('../test_H/impact_test/impact_RA_Q_H_ded.csv')
impact_NQ_H_ded = pd.read_csv('../test_H/impact_test/impact_RA_NQ_H_ded.csv')
avg_l1 = impact_l1_ded['impact'].mean()
avg_l2 = impact_l2_ded['impact'].mean()
avg_QC = impact_Q_C_ded['impact'].mean()
avg_NQC = impact_NQ_C_ded['impact'].mean()
avg_QH = impact_Q_H_ded['impact'].mean()
avg_NQH = impact_NQ_H_ded['impact'].mean()
print(avg_l1,' ',avg_l2,' ',avg_QC,' ',avg_NQC,' ',avg_QH,' ',avg_NQH)

impactl1ded_VTRD = impact_l1_ded[( impact_l1_ded['del_avg_tr'] == 250 )&
                        ( impact_l1_ded['del_avg_te'] == 175)]
impactl2ded_VTRD = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 250) &
                            (impact_l2_ded['del_avg_te'] == 175)]
impactQCded_VTRD = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 250) &
                             (impact_Q_C_ded['del_avg_te'] == 175)]
impactNQCded_VTRD = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 250) &
                               (impact_NQ_C_ded['del_avg_te'] == 175)]
impactQHded_VTRD = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 250) &
                             (impact_Q_H_ded['del_avg_te'] == 175)]
impactNQHded_VTRD = impact_NQ_H_ded[( impact_NQ_H_ded['del_avg_tr'] == 250 )&
                        ( impact_NQ_H_ded['del_avg_te'] == 175)]

plt.plot(impactl1ded_VTRD['ro_mal'],impactl1ded_VTRD['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VTRD['ro_mal'],impactl2ded_VTRD['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VTRD['ro_mal'],impactQCded_VTRD['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VTRD['ro_mal'],impactNQCded_VTRD['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VTRD['ro_mal'],impactQHded_VTRD['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VTRD['ro_mal'],impactNQHded_VTRD['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\rho_{mal}$')
plt.ylabel('Impact')
plt.legend()
plt.show()

impactl1ded_VTED = impact_l1_ded[( impact_l1_ded['del_avg_te'] == 100 )&
                        ( impact_l1_ded['ro_mal'] == 0.30)]
impactl2ded_VTED = impact_l2_ded[(impact_l2_ded['del_avg_te'] == 100) &
                            (impact_l2_ded['ro_mal'] == 0.30)]
impactQCded_VTED = impact_Q_C_ded[(impact_Q_C_ded['del_avg_te'] == 100) &
                             (impact_Q_C_ded['ro_mal'] == 0.30)]
impactNQCded_VTED = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_te'] == 100) &
                               (impact_NQ_C_ded['ro_mal'] == 0.30)]
impactQHded_VTED = impact_Q_H_ded[(impact_Q_H_ded['del_avg_te'] == 100) &
                             (impact_Q_H_ded['ro_mal'] == 0.30)]
impactNQHded_VTED = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_te'] == 100) &
                               (impact_NQ_H_ded['ro_mal'] == 0.30)]


plt.plot(impactl1ded_VTED['del_avg_tr'],impactl1ded_VTED['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VTED['del_avg_tr'],impactl2ded_VTED['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VTED['del_avg_tr'],impactQCded_VTED['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VTED['del_avg_tr'],impactNQCded_VTED['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VTED['del_avg_tr'],impactQHded_VTED['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VTED['del_avg_tr'],impactNQHded_VTED['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\delta_{avg}^{(p)}$')
plt.ylabel('Impact')
plt.legend()
plt.show()


impactl1ded_Fix_RO_MAX = impact_l1_ded[(impact_NQ_C_ded['del_avg_tr'] == 130) &
                        ( impact_l1_ded['ro_mal'] == 0.30)]#
impactl2ded_Fix_RO_MAX = impact_l2_ded[(impact_NQ_C_ded['del_avg_tr'] == 130) &
                        ( impact_l2_ded['ro_mal'] == 0.30)]
impactQCded_Fix_RO_MAX = impact_Q_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 130) &
                        ( impact_Q_C_ded['ro_mal'] == 0.30)]
impactNQCded_Fix_RO_MAX = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 130) &
                        ( impact_NQ_C_ded['ro_mal'] == 0.30)]
impactQHded_Fix_RO_MAX = impact_Q_H_ded[(impact_NQ_C_ded['del_avg_tr'] == 130) &
                        ( impact_Q_H_ded['ro_mal'] == 0.30)]
impactNQHded_Fix_RO_MAX = impact_NQ_H_ded[(impact_NQ_C_ded['del_avg_tr'] == 175) &
                               (impact_NQ_H_ded['ro_mal'] == 0.30)]

plt.plot(impactl1ded_Fix_RO_MAX['del_avg_te'],impactl1ded_Fix_RO_MAX['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_Fix_RO_MAX['del_avg_te'],impactl2ded_Fix_RO_MAX['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_Fix_RO_MAX['del_avg_te'],impactQCded_Fix_RO_MAX['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_Fix_RO_MAX['del_avg_te'],impactNQCded_Fix_RO_MAX['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_Fix_RO_MAX['del_avg_te'],impactQHded_Fix_RO_MAX['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_Fix_RO_MAX['del_avg_te'],impactNQHded_Fix_RO_MAX['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\delta_{avg}^{(te)}$')
plt.ylabel('Impact')
plt.legend()
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# p = ax.plot_trisurf(impactQHded_Fix_RO_MAX['del_avg_tr'],
#                impactQHded_Fix_RO_MAX['del_avg_te'],
#                impactQHded_Fix_RO_MAX['impact'],label ='QH',color='tab:olive') #alpha=0.5,
#
# q= ax.plot_trisurf(impactQCded_Fix_RO_MAX['del_avg_tr'],
#                impactQCded_Fix_RO_MAX['del_avg_te'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
#                impactQCded_Fix_RO_MAX['impact'],label='QC',color='tab:blue')#alpha=0.5,
# p._facecolors2d = p._facecolor3d
# p._edgecolors2d = p._edgecolor3d
#
# q._facecolors2d = q._facecolor3d
# q._edgecolors2d = q._edgecolor3d
# ax.set_xlabel('$\delta_{avg}^{(p)}$',labelpad=10)
# ax.set_ylabel(r'$\rho_{mal}^{(p)}$',labelpad=10)
# ax.set_zlabel('Impact',labelpad=10)
# # ax.set_xlim3d(min(impact_nQ_FIX_TR_DEL['tr_del_avg']),max(impact_nQ_FIX_TR_DEL['tr_del_avg']))
# # ax.set_ylim3d(min(impact_nQ_FIX_TR_DEL['romal']),max(impact_nQ_FIX_TR_DEL['romal']))
# # ax.set_zlim3d(min(impact_nQ_FIX_TR_DEL['impact_C']),300)
# # ax.xaxis.set_major_locator(plt.MaxNLocator(2))
# # ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# # ax.zaxis.set_major_locator(plt.MaxNLocator(3))
# ax.view_init(elev=20, azim=-20.)
# # fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
# plt.legend()
# plt.show()
#
# # print((impactNQHded))
