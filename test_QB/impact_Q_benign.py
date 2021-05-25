import json
import sys

from utility.common import *

number_of_meters = 192
attack_start_day = 91
attack_end_day = 181
number_of_reports = 24
ro_mal = .3

f = open('detection_benign_Q.json' )
poisoning_std_limits = json.load(f)
result = {}
for key1 in poisoning_std_limits.keys(): #kappa
    result[key1] = {}
    for key2 in poisoning_std_limits[key1].keys(): #delavg
        result[key1][key2] = {}
        first_detected = poisoning_std_limits[key1][key2]['first_detected']
        false_alarm = poisoning_std_limits[key1][key2]['false_alarm']
        days_undetected = first_detected - attack_start_day
        result[key1][key2]['days_undetected'] = days_undetected
        if(len(false_alarm)>1):
            T_btw_FA = 0
            for i in range(len(false_alarm)):
                if (i == 0):
                    T_btw_FA += false_alarm[i] - 1
                    continue
                T_btw_FA += false_alarm[i] - false_alarm[i - 1]
                i += 1
            T_btw_FA += 365 - false_alarm[len(false_alarm) - 1]
            result[key1][key2]['Efa'] = T_btw_FA / (len(false_alarm) - 1)
        else:
            result[key1][key2]['Efa'] = sys.maxsize
        result[key1][key2]['impact'] = int(key2) * ro_mal * number_of_meters * E * days_undetected*number_of_reports/1000

with open("impact_benign_Q.json", "w") as outfile:
    json.dump(result, outfile)
