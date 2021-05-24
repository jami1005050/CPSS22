import json
from utility.common import *
tau_dict = {1.0:{'tau_max': 0.005, 'tau_min': -0.0038691378044811986},
            1.25:{ 'tau_max': 0.0025, 'tau_min': -0.0029683815875770903},
            1.5:{ 'tau_max': 0.0025, 'tau_min': -0.004567625370672981},
            1.75:{ 'tau_max': 0.0075, 'tau_min': -0.006166869153768871},
            2.0: {'tau_max': 0.0125, 'tau_min': -0.012766112936864759},
            2.25:{ 'tau_max': 0.0125, 'tau_min': -0.01186535671996054},
            2.5:{ 'tau_max': 0.01, 'tau_min': -0.010964600503056431}}
result = {}
for key in tau_dict.keys():
    result[key] = {}
    for del_avg in DEL_AVG_ARRAY_DED:
        testing_residualM4M6 = pd.read_csv("../data/test_residuals_cleaned/Test_RUC_K_mad_"+str(key)+"_D"+str(del_avg)+"_M4M6.csv") #91-181
        result [key][del_avg] = {}
        tier1_anomaly,tier2_for_org,first_detected_org,false_alarm = testing_tau(testing_residualM4M6,tau_dict[key]['tau_max'],tau_dict[key]['tau_min'])
        result [key][del_avg] ['tier1'] = tier1_anomaly
        result [key][del_avg] ['tier2'] = tier2_for_org
        result [key][del_avg] ['first_detected'] = first_detected_org
        result [key][del_avg] ['false_alarm'] = false_alarm


with open("detection.json", "w") as outfile:
    json.dump(result, outfile)
