import matplotlib.pyplot as plt


SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
imp_m4m6 = {'Q': [464.48639999999995, 223.94879999999998, 66.3552],
            'H': [497.6639999999999, 248.832, 66.3552],
            'C': [265.4208, 149.29919999999998, 33.1776]}
imp_m7m9 = {'Q': [729.9072, 1069.9776000000002, 99.5328],
            'H': [729.9072, 1094.8608, 132.7104],
            'C': [696.7296, 1020.2112, 66.3552]}

days_undetected_m4m6 = {'Q':[28,9,2],'H':[30,10,2],'C':[16,7,1]}
days_undetected_m7m9 = {'Q':[45,44,4],'H':[45,45,5],'C':[43,42,3]}
del_avg = [100,150,200]
merged = {}
days_merged = {}
for key in imp_m4m6.keys():
    merged[key] = []
    days_merged[key] = []
    for i in range(len(imp_m4m6[key])):
        merged[key].append((imp_m4m6[key][i]+imp_m7m9[key][i])/(days_undetected_m4m6[key][i]+days_undetected_m7m9[key][i]))
        days_merged[key].append(days_undetected_m4m6[key][i]+days_undetected_m7m9[key][i])

print(merged)
# print(days_merged)
plt.plot(del_avg, merged['Q'],marker = "D", markevery=1,label ='Q')
plt.plot(del_avg, merged['H'],marker = "<", markevery=1,label ='H')
plt.plot(del_avg, merged['C'],marker = ">", markevery=1,label ='C')
plt.xlabel("Del")
plt.ylabel("Impact")
plt.legend()
plt.show()