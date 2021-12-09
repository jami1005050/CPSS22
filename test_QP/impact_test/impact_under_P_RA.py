import pandas as pd

from utility.constant import *

# det_l1_add = pd.read_csv('../detection_test/det_RA_L1_add.csv')
det_l1_ded = pd.read_csv('../detection_test/det_RA_L1_ded_12_03_21_M4M6.csv')
# det_l2_add = pd.read_csv('../detection_test/det_RA_L2_add.csv')
det_l2_ded = pd.read_csv('../detection_test/det_RA_L2_ded_12_03_21_M4M6.csv')
attack_start_day = 91
attack_end_day = 181
number_of_meters = 192
number_of_reports = 24
# temp = pd.DataFrame()
# temp['v'] = det_l2_ded[det_l2_ded['day_detected']>0]['day_detected'] - det_l1_ded[det_l2_ded['day_detected']>0]['day_detected']
# print(temp[temp['v']!=0])
# result_array = []
# for index,row in det_l1_add.iterrows():
#     days_undetected = 0
#     if (row.day_detected > attack_start_day):
#         days_undetected = row.day_detected - attack_start_day
#     else:
#         days_undetected = attack_end_day - attack_start_day
#
#     impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
#     object_c = {"del_avg_tr": row.del_avg_tr, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
#                 'type': 'add',  'impact': impact}
#     result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('impact_RA_L1_add.csv')
#
result_array = []
for index, row in det_l1_ded.iterrows():
    days_undetected = 0

    if (row.day_detected >= attack_start_day):
        days_undetected = row.day_detected - attack_start_day+1
    else:
        days_undetected = attack_end_day - attack_start_day
    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    # if(index == 630):
    #     print("L2: ",impact,days_undetected,row.del_avg_te,row.ro_mal)
    object_c = {"del_avg_tr": row.del_avg_tr, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
                'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_RA_L1_ded_12_03_21_M4M6.csv')
#
# result_array = []
# for index, row in det_l2_add.iterrows():
#     days_undetected = 0
#     if (row.day_detected > attack_start_day):
#         days_undetected = row.day_detected - attack_start_day
#     else:
#         days_undetected = attack_end_day - attack_start_day
#
#     impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
#     object_c = {"del_avg_tr": row.del_avg_tr, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
#                 'type': 'add', 'impact': impact}
#     result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('impact_RA_L2_add.csv')
#
result_array = []
for index, row in det_l2_ded.iterrows():
    days_undetected = 0
    if (row.day_detected > attack_start_day):
        days_undetected = row.day_detected - attack_start_day
    else:
        days_undetected = attack_end_day - attack_start_day

    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    # if (index == 630):
    #     print("L2: ",impact,days_undetected,row.del_avg_te,row.ro_mal)
    object_c = {"del_avg_tr": row.del_avg_tr, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
                'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_RA_L2_ded_12_03_21_M4M6.csv')