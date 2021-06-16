import matplotlib.pyplot as plt
from utility.constant import E
SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24
number_of_meters = 192
attack_start_day = 182
attack_end_day = 273
number_of_reports = 24
del_avg = 100

ro_mal = .3
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

# 79 9 225 [18, 24, 25]
# 79 0 0 []
# 79 20 223 [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35]
# 79 19 224 [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# 79 19 224 [17, 18, 19, 23, 24, 25, 26, 27, 28]
# 79 7 225 [18, 19, 24, 25]
First_Detected_Q = 225
First_Detected_QL2 = 273
First_Detected_NQC = 223

First_Detected_NQH = 224
First_Detected_QC = 224
First_Detected_QH = 225

range_Q = First_Detected_Q-attack_start_day
range_QL2 = First_Detected_QL2-attack_start_day
range_NQC = First_Detected_NQC-attack_start_day

range_NQH = First_Detected_NQH-attack_start_day
range_QC = First_Detected_QC-attack_start_day
range_QH = First_Detected_QH-attack_start_day


impact_Q = del_avg * ro_mal * number_of_meters * E * range_Q*number_of_reports/1000
impact_QL2 = del_avg * ro_mal * number_of_meters * E * range_QL2*number_of_reports/1000
impact_NQC = del_avg * ro_mal * number_of_meters * E * range_NQC*number_of_reports/1000

impact_NQH = del_avg * ro_mal * number_of_meters * E * range_NQH*number_of_reports/1000
impact_QC = del_avg * ro_mal * number_of_meters * E * range_QC*number_of_reports/1000
impact_QH = del_avg * ro_mal * number_of_meters * E * range_QH*number_of_reports/1000

# plt.bar(["QL1","QL2","QH","QC"],
#         [impact_Q,impact_QL2,impact_QH,impact_QC],
#         color=[ 'violet','blue','cyan','tab:orange'])
plt.bar(["QC","NQH","NQC"],
        [impact_QC,impact_NQH,impact_NQC],
        color=['violet','tab:green','tab:olive'])
plt.ylabel("Impact")
plt.ylim(675,700)
plt.show()
#
# dict = {'Q':[impact_Q_D100,impact_Q_D150,impact_Q_D200],
#          'H':[impact_H_D100,impact_H_D150,impact_H_D200],
#          'C':[impact_C_D100,impact_C_D150,impact_C_D200]}
# print(dict)

