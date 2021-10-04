import matplotlib.pyplot as plt
from utility.constant import E

SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24
number_of_meters = 192
attack_start_day = 1
attack_end_day = 90
number_of_reports = 24
del_avg = 100
ro_mal = .3

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

#Huber loss  b=0.006
tao_max_HA = 0.09
tao_min_HA = -0.09
tao_max_H = 0.065
tao_min_H = -0.065

#Cauchy loss b=0.006
tao_max_CA = 0.105
tao_min_CA = -0.105
tao_max_C = 0.075
tao_min_C = -0.075

#Quantile loss
tao_max_QA = 0.0975
tao_min_QA = -0.0975
tao_max_Q = 0.065
tao_min_Q = -0.065


# plt.ylim(0,160)
First_Detected_Q = 74
First_Detected_QA = 78

First_Detected_C = 75
First_Detected_CA = 90

First_Detected_H = 74
First_Detected_HA = 77

range_Q =First_Detected_Q-attack_start_day
range_QA =First_Detected_QA-attack_start_day

range_H =First_Detected_H-attack_start_day
range_HA =First_Detected_HA-attack_start_day

range_C =First_Detected_C-attack_start_day
range_CA =First_Detected_CA-attack_start_day

total_change_std_limit_QR_l1 = abs(tao_max_Q - tao_max_QA) + abs(tao_min_Q - tao_min_QA)
impact_Q = del_avg * ro_mal * number_of_meters * E * range_Q*number_of_reports/1000
impact_QA = del_avg * ro_mal * number_of_meters * E * range_QA*number_of_reports/1000
impact_per_std_limit_change_Q = (impact_QA-impact_Q)/total_change_std_limit_QR_l1

total_change_std_limit_C = abs(tao_max_C - tao_max_CA) + abs(tao_min_C - tao_min_CA)
impact_C = del_avg * ro_mal * number_of_meters * E * range_C*number_of_reports/1000
impact_CA = del_avg * ro_mal * number_of_meters * E * range_CA*number_of_reports/1000
impact_per_std_limit_change_C = (impact_CA-impact_C)/total_change_std_limit_C

total_change_std_limit_H = abs(tao_max_H - tao_max_HA) + abs(tao_min_H - tao_min_HA)
impact_H = del_avg * ro_mal * number_of_meters * E * range_H*number_of_reports/1000
impact_HA = del_avg * ro_mal * number_of_meters * E * range_HA*number_of_reports/1000
impact_per_std_limit_change_H = (impact_QA-impact_Q)/total_change_std_limit_H


# plt.bar(["Q","H"], [impact_per_std_limit_change_Q/range_Q,impact_per_std_limit_change_H/range_H],
#         color=[ 'violet','blue'])
plt.bar(["Q","C"], [impact_per_std_limit_change_Q/range_Q,impact_per_std_limit_change_C/range_C],
        color=[ 'violet','blue'])
# plt.bar(["Q","H"], [impact_QA/range_Q,impact_HA/range_H],
#         color=[ 'violet','blue'])
# print("range QA",range_Q," range HA",range_H)
# plt.bar(["Q","C"], [impact_QA/range_Q,impact_CA/range_C],
#         color=[ 'violet','blue'])

plt.ylabel("Increased Impact/Day")
plt.show()