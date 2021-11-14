import json
from utility.common import *
f = open('../../result/standard_limit/poison_tau_K2.json')
poisoning_std_limits = json.load(f)
result = {}
testing_residualM4M6 = pd.read_csv("../../../data/test_ruc/test_residuals/Test_RUC_Benign.csv")  # 91-181

for key2 in poisoning_std_limits.keys(): # romax
    result[key2] = {}
    for key3 in poisoning_std_limits[key2].keys(): #epsilon
        result[key2][key3] = {}
        result[key2][key3] = {}
        false_alarm = testing_EFA(testing_residualM4M6,poisoning_std_limits[key2][key3]['tau_max'],
                                                    poisoning_std_limits[key2][key3]['tau_min'])
        result[key2][key3] ['false_alarm'] = false_alarm


with open("../../result/false_alarm/FA_Q.json", "w") as outfile:
    json.dump(result, outfile)
