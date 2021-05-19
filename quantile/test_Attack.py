from utility.common import *
#Huber loss  b=0.006
tao_max_H = 0.1075
tao_min_H = -0.1311
#Cauchy loss b=0.006
tao_max_C = 0.10
tao_min_C = -0.1086

#Quantile loss
tao_max_Q = 0.0925
tao_min_Q = -0.11

# testing_residualM4M6 = pd.read_csv("../data/test_residual_new/TestR_DA_del200_romal30_M04M06.csv") #91-181
testing_residualM7M9 = pd.read_csv("../data/test_residual_new/TestR_DA_del200_romal30_M07M09.csv")  #182-273
tier2_Q, first_detected_Q,false_alarm_tier2_Q = testing_tau(testing_residualM7M9,tao_max_Q,tao_min_Q)
tier2_for_C, first_detected_C,false_alarm_tier2_C = testing_tau(testing_residualM7M9,tao_max_C,tao_min_C)
tier2_for_H, first_detected_H,false_alarm_tier2_H = testing_tau(testing_residualM7M9,tao_max_H,tao_min_H)

