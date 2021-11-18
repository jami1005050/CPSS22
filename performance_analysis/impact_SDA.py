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

impactl1ded_Fix_RO_MAX = impact_l1_ded[( impact_l1_ded['ro_max'] == 28 )&
                        ( impact_l1_ded['ro_mal'] == 0.20)]#
impactl2ded_Fix_RO_MAX = impact_l2_ded[( impact_l2_ded['ro_max'] == 28)&
                        ( impact_l2_ded['ro_mal'] == 0.20)]
impactQCded_Fix_RO_MAX = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 28 )&
                        ( impact_Q_C_ded['ro_mal'] == 0.20)]
impactNQCded_Fix_RO_MAX = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 28 )&
                        ( impact_NQ_C_ded['ro_mal'] == 0.20)]
impactQHded_Fix_RO_MAX = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 28)&
                        ( impact_Q_H_ded['ro_mal'] == 0.20)]
impactNQHded_Fix_RO_MAX = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 28) &
                               (impact_NQ_H_ded['ro_mal'] == 0.20)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
p = ax.plot_trisurf(impactl1ded_Fix_RO_MAX['epsilon'],
               impactl1ded_Fix_RO_MAX['del_avg_te'],
               impactl1ded_Fix_RO_MAX['impact'],label ='QH',color='tab:olive') #alpha=0.5,

q= ax.plot_trisurf(impactl2ded_Fix_RO_MAX['epsilon'],
               impactl2ded_Fix_RO_MAX['del_avg_te'],  #     cmap=matplotlib.cm.inferno,antialiased=True,
               impactl2ded_Fix_RO_MAX['impact'],label='QC',color='tab:blue')#alpha=0.5,
p._facecolors2d = p._facecolor3d
p._edgecolors2d = p._edgecolor3d

q._facecolors2d = q._facecolor3d
q._edgecolors2d = q._edgecolor3d
ax.set_xlabel('$\delta_{avg}^{(p)}$',labelpad=10)
ax.set_ylabel(r'$\rho_{mal}^{(p)}$',labelpad=10)
ax.set_zlabel('Impact',labelpad=10)
# ax.set_xlim3d(min(impact_nQ_FIX_TR_DEL['tr_del_avg']),max(impact_nQ_FIX_TR_DEL['tr_del_avg']))
# ax.set_ylim3d(min(impact_nQ_FIX_TR_DEL['romal']),max(impact_nQ_FIX_TR_DEL['romal']))
# ax.set_zlim3d(min(impact_nQ_FIX_TR_DEL['impact_C']),300)
# ax.xaxis.set_major_locator(plt.MaxNLocator(2))
# ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# ax.zaxis.set_major_locator(plt.MaxNLocator(3))
ax.view_init(elev=20, azim=-20.)
# fig.colorbar(p,ax=ax,orientation="horizontal", pad=0.05)
plt.legend()
plt.show()



# impactl1ded_VTRD = impact_l1_ded[( impact_l1_ded['epsilon'] == 200 )&
#                         ( impact_l1_ded['del_avg_te'] == 200)]
# impactl2ded_VTRD = impact_l2_ded[(impact_l2_ded['epsilon'] == 200) &
#                             (impact_l2_ded['del_avg_te'] == 200)]
# impactQCded_VTRD = impact_Q_C_ded[(impact_Q_C_ded['epsilon'] == 200) &
#                              (impact_Q_C_ded['del_avg_te'] == 200)]
# impactNQCded_VTRD = impact_NQ_C_ded[(impact_NQ_C_ded['epsilon'] == 200) &
#                                (impact_NQ_C_ded['del_avg_te'] == 200)]
# impactQHded_VTRD = impact_Q_H_ded[(impact_Q_H_ded['epsilon'] == 200) &
#                              (impact_Q_H_ded['del_avg_te'] == 200)]
# impactNQHded_VTRD = impact_NQ_H_ded[( impact_NQ_H_ded['epsilon'] == 200 )&
#                         ( impact_NQ_H_ded['del_avg_te'] == 200)]
#
#
# impactl1ded_VTED = impact_l1_ded[( impact_l1_ded['epsilon'] == 50 )&
#                         ( impact_l1_ded['ro_mal'] == 0.20)]
# impactl2ded_VTED = impact_l2_ded[(impact_l2_ded['epsilon'] == 50) &
#                             (impact_l2_ded['ro_mal'] == 0.20)]
# impactQCded_VTED = impact_Q_C_ded[(impact_Q_C_ded['epsilon'] == 50) &
#                              (impact_Q_C_ded['ro_mal'] == 0.20)]
# impactNQCded_VTED = impact_NQ_C_ded[(impact_NQ_C_ded['epsilon'] == 50) &
#                                (impact_NQ_C_ded['ro_mal'] == 0.20)]
# impactQHded_VTED = impact_Q_H_ded[(impact_Q_H_ded['epsilon'] == 50) &
#                              (impact_Q_H_ded['ro_mal'] == 0.20)]
# impactNQHded_VTED = impact_NQ_H_ded[(impact_NQ_H_ded['epsilon'] == 50) &
#                                (impact_NQ_H_ded['ro_mal'] == 0.20)]

