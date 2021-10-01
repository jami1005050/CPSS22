import json
from utility.common import *
f = open('../result/standard_limit/robust_H_non_Q_RA.json')
poisoning_std_limits = json.load(f)
result = {}
testing_residualM4M6 = pd.read_csv("../../data/Test_RUC_Benign.csv")  # 91-181
for key2 in poisoning_std_limits.keys(): # del
    result[key2] = {}
    for key3 in poisoning_std_limits[key2].keys(): #beta
        result[key2][key3] = {}
        false_alarm = testing_EFA(testing_residualM4M6,poisoning_std_limits[key2][key3]['tau_max'],
                                                        poisoning_std_limits[key2][key3]['tau_min'])
        result[key2][key3]['false_alarm'] = false_alarm


with open("../result/false_alarm/fa_NQHRA.json", "w") as outfile:
    json.dump(result, outfile)
