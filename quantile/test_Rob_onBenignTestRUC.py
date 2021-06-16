import pandas as pd
from utility.common import *
#NQ Cauchy
# 0.0375 -0.0302 attacked romax 60 eps .02
# 0.0125 -0.0127 benign
# 0.0125 -0.0114 attacked romax 10 eps 12
#NQ Huber
# 0.05 -0.0427 attacked romax 60 eps .02
# 0.03 -0.0302 benign
# 0.0525 -0.0389 attacked romax 10 eps 12
#Quantile L1
# 0.0825 -0.082658004 romax 60 eps .02
# 0.0875	-0.096353261 romax 10 eps .12
#Quantile L2
# 0.095 -0.1423795698887212 romax 60 eps .02

#Quantile Cauchy and Huber
# 0.0775	-0.0427 -- C when romax -- 60  and epsilon 0.02
# 0.085	-0.0927 -- H

#Quantile loss
tao_max_Q = 0.0875
tao_min_Q = -0.082658004
#Cauchy loss  b=0.006 --.01
tao_max_NQC = 0.0375
tao_min_NQC = -0.0302
#Huber loss b=0.006 --.01
tao_max_NQH = 0.05
tao_min_NQH = -0.0427
tao_max_QL2 = 0.095
tao_min_QL2 = -0.1423795698887212
tao_max_QH = 0.085
tao_min_QH = -0.0927
tao_max_QC = 0.0775
tao_min_QC = -0.0427

# testing_residualM4M6 = pd.read_csv("../data/test_residuals/TestR_DA_del100_romal30_M4M6.csv") #91-181
testing_residualM7M9 = pd.read_csv("../data/Test_RUC_Benign.csv")  #182-273
false_alarm_tier2_Q = testing_EFA(testing_residualM7M9,tao_max_Q,tao_min_Q)
false_alarm_tier2_QL2 = testing_EFA(testing_residualM7M9,tao_max_QL2,tao_min_QL2)
false_alarm_tier2_NQC = testing_EFA(testing_residualM7M9,tao_max_NQC,tao_min_NQC)
false_alarm_tier2_NQH = testing_EFA(testing_residualM7M9,tao_max_NQH,tao_min_NQH)
false_alarm_tier2_QC = testing_EFA(testing_residualM7M9,tao_max_QC,tao_min_QC)
false_alarm_tier2_QH = testing_EFA(testing_residualM7M9,tao_max_QH,tao_min_QH)

print(false_alarm_tier2_Q)
print(false_alarm_tier2_QL2)
print(false_alarm_tier2_NQC)
print(false_alarm_tier2_NQH)
print(false_alarm_tier2_QC)
print(false_alarm_tier2_QH)