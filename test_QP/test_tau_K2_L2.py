import json
from utility.common import *
f = open('poison_tau_K2_L2.json' )
poisoning_std_limits = json.load(f)
result = {}

for key2 in poisoning_std_limits.keys(): # romax
    result[key2] = {}
    for key3 in poisoning_std_limits[key2].keys(): #epsilon
        result[key2][key3] = {}
        # for del_avg in DEL_AVG_ARRAY_DED:
        for del_avg in DEL_AVG_ARRAY_DED_TE:#for small scale del step
            # testing_residualM4M6 = pd.read_csv("../data/test_residuals_cleaned/Test_RUC_K_mad_2.0_D"+str(del_avg)+"_M4M6.csv") #91-181
            testing_residualM4M6 = pd.read_csv("../data/test_residual_small_step_del/Test_RUC_kappa_2.0Del_"+str(del_avg)+"_M7M9.csv") #91-181
            result[key2][key3][del_avg] = {}
            tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,
                                                                                     poisoning_std_limits[key2][key3]['tau_max'],
                                                                                     poisoning_std_limits[key2][key3]['tau_min'])
            result[key2][key3][del_avg] ['tier1'] = tier1_anomaly
            result[key2][key3][del_avg] ['tier2'] = tier2_for_org
            result[key2][key3][del_avg] ['first_detected'] = first_detected_org
            result[key2][key3][del_avg] ['false_alarm'] = false_alarm



with open("detection_poisoned_QK2_L2_small_step_del.json", "w") as outfile:
    json.dump(result, outfile)
