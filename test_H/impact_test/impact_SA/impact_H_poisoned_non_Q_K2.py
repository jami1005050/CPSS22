import json
import sys

from utility.common import *

number_of_meters = 192
attack_start_day = 182
attack_end_day = 273
number_of_reports = 24
ro_mal = .3

f = open('../../result/detection/detection_poisoned_H_non_Q_K2_small_step_del.json')
poisoning_std_limits = json.load(f)
result = {}

for key2 in poisoning_std_limits.keys(): # romax
    result[key2] = {}
    for key3 in poisoning_std_limits[key2].keys(): #epsilon
        result[key2][key3] = {}
        for key4 in poisoning_std_limits[key2][key3].keys(): #beta
            result[key2][key3][key4] = {}
            for key5 in poisoning_std_limits[key2][key3][key4].keys(): # del_avg
                result[key2][key3][key4][key5] = {}
                # print(poisoning_std_limits[key1][key2][key3][key4][key5])
                first_detected = poisoning_std_limits[key2][key3][key4][key5]['first_detected']
                false_alarm = poisoning_std_limits[key2][key3][key4][key5]['false_alarm']
                if(first_detected>attack_start_day):
                    days_undetected = first_detected - attack_start_day
                else:
                    days_undetected = attack_end_day - attack_start_day
                result[key2][key3][key4][key5]['days_undetected'] = days_undetected
                if(len(false_alarm)>1):
                    T_btw_FA = 0
                    for i in range(len(false_alarm)):
                        if (i == 0):
                            T_btw_FA += false_alarm[i] - 1
                            continue
                        T_btw_FA += false_alarm[i] - false_alarm[i - 1]
                        i += 1
                    T_btw_FA += 365 - false_alarm[len(false_alarm) - 1]
                    result[key2][key3][key4][key5]['Efa'] = T_btw_FA / (len(false_alarm) - 1)
                else:
                    result[key2][key3][key4][key5]['Efa'] = sys.maxsize
                if(key5 == str(10)):
                    print(days_undetected)
                    # print(int(key5) * ro_mal * number_of_meters * E * days_undetected*number_of_reports/1000)
                result[key2][key3][key4][key5]['impact'] = int(key5) * ro_mal * number_of_meters * E * days_undetected*number_of_reports/1000

with open("../../result/impact/impact_poisoned_H_non_Q_K2_small_step_del.json", "w") as outfile:
    json.dump(result, outfile)
