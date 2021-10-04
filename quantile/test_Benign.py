from utility.common import *
# -0.0651580041643599 0.0675

#Quantile loss
tao_max_Q = 0.0675
tao_min_Q = -0.0651580041643599
#Cauchy loss  b=0.006 --.01
tao_max_C = 0.065
tao_min_C = -0.0652
#Huber loss b=0.006 --.01
tao_max_H = 0.0775
tao_min_H = -0.0777
# testing_residualM4M6 = pd.read_csv("../data/test_residuals/TestR_DA_del100_romal30_M4M6.csv") #91-181
testing_residualM7M9 = pd.read_csv("../data/test_ruc/test_residual_CA_AA/TestR_AA_del500_romal40_M07M09.csv")  #182-273
tier2_Q, first_detected_Q,false_alarm_tier2_Q = testing_tau(testing_residualM7M9,tao_max_Q,tao_min_Q)
tier2_for_C, first_detected_C,false_alarm_tier2_C = testing_tau(testing_residualM7M9,tao_max_C,tao_min_C)
tier2_for_H, first_detected_H,false_alarm_tier2_H = testing_tau(testing_residualM7M9,tao_max_H,tao_min_H)

