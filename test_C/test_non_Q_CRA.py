import json
from utility.common import *
f = open('robust_C_non_Q_RA.json')
poisoning_std_limits = json.load(f)
result = {}
for key2 in poisoning_std_limits.keys(): # del
    result[key2] = {}
    for key3 in poisoning_std_limits.keys(): #del
        result[key2][key3] = {}
        for key4 in poisoning_std_limits[key3].keys(): #beta
            result[key2][key3][key4] = {}
            testing_residualM4M6 = pd.read_csv("../data/test_residual_random_attack/Test_RUC_PWith_" + str(key2) + "Del_" + str(key3) + "_M7M9.csv")  # 182-273
            result[key2][key3][key4] = {}
            tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,
                                                                                     poisoning_std_limits[key3][key4]['tau_max'],
                                                                                     poisoning_std_limits[key3][key4]['tau_min'])
            result[key2][key3][key4]['tier1'] = tier1_anomaly
            result[key2][key3][key4]['tier2'] = tier2_for_org
            result[key2][key3][key4]['first_detected'] = first_detected_org
            result[key2][key3][key4]['false_alarm'] = false_alarm


with open("detection_poisoned_CRA_non_Q.json", "w") as outfile:
    json.dump(result, outfile)
