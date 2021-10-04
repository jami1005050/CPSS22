import matplotlib.pyplot as plt
from utility.constant import E
SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24
number_of_meters = 192
attack_start_day = 91
attack_end_day = 181
number_of_reports = 24
del_avg1 = 100
del_avg2 = 150
del_avg3 = 200
ro_mal = .4
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

#Huber loss  b=0.006
tao_max_H = 0.085
tao_min_H = -0.0927
#Cauchy loss b=0.006
tao_max_C = 0.0775
tao_min_C = -0.0427
#Quantile loss
tao_max_Q = 0.0825
tao_min_Q = -0.082658004

# plt.ylim(0,160)
First_Detected_Q_D100 = 118
First_Detected_Q_D150 = 98
First_Detected_Q_D200 = 92

First_Detected_C_D100 = 107
First_Detected_C_D150 = 96
First_Detected_C_D200 = 92

First_Detected_H_D100 = 119
First_Detected_H_D150 = 99
First_Detected_H_D200 = 93

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
plt.ylabel("Impact")
plt.show()

dict = {'Q':[impact_Q_D100,impact_Q_D150,impact_Q_D200],
         'H':[impact_H_D100,impact_H_D150,impact_H_D200],
         'C':[impact_C_D100,impact_C_D150,impact_C_D200]}
print(dict)