import matplotlib.pyplot as plt
from utility.constant import E
SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24
number_of_meters = 192
attack_start_day = 182
attack_end_day = 273
number_of_reports = 24
del_avg1 = 100
del_avg2 = 150
del_avg3 = 200
ro_mal = .3
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

#Huber loss  b=0.006
tao_max_H = 0.1075
tao_min_H = -0.1311
#Cauchy loss b=0.006
tao_max_C = 0.10
tao_min_C = -0.1086

#Quantile loss
tao_max_Q = 0.0925
tao_min_Q = -0.11

# plt.ylim(0,160)
First_Detected_Q_D100 = 226
First_Detected_Q_D150 = 226
First_Detected_Q_D200 = 186

First_Detected_C_D100 = 226
First_Detected_C_D150 = 225
First_Detected_C_D200 = 186


First_Detected_H_D100 = 273
First_Detected_H_D150 = 226
First_Detected_H_D200 = 187

range_Q_D100 =First_Detected_Q_D100-attack_start_day
range_Q_D150 =First_Detected_Q_D150-attack_start_day
range_Q_D200 =First_Detected_Q_D200-attack_start_day

range_H_D100 =First_Detected_H_D100-attack_start_day
range_H_D150 =First_Detected_H_D150-attack_start_day
range_H_D200 =First_Detected_H_D200-attack_start_day

range_C_D100 =First_Detected_C_D100-attack_start_day
range_C_D150 =First_Detected_C_D150-attack_start_day
range_C_D200 =First_Detected_C_D200-attack_start_day

impact_Q_D100 = del_avg1 * ro_mal * number_of_meters * E * range_Q_D100*number_of_reports/1000
impact_Q_D150 = del_avg2 * ro_mal * number_of_meters * E * range_Q_D150*number_of_reports/1000
impact_Q_D200 = del_avg3 * ro_mal * number_of_meters * E * range_Q_D200*number_of_reports/1000

impact_H_D100 = del_avg1 * ro_mal * number_of_meters * E * range_H_D100*number_of_reports/1000
impact_H_D150 = del_avg2 * ro_mal * number_of_meters * E * range_H_D150*number_of_reports/1000
impact_H_D200 = del_avg3 * ro_mal * number_of_meters * E * range_H_D200*number_of_reports/1000

impact_C_D100 = del_avg1 * ro_mal * number_of_meters * E * range_C_D100*number_of_reports/1000
impact_C_D150 = del_avg2 * ro_mal * number_of_meters * E * range_C_D150*number_of_reports/1000
impact_C_D200 = del_avg3 * ro_mal * number_of_meters * E * range_C_D200*number_of_reports/1000

# plt.bar(["Q","H","C"], [impact_Q_D100,impact_H_D100,impact_C_D100],color=[ 'violet','blue','cyan'])
# plt.bar(["Q","H","C"], [impact_Q_D150,impact_H_D150,impact_C_D150],color=[ 'violet','blue','cyan'])
plt.bar(["Q","H","C"], [impact_Q_D200,impact_H_D200,impact_C_D200],color=[ 'violet','blue','cyan'])
plt.ylabel("Increased Impact/Day")
plt.show()