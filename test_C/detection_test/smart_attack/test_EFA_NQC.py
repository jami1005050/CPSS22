import json
from utility.common import *
f = open('../../result_data/standard_limit/robust_poison_C_non_Q_K2.json')
poisoning_std_limits = json.load(f)
result = {}
testing_residualM4M6 = pd.read_csv("../../../data/Test_RUC_Benign.csv")  # 91-181
for key2 in poisoning_std_limits.keys(): # romax
    result[key2] = {}
    for key3 in poisoning_std_limits[key2].keys(): #epsilon
        result[key2][key3] = {}
        for key4 in poisoning_std_limits[key2][key3].keys(): #beta
            result[key2][key3][key4] = {}
            false_alarm = testing_EFA(testing_residualM4M6,poisoning_std_limits[key2][key3][key4]['tau_max'],
                                        poisoning_std_limits[key2][key3][key4]['tau_min'])
            result[key2][key3][key4]['false_alarm'] = false_alarm

with open("../../result_data/false_alarm/FA_NQC.json", "w") as outfile:
    json.dump(result, outfile)
