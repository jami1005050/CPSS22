import pandas as pd
import matplotlib.pyplot as plt

impact_l1_ded = pd.read_csv('../test_QP/impact_test/impact_RA_L1_ded.csv')
impact_l2_ded = pd.read_csv('../test_QP/impact_test/impact_RA_L2_ded.csv')
impact_Q_C_ded = pd.read_csv('../test_C/impact_test/impact_RA_Q_C_ded.csv')
impact_NQ_C_ded = pd.read_csv('../test_C/impact_test/impact_RA_NQ_C_ded.csv')
impact_Q_H_ded = pd.read_csv('../test_H/impact_test/impact_RA_Q_H_ded.csv')
impact_NQ_H_ded = pd.read_csv('../test_H/impact_test/impact_RA_NQ_H_ded.csv')


impactl1ded_VR = impact_l1_ded[( impact_l1_ded['del_avg_tr'] == 200 )&
                        ( impact_l1_ded['del_avg_te'] == 200)]#
impactl2ded_VR = impact_l2_ded[( impact_l2_ded['del_avg_tr'] == 200 )&
                        ( impact_l2_ded['del_avg_te'] == 200)]
impactQCded_VR = impact_Q_C_ded[( impact_Q_C_ded['del_avg_tr'] == 200 )&
                        ( impact_Q_C_ded['del_avg_te'] == 200)]
impactNQCded_VR = impact_NQ_C_ded[( impact_NQ_C_ded['del_avg_tr'] == 200 )&
                        ( impact_NQ_C_ded['del_avg_te'] == 200)]
impactQHded_VR = impact_Q_H_ded[( impact_Q_H_ded['del_avg_tr'] == 200 )&
                        ( impact_Q_H_ded['del_avg_te'] == 200)]
impactNQHded_VR = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_tr'] == 200) &
                               (impact_NQ_H_ded['del_avg_te'] == 200)]

impactl1ded_VTRD = impact_l1_ded[( impact_l1_ded['del_avg_tr'] == 200 )&
                        ( impact_l1_ded['del_avg_te'] == 200)]
impactl2ded_VTRD = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 200) &
                            (impact_l2_ded['del_avg_te'] == 200)]
impactQCded_VTRD = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 200) &
                             (impact_Q_C_ded['del_avg_te'] == 200)]
impactNQCded_VTRD = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 200) &
                               (impact_NQ_C_ded['del_avg_te'] == 200)]
impactQHded_VTRD = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 200) &
                             (impact_Q_H_ded['del_avg_te'] == 200)]
impactNQHded_VTRD = impact_NQ_H_ded[( impact_NQ_H_ded['del_avg_tr'] == 200 )&
                        ( impact_NQ_H_ded['del_avg_te'] == 200)]


impactl1ded_VTED = impact_l1_ded[( impact_l1_ded['del_avg_tr'] == 50 )&
                        ( impact_l1_ded['ro_mal'] == 0.20)]
impactl2ded_VTED = impact_l2_ded[(impact_l2_ded['del_avg_tr'] == 50) &
                            (impact_l2_ded['ro_mal'] == 0.20)]
impactQCded_VTED = impact_Q_C_ded[(impact_Q_C_ded['del_avg_tr'] == 50) &
                             (impact_Q_C_ded['ro_mal'] == 0.20)]
impactNQCded_VTED = impact_NQ_C_ded[(impact_NQ_C_ded['del_avg_tr'] == 50) &
                               (impact_NQ_C_ded['ro_mal'] == 0.20)]
impactQHded_VTED = impact_Q_H_ded[(impact_Q_H_ded['del_avg_tr'] == 50) &
                             (impact_Q_H_ded['ro_mal'] == 0.20)]
impactNQHded_VTED = impact_NQ_H_ded[(impact_NQ_H_ded['del_avg_tr'] == 50) &
                               (impact_NQ_H_ded['ro_mal'] == 0.20)]



# print((impactNQHded))
