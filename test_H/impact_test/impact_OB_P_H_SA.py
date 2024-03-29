import pandas as pd

from utility.constant import *

# det_Q_add = pd.read_csv('../detection_test/det_SA_Q_H_add.csv')
det_Q_ded = pd.read_csv('../detection_test/det_SA_QH_ded_12_03_21_M4M6.csv')
# det_NQ_add = pd.read_csv('../detection_test/det_SA_NQ_H_add.csv')
det_NQ_ded = pd.read_csv('../detection_test/det_SA_NQH_ded_12_03_21_M4M6.csv')
attack_start_day = 91
attack_end_day = 181
number_of_meters = 192
number_of_reports = 24
#
# result_array = []
# for index,row in det_Q_add.iterrows():
#     days_undetected = 0
#     if (row.day_detected > attack_start_day):
#         days_undetected = row.day_detected - attack_start_day
#     else:
#         days_undetected = attack_end_day - attack_start_day
#
#     impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
#     object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
#                 'ro_max':row.ro_max,'type': 'add',  'impact': impact}
#     result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('impact_SA_Q_H_add.csv')

result_array = []
for index, row in det_Q_ded.iterrows():
    days_undetected = 0
    if (row.day_detected >= attack_start_day):
        days_undetected = row.day_detected - attack_start_day + 1
    else:
        days_undetected = attack_end_day - attack_start_day

    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
                'ro_max':row.ro_max,'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_SA_QH_ded_12_03_21_M4M6.csv')

# result_array = []
# for index, row in det_NQ_add.iterrows():
#     days_undetected = 0
#     if (row.day_detected > attack_start_day):
#         days_undetected = row.day_detected - attack_start_day
#     else:
#         days_undetected = attack_end_day - attack_start_day
#
#     impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
#     object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
#                 'ro_max':row.ro_max,'type': 'add', 'impact': impact}
#     result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('impact_SA_NQ_H_add.csv')

result_array = []
for index, row in det_NQ_ded.iterrows():
    days_undetected = 0
    if (row.day_detected >= attack_start_day):
        days_undetected = row.day_detected - attack_start_day + 1
    else:
        days_undetected = attack_end_day - attack_start_day

    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
                'ro_max':row.ro_max,'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_SA_NQH_ded_12_03_21_M4M6.csv')