#Plot benign Comparison
import matplotlib.pyplot as plt
import json
SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/result_data/impact/impact_benign_C.json')
f_H = open('../test_H/result/impact/impact_benign_H.json')
f_Q = open('../test_QB/impact_benign_Q.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
beta = str(0.006)
del_avg = str(175)
C_arr_imp = []
C_arr_efa = []
H_arr_imp = []
H_arr_efa = []
Q_arr_imp = []
Q_arr_efa = []
for key1 in impact_dict_C.keys():
    # C_arr_imp.append(impact_dict_C[key1][beta][del_avg]['impact']/impact_dict_C[key1][beta][del_avg]['days_undetected'])
    C_arr_imp.append(impact_dict_C[key1][beta][del_avg]['impact'])
    C_arr_efa.append(impact_dict_C[key1][beta][del_avg]['Efa'])
    H_arr_imp.append(impact_dict_H[key1][beta][del_avg]['impact'])
    H_arr_efa.append(impact_dict_H[key1][beta][del_avg]['Efa'])
    Q_arr_imp.append(impact_dict_Q[key1][del_avg]['impact'])
    Q_arr_efa.append(impact_dict_Q[key1][del_avg]['Efa'])

plt.plot(C_arr_efa, C_arr_imp,marker = "D", markevery=1,label ='C')
plt.plot( H_arr_efa,H_arr_imp,marker = "<", markevery=1,label ='H')
plt.plot(Q_arr_efa,Q_arr_imp, marker = ">", markevery=1,label ='Q')
plt.xlabel("Effective Time between False Alarm")
plt.ylabel("Impact")
plt.legend()
plt.show()