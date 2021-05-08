import matplotlib.pyplot as plt

from utility.constant import E

SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
number_of_meters = 192
attack_start_day = 91
attack_end_day = 181
del_avg = 100
ro_mal = .3
plt.ylim(0,160)
First_Detected_org_QR_l1=  99
First_Detected_att_QR_l1=  102
First_Detected_org_QR_l2=  100
First_Detected_att_QR_l2=  110
First_Detected_org_LR_l1=  97
First_Detected_att_LR_l1=  100
First_Detected_org_LR_l2=  94
First_Detected_att_LR_l2=  100
# First Detected org:  97 First Detected atta:  100
# First Detected org:  94 First Detected atta:  100
#region L1
range_org_QR_l1 =First_Detected_org_QR_l1-attack_start_day
range_att_QR_l1 =First_Detected_att_QR_l1-attack_start_day
t_max_org_QR_l1 = 0.065
t_min_org_QR_l1 = -0.065
t_max_att_QR_l1 =  0.12 # when romax -- 50 and epsilon .07
t_min_att_QR_l1 = -0.1175
total_change_std_limit_QR_l1 = abs(t_max_org_QR_l1 - t_max_att_QR_l1) + abs(t_min_org_QR_l1 - t_min_att_QR_l1)
impact_org_QR_l1 = del_avg * ro_mal * number_of_meters * E * range_org_QR_l1*24/1000
impact_att_QR_l1 = del_avg * ro_mal * number_of_meters * E * range_att_QR_l1*24/1000
impact_per_std_limit_change_QR_l1 = (impact_att_QR_l1-impact_org_QR_l1)/total_change_std_limit_QR_l1
#endregion

#region l2
t_max_org_QR_l2 = 0.08
t_min_org_QR_l2 = -0.08
t_max_att_QR_l2 =  0.1375 # when romax --50 and epsilon .07
t_min_att_QR_l2 = -0.14
range_org_QR_l2 =First_Detected_org_QR_l2-attack_start_day
range_att_QR_l2 =First_Detected_att_QR_l2-attack_start_day

total_change_std_limit_QR_l2 = abs(t_max_org_QR_l2 - t_max_att_QR_l2) + abs(t_min_org_QR_l2 - t_min_att_QR_l2)
impact_org_QR_l2 = del_avg * ro_mal * number_of_meters * E * range_org_QR_l2*24/1000
impact_att_QR_l2 = del_avg * ro_mal * number_of_meters * E * range_att_QR_l2*24/1000
impact_per_std_limit_change_QR_l2 = (impact_att_QR_l2-impact_org_QR_l2)/total_change_std_limit_QR_l2
#endregion
#endregion
#region LR
#region l1
range_org_LR_l1 =First_Detected_org_LR_l1-attack_start_day
range_att_LR_l1 = First_Detected_att_LR_l1 - attack_start_day
t_max_org_LR_l1 = 0.0275
t_min_org_LR_l1 = -0.0275
t_max_att_LR_l1 =  0.075
t_min_att_LR_l1 = -0.075


total_change_std_limit_LR_l1 = abs(t_max_org_LR_l1 - t_max_att_LR_l1) + abs(t_min_org_LR_l1 - t_min_att_LR_l1)
impact_org_LR_l1 = del_avg * ro_mal * number_of_meters * E * range_org_LR_l1*24/1000
impact_att_LR_l1 = del_avg * ro_mal * number_of_meters * E * range_att_LR_l1*24/1000
impact_per_std_limit_change_LR_l1 = (impact_att_LR_l1-impact_org_LR_l1)/total_change_std_limit_LR_l1

#endregion
#region l2
range_org_LR_l2 =First_Detected_org_LR_l2-attack_start_day
range_att_LR_l2 =First_Detected_att_LR_l2-attack_start_day
t_max_org_LR_l2 = 0.0425
t_min_org_LR_l2 = -0.0425
t_max_att_LR_l2 =  0.0875
t_min_att_LR_l2 = -0.0875
total_change_std_limit_LR_l2 = abs(t_max_org_LR_l2 - t_max_att_LR_l2) + abs(t_min_org_LR_l2 - t_min_att_LR_l2)
impact_org_LR_l2 = del_avg * ro_mal * number_of_meters * E * range_org_LR_l2*24/1000
impact_att_LR_l2 = del_avg * ro_mal * number_of_meters * E * range_att_LR_l2*24/1000
impact_per_std_limit_change_LR_l2 = (impact_att_LR_l2-impact_org_LR_l2)/total_change_std_limit_LR_l2
#endregion
#endregion

# plt.bar(["Not Attacked","Attacked"], [impact_org_QR_l1/(24*range_org_QR_l1),impact_att_QR_l1/(24*range_org_QR_l1)],
#         color=[ 'green','red'])
# plt.bar(["Not Attacked","Attacked"], [impact_org_QR_l2/(24*range_org_QR_l2),impact_att_QR_l2/(24*range_org_QR_l2)],
#         color=[ 'green','red'])
# plt.bar(["Not Attacked","Attacked"], [impact_org_LR_l1/(range_org_LR_l1*24),impact_att_LR_l1/(range_org_LR_l1*24)],
#         color=[ 'green','red'])
# plt.bar(["Not Attacked","Attacked"], [impact_org_LR_l2/(24*range_org_LR_l2),impact_att_LR_l2/(range_org_LR_l2*24)],
#         color=[ 'green','red'])
# plt.ylabel("Increasing Impact($/Hour)")
#
# plt.bar(["LR","QR"], [impact_per_std_limit_change_LR_l1/range_org_LR_l1,impact_per_std_limit_change_QR_l1/range_org_QR_l1],
#         color=[ 'black','blue'])
plt.bar(["L1","L2"], [impact_per_std_limit_change_QR_l1/range_org_QR_l1,impact_per_std_limit_change_QR_l2/range_org_QR_l2],
        color=[ 'black','blue'])

plt.ylabel("Increased Impact/Day")
plt.show()
