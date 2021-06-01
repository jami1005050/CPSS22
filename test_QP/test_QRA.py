import json
from utility.common import *
f = open('poison_RA.json' )
poisoning_std_limits = json.load(f)
result = {}
for key2 in poisoning_std_limits.keys(): # romax
    result[key2] = {}
    for key3 in poisoning_std_limits.keys(): #epsilon
        result[key2][key3] = {}
        testing_residualM4M6 = pd.read_csv("../data/test_residual_random_attack/Test_RUC_PWith_"+str(key2)+"Del_"+str(key3)+"_M7M9.csv") #91-181
        result[key2][key3] = {}
        tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,
                                                                                 poisoning_std_limits[key3]['tau_max'],
                                                                                 poisoning_std_limits[key3]['tau_min'])
        result[key2][key3]['tier1'] = tier1_anomaly
        result[key2][key3]['tier2'] = tier2_for_org
        result[key2][key3]['first_detected'] = first_detected_org
        result[key2][key3]['false_alarm'] = false_alarm


with open("detection_poisoned_QRA.json", "w") as outfile:
    json.dump(result, outfile)
