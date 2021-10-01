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
f_C = open('../test_C/result_data/impact/impact_poisoned_C.json')
f_H = open('../test_H/result/impact/impact_poisoned_H.json')
f_Q = open('../test_QP/result/impact/impact_poisoned_Q.json')
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
# print(impact_dict_C['2.0']['7'].keys())
# print(impact_dict_C['2.0']['7']['0.006806130721932213'].keys())
# print(impact_dict_C['1.0']['29']['0.004248316276166424']['0.006'].keys())
# for key in impact_dict_C['2.25'].keys():
#     for key1 in impact_dict_C['2.25'][key].keys():
#         C_arr_imp = []
#         C_arr_efa = []
#         H_arr_imp = []
#         H_arr_efa = []
#         Q_arr_imp = []
#         Q_arr_efa = []
#         for key2 in impact_dict_C['2.25'][key][key1]['0.006'].keys():
#             Efa_C = impact_dict_C['2.25'][key][key1]['0.006'][key2]['Efa']
#             Efa_H = impact_dict_H['2.25'][key][key1]['0.006'][key2]['Efa']
#             Efa_Q = impact_dict_Q['2.25'][key][key1][key2]['Efa']
#             impact_C = impact_dict_C['2.25'][key][key1]['0.006'][key2]['impact']
#             impact_H = impact_dict_H['2.25'][key][key1]['0.006'][key2]['impact']
#             impact_Q = impact_dict_Q['2.25'][key][key1][key2]['impact']
#             if(Efa_Q>365):Efa_Q = 365
#             if(Efa_H>365):Efa_H = 365
#             if(Efa_C>365):Efa_C = 365
#             print([impact_C,impact_H,impact_Q])
#             print([Efa_C,Efa_H,Efa_Q])
#             C_arr_efa.append(Efa_C)
#             H_arr_efa.append(Efa_H)
#             Q_arr_efa.append(Efa_Q)
#             C_arr_imp.append(impact_C)
#             H_arr_imp.append(impact_H)
#             Q_arr_imp.append(impact_Q)
#
#         plt.scatter(C_arr_efa, C_arr_imp,label ='C',marker='D')
#         plt.scatter( H_arr_efa,H_arr_imp,label ='H',marker='>')
#         plt.scatter(Q_arr_efa,Q_arr_imp,label ='Q',marker='<')
#         plt.xlabel("Efa ")
#         plt.ylabel("Impact")
#         plt.title("Impact vs Efa k2.0 ro:"+key+" eps:"+key1 )
#         plt.legend()
#         plt.show()


for key in impact_dict_C['2.0'].keys():
    C_arr_imp = []
    C_arr_efa = []
    H_arr_imp = []
    H_arr_efa = []
    Q_arr_imp = []
    Q_arr_efa = []
    for key1 in impact_dict_C['2.0'][key].keys():

        Efa_C = impact_dict_C['2.0'][key][key1]['0.006']['130']['Efa']
        Efa_H = impact_dict_H['2.0'][key][key1]['0.006']['130']['Efa']
        Efa_Q = impact_dict_Q['2.0'][key][key1]['130']['Efa']
        impact_C = impact_dict_C['2.0'][key][key1]['0.006']['130']['impact']
        impact_H = impact_dict_H['2.0'][key][key1]['0.006']['130']['impact']
        impact_Q = impact_dict_Q['2.0'][key][key1]['130']['impact']
        if(Efa_Q>365):Efa_Q = 365
        if(Efa_H>365):Efa_H = 365
        if(Efa_C>365):Efa_C = 365
        print([impact_C,impact_H,impact_Q])
        print([Efa_C,Efa_H,Efa_Q])
        C_arr_efa.append(Efa_C)
        H_arr_efa.append(Efa_H)
        Q_arr_efa.append(Efa_Q)
        C_arr_imp.append(impact_C)
        H_arr_imp.append(impact_H)
        Q_arr_imp.append(impact_Q)

    plt.scatter(C_arr_efa, C_arr_imp,label ='C',marker='D')
    plt.scatter( H_arr_efa,H_arr_imp,label ='H',marker='>')
    plt.scatter(Q_arr_efa,Q_arr_imp,label ='Q',marker='<')
    plt.xlabel("Efa ")
    plt.ylabel("Impact")
    plt.title("Impact vs Efa k2.0 ro:"+key+" del130")
    plt.legend()
    plt.show()
