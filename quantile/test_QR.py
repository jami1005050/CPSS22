from utility.common import *
#Quantile loss
tao_max_QA_l1 = 0.0975
tao_min_QA_l1 = -0.0975
tao_max_Q_l1 = 0.065
tao_min_Q_l1 = -0.065
t_max_att_QR_l1 =  0.12 # when romax -- 50 and epsilon .07
t_min_att_QR_l1 = -0.1175
# t_max_org_QR_l2 = 0.08
# t_min_org_QR_l2 = -0.08
# t_max_att_QR_l2 =  0.1375 # when romax --50 and epsilon .07
# t_min_att_QR_l2 = -0.14
#Cauchy loss  b=0.006
tao_max_HA = 0.09
tao_min_HA = -0.09
tao_max_H = 0.065
tao_min_H = -0.065
#Hubur loss b=0.006
tao_max_CA = 0.105
tao_min_CA = -0.105
tao_max_C = 0.075
tao_min_C = -0.075
# testing_residualM1M3 = pd.read_csv("../data/test_residuals/TestR_DA_del100_romal30_M1M3.csv") #1-90
# testing_residualM4M6 = pd.read_csv("../data/test_residuals/TestR_DA_del100_romal30_M4M6.csv") #91-181
# testing_residualM7M9 = pd.read_csv("../data/test_residuals/TestR_DA_del100_romal30_M7M9.csv")  #182-273
testing_residualM10M12 = pd.read_csv("../data/test_ruc/test_residuals/TestR_DA_del100_romal30_M10M12.csv") #244-365
# testing_attacked_threshold(testing_residual,tao_max_Q_l1,tao_min_Q_l1,t_max_att_QR_l1,t_min_att_QR_l1)
# testing_attacked_threshold(testing_residual,t_max_org_QR_l2,t_min_org_QR_l2,t_max_att_QR_l2,t_min_att_QR_l2)
tier2_Q, first_detected_Q,false_alarm_tier2_Q = testing_tau(testing_residualM10M12,tao_max_Q_l1,tao_min_Q_l1)
tier2_for_QA, first_detected_QA,false_alarm_tier2_QA = testing_tau(testing_residualM10M12,tao_max_QA_l1,tao_min_QA_l1)
tier2_for_C, first_detected_C,false_alarm_tier2_C = testing_tau(testing_residualM10M12,tao_max_C,tao_min_C)
tier2_for_CA, first_detected_CA,false_alarm_tier2_CA = testing_tau(testing_residualM10M12,tao_max_CA,tao_min_CA)
tier2_for_H, first_detected_H,false_alarm_tier2_H = testing_tau(testing_residualM10M12,tao_max_H,tao_min_H)
tier2_for_HA, first_detected_HA,false_alarm_tier2_HA = testing_tau(testing_residualM10M12,tao_max_HA,tao_min_HA)

