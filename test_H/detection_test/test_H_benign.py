import json
from utility.common import *
f = open('../result/standard_limit/robust_benign_H.json')
poisoning_std_limits = json.load(f)
result = {}
for key1 in poisoning_std_limits.keys(): #kappa
    result[key1] = {}
    for key2 in poisoning_std_limits[key1].keys(): # beta
        result[key1][key2] = {}
        for del_avg in DEL_AVG_ARRAY_DED:
            testing_residualM4M6 = pd.read_csv("../data/test_residuals_cleaned/Test_RUC_K_mad_"+str(key1)+"_D"+str(del_avg)+"_M4M6.csv") #91-181
            result[key1][key2][del_avg] = {}
            tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,
                                                                                     poisoning_std_limits[key1][key2]['tau_max'],
                                                                                     poisoning_std_limits[key1][key2]['tau_min'])
            result[key1][key2][del_avg] ['tier1'] = tier1_anomaly
            result[key1][key2][del_avg] ['tier2'] = tier2_for_org
            result[key1][key2][del_avg] ['first_detected'] = first_detected_org
            result[key1][key2][del_avg] ['false_alarm'] = false_alarm


with open("../result/detection/detection_benign_H.json", "w") as outfile:
    json.dump(result, outfile)
