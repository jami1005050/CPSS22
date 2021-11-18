import pandas as pd
import matplotlib.pyplot as plt

impact_l1_add = pd.read_csv('../test_QP/impact_test/impact_SA_L1_add.csv')
impact_l2_add = pd.read_csv('../test_QP/impact_test/impact_SA_L2_add.csv')
impact_Q_C_add = pd.read_csv('../test_C/impact_test/impact_SA_Q_C_add.csv')
impact_NQ_C_add = pd.read_csv('../test_C/impact_test/impact_SA_NQ_C_add.csv')
impact_Q_H_add = pd.read_csv('../test_H/impact_test/impact_SA_Q_H_add.csv')
impact_NQ_H_add = pd.read_csv('../test_H/impact_test/impact_SA_NQ_H_add.csv')

avg_l1 = impact_l1_add['impact'].mean()
avg_l2 = impact_l2_add['impact'].mean()
avg_QC = impact_Q_C_add['impact'].mean()
avg_NQC = impact_NQ_C_add['impact'].mean()
avg_QH = impact_Q_H_add['impact'].mean()
avg_NQH = impact_NQ_H_add['impact'].mean()
print(avg_l1,' ',avg_l2,' ',avg_QC,' ',avg_NQC,' ',avg_QH,' ',avg_NQH)
#In the plot the factors involved are following ro_max,del_avg_te, epsilon, ro_mal
#Ro_MAX 1:Large case 2:middle case 3:small case for 3D plot

impactl1add_VR = impact_l1_add[( impact_l1_add['ro_max'] == 400 )&
                        ( impact_l1_add['del_avg_te'] == 700)]#
impactl2add_VR = impact_l2_add[( impact_l2_add['ro_max'] == 400 )&
                        ( impact_l2_add['del_avg_te'] == 700)]
impactQCadd_VR = impact_Q_C_add[( impact_Q_C_add['ro_max'] == 400 )&
                        ( impact_Q_C_add['del_avg_te'] == 700)]
impactNQCadd_VR = impact_NQ_C_add[( impact_NQ_C_add['ro_max'] == 400 )&
                        ( impact_NQ_C_add['del_avg_te'] == 700)]
impactQHadd_VR = impact_Q_H_add[( impact_Q_H_add['ro_max'] == 400 )&
                        ( impact_Q_H_add['del_avg_te'] == 700)]
impactNQHadd_VR = impact_NQ_H_add[(impact_NQ_H_add['ro_max'] == 400) &
                               (impact_NQ_H_add['del_avg_te'] == 700)]

impactl1add_VTRD = impact_l1_add[( impact_l1_add['epsilon'] == 400 )&
                        ( impact_l1_add['del_avg_te'] == 700)]
impactl2add_VTRD = impact_l2_add[(impact_l2_add['epsilon'] == 400) &
                            (impact_l2_add['del_avg_te'] == 700)]
impactQCadd_VTRD = impact_Q_C_add[(impact_Q_C_add['epsilon'] == 400) &
                             (impact_Q_C_add['del_avg_te'] == 700)]
impactNQCadd_VTRD = impact_NQ_C_add[(impact_NQ_C_add['epsilon'] == 400) &
                               (impact_NQ_C_add['del_avg_te'] == 700)]
impactQHadd_VTRD = impact_Q_H_add[(impact_Q_H_add['epsilon'] == 400) &
                             (impact_Q_H_add['del_avg_te'] == 700)]
impactNQHadd_VTRD = impact_NQ_H_add[( impact_NQ_H_add['epsilon'] == 400 )&
                        ( impact_NQ_H_add['del_avg_te'] == 700)]


impactl1add_VTED = impact_l1_add[( impact_l1_add['epsilon'] == 100 )&
                        ( impact_l1_add['ro_max'] == 0.20)]
impactl2add_VTED = impact_l2_add[(impact_l2_add['epsilon'] == 100) &
                            (impact_l2_add['ro_max'] == 0.20)]
impactQCadd_VTED = impact_Q_C_add[(impact_Q_C_add['epsilon'] == 100) &
                             (impact_Q_C_add['ro_max'] == 0.20)]
impactNQCadd_VTED = impact_NQ_C_add[(impact_NQ_C_add['epsilon'] == 100) &
                               (impact_NQ_C_add['ro_max'] == 0.20)]
impactQHadd_VTED = impact_Q_H_add[(impact_Q_H_add['epsilon'] == 100) &
                             (impact_Q_H_add['ro_max'] == 0.20)]
impactNQHadd_VTED = impact_NQ_H_add[(impact_NQ_H_add['epsilon'] == 100) &
                               (impact_NQ_H_add['ro_max'] == 0.20)]


plt.plot(impactl1add_VTED['del_avg_te'],impactl1add_VTED['impact'],label='l1')
plt.plot(impactl2add_VTED['del_avg_te'],impactl2add_VTED['impact'],label='l2')
plt.plot(impactQCadd_VTED['del_avg_te'],impactQCadd_VTED['impact'],label = 'QC')
plt.plot(impactNQCadd_VTED['del_avg_te'],impactNQCadd_VTED['impact'],label = 'NQC')
plt.plot(impactQHadd_VTED['del_avg_te'],impactQHadd_VTED['impact'],label = 'QH')
plt.plot(impactNQHadd_VTED['del_avg_te'],impactNQHadd_VTED['impact'],label = 'NQH')
plt.legend()
plt.show()

# plt.show()
# print((impactNQHadd))
