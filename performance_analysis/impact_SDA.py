import pandas as pd
import matplotlib.pyplot as plt

impact_l1_ded = pd.read_csv('../test_QP/impact_test/impact_SA_L1_ded.csv')
impact_l2_ded = pd.read_csv('../test_QP/impact_test/impact_SA_L2_ded.csv')
impact_Q_C_ded = pd.read_csv('../test_C/impact_test/impact_SA_Q_C_ded.csv')
impact_NQ_C_ded = pd.read_csv('../test_C/impact_test/impact_SA_NQ_C_ded.csv')
impact_Q_H_ded = pd.read_csv('../test_H/impact_test/impact_SA_Q_H_ded.csv')
impact_NQ_H_ded = pd.read_csv('../test_H/impact_test/impact_SA_NQ_H_ded.csv')
avg_l1 = impact_l1_ded['impact'].mean()
avg_l2 = impact_l2_ded['impact'].mean()
avg_QC = impact_Q_C_ded['impact'].mean()
avg_NQC = impact_NQ_C_ded['impact'].mean()
avg_QH = impact_Q_H_ded['impact'].mean()
avg_NQH = impact_NQ_H_ded['impact'].mean()
print(avg_l1,' ',avg_l2,' ',avg_QC,' ',avg_NQC,' ',avg_QH,' ',avg_NQH)
#In the plot the factors involved are following ro_max,del_avg_te, epsilon, ro_mal
#Ro_MAX 1:Large case 50 2:middle case 28 3:small case for 3D plot 10
#0.01385
impactl1ded_VEPS = impact_l1_ded[( impact_l1_ded['ro_max'] == 28 )&
                                       (impact_l1_ded['del_avg_te'] == 50)&
                                       ( impact_l1_ded['ro_mal'] == 0.30)]#
impactl2ded_VEPS = impact_l2_ded[( impact_l2_ded['ro_max'] == 28)&
                                       (impact_l2_ded['del_avg_te'] == 50)&
                                       ( impact_l2_ded['ro_mal'] == 0.30)]
impactQCded_VEPS = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 28 )&
                                        (impact_Q_C_ded['del_avg_te'] == 50)&
                                        ( impact_Q_C_ded['ro_mal'] == 0.30)]
impactNQCded_VEPS = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 28 )&
                                          (impact_NQ_C_ded['del_avg_te'] == 50)&
                                          ( impact_NQ_C_ded['ro_mal'] == 0.30)]
impactQHded_VEPS = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 28)&
                                        (impact_Q_H_ded['del_avg_te'] == 50)&
                                        ( impact_Q_H_ded['ro_mal'] == 0.30)]
impactNQHded_VEPS = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 28) &
                                          (impact_NQ_H_ded['del_avg_te'] == 50)&
                                          (impact_NQ_H_ded['ro_mal'] == 0.30)]


plt.plot(impactl1ded_VEPS['epsilon'],impactl1ded_VEPS['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VEPS['epsilon'],impactl2ded_VEPS['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VEPS['epsilon'],impactQCded_VEPS['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VEPS['epsilon'],impactNQCded_VEPS['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VEPS['epsilon'],impactQHded_VEPS['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VEPS['epsilon'],impactNQHded_VEPS['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\epsilon$')
plt.ylabel('Impact')
plt.legend()
plt.show()


#0.01385
impactl1ded_VDTE = impact_l1_ded[( impact_l1_ded['ro_max'] == 28 )&
                                       (impact_l1_ded['epsilon'] == 0.01385)&
                                       ( impact_l1_ded['ro_mal'] == 0.30)]#
impactl2ded_VDTE = impact_l2_ded[( impact_l2_ded['ro_max'] == 28)&
                                       (impact_l2_ded['epsilon'] == 0.01385)&
                                       ( impact_l2_ded['ro_mal'] == 0.30)]
impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 28 )&
                                        (impact_Q_C_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_C_ded['ro_mal'] == 0.30)]
impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 28 )&
                                          (impact_NQ_C_ded['epsilon'] == 0.01385)&
                                          ( impact_NQ_C_ded['ro_mal'] == 0.30)]
impactQHded_VDTE = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 28)&
                                        (impact_Q_H_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_H_ded['ro_mal'] == 0.30)]
impactNQHded_VDTE = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 28) &
                                          (impact_NQ_H_ded['epsilon'] == 0.01385)&
                                          (impact_NQ_H_ded['ro_mal'] == 0.30)]


