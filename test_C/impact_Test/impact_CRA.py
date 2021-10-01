import json
import sys

from utility.common import *

number_of_meters = 192
attack_start_day = 182
attack_end_day = 273
number_of_reports = 24
ro_mal = .3

f = open('../result_data/detection/detection_poisoned_CRA_small_step_del.json')
poisoning_std_limits = json.load(f)
result = {}

for key2 in poisoning_std_limits.keys(): # del
    result[key2] = {}
    # for key3 in poisoning_std_limits.keys(): #del
    for key3 in poisoning_std_limits[key2].keys(): #del use for small step del
        result[key2][key3] = {}
        for key4 in poisoning_std_limits[key2][key3].keys(): #beta
            result[key2][key3][key4] = {}
            first_detected = poisoning_std_limits[key2][key3][key4]['first_detected']
            false_alarm = poisoning_std_limits[key2][key3][key4]['false_alarm']
            if(first_detected>attack_start_day):
                days_undetected = first_detected - attack_start_day
            else:
                days_undetected = attack_end_day - attack_start_day
            result[key2][key3][key4]['days_undetected'] = days_undetected
            if(len(false_alarm)>1):
                T_btw_FA = 0
                for i in range(len(false_alarm)):
                    if (i == 0):
                        T_btw_FA += false_alarm[i] - 1
                        continue
                    T_btw_FA += false_alarm[i] - false_alarm[i - 1]
                    i += 1
                T_btw_FA += 365 - false_alarm[len(false_alarm) - 1]
                result[key2][key3][key4]['Efa'] = T_btw_FA / (len(false_alarm) - 1)
            else:
                result[key2][key3][key4]['Efa'] = sys.maxsize
            result[key2][key3][key4]['impact'] = int(key3) * ro_mal * number_of_meters * E * days_undetected*number_of_reports/1000

with open("../result_data/impact/impact_poisoned_CRA_small_step_del.json", "w") as outfile:
    json.dump(result, outfile)
