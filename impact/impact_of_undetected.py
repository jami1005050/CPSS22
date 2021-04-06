import matplotlib.pyplot as plt

from utility.constant import E

SMALL_SIZE = 8
MEDIUM_SIZE = 14
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
#QR-->Tier 2 Detection for Org Threshold: 52 First Detected org: 99 First Detected atta: 100 false_alarm_tier2_org: 19 false_alarm_tier2_att: 12
number_of_meters = 192
attack_start_day = 91
del_avg = 100
ro_mal = .3
attack_end_day = 181
range_att_QR =100-91
range_org_QR =99-91
t_max_QR = 0.065
t_min_QR = -0.065
t_max_att_QR =  0.075
t_min_att_QR = -0.0875
total_change_std_limit_QR = abs(t_max_QR-t_max_att_QR) + abs(t_min_QR-t_min_att_QR)
#LR-->Tier 2 Detection for Org Threshold: 56 First Detected org: 97 First Detected atta: 99 false_alarm_tier2_org: 38 false_alarm_tier2_att: 26

range_att_LR =99-91
range_org_LR =97-91
t_max_LR = 0.0275
t_min_LR = -0.0275
t_max_att_LR =  0.0475
t_min_att_LR = -0.055
total_change_std_limit_LR = abs(t_max_LR-t_max_att_LR) + abs(t_min_LR-t_min_att_LR)

impact_org_QR = del_avg * ro_mal * number_of_meters * E * range_org_QR/1000
impact_att_QR = del_avg * ro_mal * number_of_meters * E * range_att_QR/1000
impact_per_std_limit_change_QR = (impact_att_QR-impact_org_QR)/total_change_std_limit_QR
plt.bar(["Not Attacked QR","Attacked QR"], [impact_org_QR/24,impact_att_QR/24],
        color=[ 'green','red'])


impact_org_LR = del_avg * ro_mal * number_of_meters * E * range_org_LR/1000
impact_att_LR = del_avg * ro_mal * number_of_meters * E * range_att_LR/1000
impact_per_std_limit_change_LR = (impact_att_LR-impact_org_LR)/total_change_std_limit_LR

# plt.bar(["Not Attacked LR","Attacked LR"], [impact_org_LR/24,impact_att_LR/24],
#         color=[ 'green','red'])
plt.ylabel("Increasing Impact($/Hour)")

# plt.title("Compared impact of Undetected attack")

# plt.bar(["LR","QR"], [impact_per_std_limit_change_LR,impact_per_std_limit_change_QR],
#         color=[ 'black','blue'])
# plt.ylabel("Impact Rate")

plt.show()
