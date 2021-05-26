#Plot benign Comparison
import matplotlib.pyplot as plt
import json
import pandas as pd

SMALL_SIZE = 12
MEDIUM_SIZE = 20
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #
f_C = open('../test_C/impact_poisoned_C_K2.json' )
f_H = open('../test_H/impact_poisoned_H_K2.json' )
f_Q = open('../test_QP/impact_poisoned_Q_k2.json' )
impact_dict_C = json.load(f_C)
impact_dict_H = json.load(f_H)
impact_dict_Q = json.load(f_Q)
result = []
for key in impact_dict_C.keys():
    for key1 in impact_dict_C[key].keys():
        # print(impact_dict_C[key][key1].keys())
        for key2 in impact_dict_C[key1]['0.006'].keys():
            Efa_C = impact_dict_C[key][key1]['0.006'][key2]['Efa']
            Efa_H = impact_dict_H[key][key1]['0.006'][key2]['Efa']
            Efa_Q = impact_dict_Q[key][key1][key2]['Efa']
            impact_C = impact_dict_C[key][key1]['0.006'][key2]['impact']
            impact_H = impact_dict_H[key][key1]['0.006'][key2]['impact']
            impact_Q = impact_dict_Q[key][key1][key2]['impact']
            if(Efa_Q>365):Efa_Q = 365
            if(Efa_H>365):Efa_H = 365
            if(Efa_C>365):Efa_C = 365
            temp = {'romax':key,'epsilon':key1,'del_avg':key2,'impact_C':impact_C,
                    'impact_Q':impact_Q,'impact_H':impact_H,'Efa_Q':Efa_Q,'Efa_C':Efa_C,'Efa_H':Efa_H}
            result.append(temp)


result_frame = pd.DataFrame(result)
print(result_frame)


