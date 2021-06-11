import json
from utility.common import *
f = open('robust_C_non_Q_ro_del_RA.json')
poisoning_std_limits = json.load(f)
result = {}
for key2 in poisoning_std_limits.keys(): # del
    result[key2] = {}
    if (key2 > str(175)): break
    for key3 in DEL_AVG_ARRAY_DED_TE: #del
        result[key2][key3] = {}
        for key4 in poisoning_std_limits[key2].keys(): #romal
            result[key2][key3][key4] = {}
            for key5 in poisoning_std_limits[key2][key4].keys(): #beta
                testing_residualM4M6 = pd.read_csv("../data/test_residual_ro_del_RA/Test_RUC_TR_Del"+
                                                   str(key2)+"_TE_Del_"+str(key3)+"_RO_"+str(key4)+"_M7M9.csv")  # 182-273
                result[key2][key3][key4][key5] = {}
                # tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,
                #                                                                          poisoning_std_limits[key3][key4]['tau_max'],
                #                                                                          poisoning_std_limits[key3][key4]['tau_min'])
                tier1_anomaly, tier2_for_org, first_detected_org, false_alarm = testing_tau(testing_residualM4M6,
                                                                                            poisoning_std_limits[key2][
                                                                                                key4][key5]['tau_max'],
                                                                                            poisoning_std_limits[key2][
                                                                                                key4][key5]['tau_min'])
                #remark use key3 when we are not using small step del avg changes in the system
                result[key2][key3][key4][key5]['tier1'] = tier1_anomaly
                result[key2][key3][key4][key5]['tier2'] = tier2_for_org
                result[key2][key3][key4][key5]['first_detected'] = first_detected_org
                result[key2][key3][key4][key5]['false_alarm'] = false_alarm


with open("detection_poisoned_ro_del_nonQ_CRA.json", "w") as outfile:
    json.dump(result, outfile)
