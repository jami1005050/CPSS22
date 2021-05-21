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

# ROMAX 10 - EPS 0.06
# 	Quantile
# 		tmin after ROMAX QR:  -0.07885326123657704
# 		tmax after ROMAX QR:  0.0725
# 	Huber b = 0.006
# 		attacked_tau_max: 0.0850
# 		attacked_tau_min: -0.0989
# 	Cauchy
# 		attacked_tau_max: 0.0775
# 		attacked_tau_min: -0.0889
# ROMAX 30 - EPS 0.06
# 	Quantile
# 		tmin after ROMAX QR:  -0.09856611918752112
# 		tmax after ROMAX QR:  0.085
# 	Huber b = 0.006
# 		attacked_tau_max: 0.0925
# 		attacked_tau_min: -0.1186
# 	Cauchy b = 0.006
# 		attacked_tau_max: 0.0825
# 		attacked_tau_min: -0.0811

# ROMAX 60-- EPS 0.06
# 	Quantile
# 		tmin after ROMAX QR:  -0.11765800416435984
# 		tmax after ROMAX QR:  0.11750000000000001
# 	Huber b = 0.006
# 		attacked_tau_max: 0.1275
# 		attacked_tau_min: -0.1302
# 	Cauchy b = 0.006
# 		attacked_tau_max: 0.0900
# 		attacked_tau_min: -0.0802

# ROMAX 10-- EPS 0.02
# 	Quantile
# 		tmin after ROMAX QR:  -0.07015800416435986
# 		tmax after ROMAX QR:  0.0675
# 	Huber b = 0.006
# 		attacked_tau_max: 0.0775
# 		attacked_tau_min: -0.0852
# 	Cauchy b = 0.006
# 		attacked_tau_max: 0.0575
# 		attacked_tau_min: -0.0852
# ROMAX 30 - EPS 0.02
# 	Quantile
# 		tmin after ROMAX QR:  -0.07606611918752115
# 		tmax after ROMAX QR:  0.0725
# 	Huber b= 0.006
# 		attacked_tau_max: 0.0800
# 		attacked_tau_min: -0.0911
# 	Cauchy b = 0.006
# 		attacked_tau_max: 0.0725
# 		attacked_tau_min: -0.0786

# ROMAX 30-- EPS 0.12
# 	Quantile
# 		tmin after ROMAX QR:  -0.1335661191875211
# 		tmax after ROMAX QR:  0.12
# 	Huber b = 0.006
# 		attacked_tau_max: 0.1350
# 		attacked_tau_min: -0.1711
# 	Cauchy b = 0.006
# 		attacked_tau_max: 0.1350
# 		attacked_tau_min: -0.1386
#Huber loss  b=0.006
tao_max_H =  0.0875
tao_min_H = -0.0927
#Cauchy loss b=0.006
tao_max_C = 0.0775
tao_min_C = -0.0427
#Quantile loss
tao_max_Q = 0.0825
tao_min_Q = -0.082658004

testing_residualM4M6 = pd.read_csv("../data/test_residual_new/TestR_DA_del200_romal30_M07M09.csv") #91-181
# testing_residualM7M9 = pd.read_csv("../data/test_residual_CA_AA/TestR_CA_del100_romal40_M07M09.csv")  #182-273
tier2_Q, first_detected_Q,false_alarm_tier2_Q = testing_tau(testing_residualM4M6,tao_max_Q,tao_min_Q)
tier2_for_C, first_detected_C,false_alarm_tier2_C = testing_tau(testing_residualM4M6,tao_max_C,tao_min_C)
tier2_for_H, first_detected_H,false_alarm_tier2_H = testing_tau(testing_residualM4M6,tao_max_H,tao_min_H)