plt.plot(impactl1ded_VDTE['del_avg_te'],impactl1ded_VDTE['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VDTE['del_avg_te'],impactl2ded_VDTE['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VDTE['del_avg_te'],impactQCded_VDTE['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VDTE['del_avg_te'],impactNQCded_VDTE['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VDTE['del_avg_te'],impactQHded_VDTE['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VDTE['del_avg_te'],impactNQHded_VDTE['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\delta_{avg}^{(te)}$')
plt.ylabel('Impact')
plt.legend()
plt.show()

impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 28 )&
                                       (impact_l1_ded['epsilon'] == 0.01385)&
                                       ( impact_l1_ded['del_avg_te'] == 130)]#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 28)&
                                       (impact_l2_ded['epsilon'] == 0.01385)&
                                       ( impact_l2_ded['del_avg_te'] == 130)]
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 28 )&
                                        (impact_Q_C_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_C_ded['del_avg_te'] == 130)]
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 28 )&
                                          (impact_NQ_C_ded['epsilon'] == 0.01385)&
                                          ( impact_NQ_C_ded['del_avg_te'] == 130)]
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 28)&
                                        (impact_Q_H_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_H_ded['del_avg_te'] == 130)]
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 28) &
                                          (impact_NQ_H_ded['epsilon'] == 0.01385)&
                                          (impact_NQ_H_ded['del_avg_te'] == 130)]


plt.plot(impactl1ded_VROMAL['ro_mal'],impactl1ded_VROMAL['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VROMAL['ro_mal'],impactl2ded_VROMAL['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VROMAL['ro_mal'],impactQCded_VROMAL['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VROMAL['ro_mal'],impactNQCded_VROMAL['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VROMAL['ro_mal'],impactQHded_VROMAL['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VROMAL['ro_mal'],impactNQHded_VROMAL['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel(r'$\rho_{mal}$')
plt.ylabel('Impact')
plt.legend()
plt.show()


impactl1ded_VROMAX = impact_l1_ded[( impact_l1_ded['del_avg_te'] == 130 )&
                                       (impact_l1_ded['epsilon'] == 0.01385)&
                                       ( impact_l1_ded['ro_mal'] == 0.30)]#
impactl2ded_VROMAX = impact_l2_ded[( impact_l2_ded['del_avg_te'] == 130)&
                                       (impact_l2_ded['epsilon'] == 0.01385)&
                                       ( impact_l2_ded['ro_mal'] == 0.30)]
impactQCded_VROMAX = impact_Q_C_ded[( impact_Q_C_ded['del_avg_te'] == 130 )&
                                        (impact_Q_C_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_C_ded['ro_mal'] == 0.30)]
impactNQCded_VROMAX = impact_NQ_C_ded[( impact_NQ_C_ded['del_avg_te'] == 130 )&
                                          (impact_NQ_C_ded['epsilon'] == 0.01385)&
                                          ( impact_NQ_C_ded['del_avg_te'] == 0.30)]
impactQHded_VROMAX = impact_Q_H_ded[( impact_Q_H_ded['del_avg_te'] == 130)&
                                        (impact_Q_H_ded['epsilon'] == 0.01385)&
                                        ( impact_Q_H_ded['ro_mal'] == 0.30)]
impactNQHded_VROMAX = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_te'] == 130) &
                                          (impact_NQ_H_ded['epsilon'] == 0.01385)&
                                          (impact_NQ_H_ded['ro_mal'] == 0.30)]


plt.plot(impactl1ded_VROMAX['ro_max'],impactl1ded_VROMAX['impact'],label = 'L1',linestyle = '--',dashes =(5,1))
plt.plot(impactl2ded_VROMAX['ro_max'],impactl2ded_VROMAX['impact'],label = 'L2',linestyle = ':',dashes =(5,1))
plt.plot(impactQCded_VROMAX['ro_max'],impactQCded_VROMAX['impact'],label = 'QC',linestyle = '-.',dashes =(5,1))
plt.plot(impactNQCded_VROMAX['ro_max'],impactNQCded_VROMAX['impact'],label = 'NQC',linestyle = '--',dashes =(10,1))
plt.plot(impactQHded_VROMAX['ro_max'],impactQHded_VROMAX['impact'],label = 'QH',linestyle = '--',dashes =(10,2))
plt.plot(impactNQHded_VROMAX['ro_max'],impactNQHded_VROMAX['impact'],label = 'NQH',linestyle = '--',dashes =(5,2))
plt.xlabel('Number of Perturb Points')
plt.ylabel('Impact')
plt.legend()
plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# p = ax.plot_trisurf(impactl1ded_Fix_RO_MAX['epsilon'],
#                impactl1ded_Fix_RO_MAX['del_avg_te'],
#                impactl1ded_Fix_RO_MAX['impact'],label ='QH',color='tab:olive') #alpha=0.5,
#
# q= ax.plot_trisurf(impactl2ded_Fix_RO_MAX['epsilon'],
#                impactl2ded_Fix_RO_MAX['del_avg_te'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
#                impactl2ded_Fix_RO_MAX['impact'],label='QC',color='tab:blue')#alpha=0.5,
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
# # plt.show()
