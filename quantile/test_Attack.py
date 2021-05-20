from utility.common import *
# 0.07	-0.0709 -- C   when romax --5 and epsilon--0.12
# 0.0925	-0.0984 -- H
# 0.0775	-0.080884237 -- Q

# 0.0725	-0.0589 --C  When romax -- 10 and eplsion 0.12
# 0.115	-0.1164 -- H
# 0.0875	-0.096353261 -- Q

# 0.1775	-0.1402 --C when romax -- 60 and epsilon 0.12
# 0.185	-0.1902 --H
# 0.17	-0.172658004 --Q

# 0.0775	-0.0427 -- C when romax -- 60  and epsilon 0.02
# 0.085	-0.0927 -- H
# 0.0825	-0.082658004 -- Q

# 0.0775	-0.0877 --C when romax -- 60  and epsilon 0.02 b = .009
# 0.0875	-0.0927--H
# 0.0825	-0.082658004--Q
#Huber loss  b=0.006
tao_max_H = 0.1000
tao_min_H = -0.1136
#Cauchy loss b=0.006
tao_max_C = 0.0700
tao_min_C = -0.0661

#Quantile loss
tao_max_Q = 0.0975
tao_min_Q = -0.09606611918752106

# #Huber loss  b=0.006
# tao_max_H = 0.1075
# tao_min_H = -0.1311
# #Cauchy loss b=0.006
# tao_max_C = 0.10
# tao_min_C = -0.1086
#
# #Quantile loss
# tao_max_Q = 0.0925
# tao_min_Q = -0.11

testing_residualM4M6 = pd.read_csv("../data/test_residual_new/TestR_DA_del200_romal30_M07M09.csv") #91-181
# testing_residualM7M9 = pd.read_csv("../data/test_residual_CA_AA/TestR_CA_del100_romal40_M07M09.csv")  #182-273
tier2_Q, first_detected_Q,false_alarm_tier2_Q = testing_tau(testing_residualM4M6,tao_max_Q,tao_min_Q)
tier2_for_C, first_detected_C,false_alarm_tier2_C = testing_tau(testing_residualM4M6,tao_max_C,tao_min_C)
tier2_for_H, first_detected_H,false_alarm_tier2_H = testing_tau(testing_residualM4M6,tao_max_H,tao_min_H)

