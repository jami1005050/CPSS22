import pandas as pd

from utility.constant import *

# det_l1_add = pd.read_csv('../detection_test/det_SA_L1_add.csv')
det_l1_ded = pd.read_csv('../detection_test/det_SA_L1_ded.csv')
# det_l2_add = pd.read_csv('../detection_test/det_SA_L2_add.csv')
det_l2_ded = pd.read_csv('../detection_test/det_SA_L2_ded.csv')
# sal1 = pd.read_csv('../../robust/tau_generation_OPT_BETA/SA_tau_L1.csv')
# sal2 = pd.read_csv('../../robust/tau_generation_OPT_BETA/SA_tau_L2.csv')
attack_start_day = 273
attack_end_day = 365
number_of_meters = 192
number_of_reports = 24
# result_array = []
# for index,row in det_l1_add.iterrows():
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
# tau_result_frame.to_csv('impact_SA_L1_add.csv')
#
result_array = []
for index, row in det_l1_ded.iterrows():
    days_undetected = 0
    if (row.day_detected > attack_start_day):
        days_undetected = row.day_detected - attack_start_day
    else:
        days_undetected = attack_end_day - attack_start_day

    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,
                'ro_max':row.ro_max,'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_SA_L1_ded.csv')

# result_array = []
# for index, row in det_l2_add.iterrows():
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
# tau_result_frame.to_csv('impact_SA_L2_add.csv')

result_array = []
for index, row in det_l2_ded.iterrows():
    days_undetected = 0
    if (row.day_detected >= attack_start_day):
        days_undetected = row.day_detected - attack_start_day + 1
    else:
        days_undetected = attack_end_day - attack_start_day

    impact = row.del_avg_te * row.ro_mal * number_of_meters * E * days_undetected * number_of_reports / 1000
    object_c = {"epsilon": row.epsilon, 'del_avg_te': row.del_avg_te, 'ro_mal': row.ro_mal, 'efa': row.efa,'ro_max':row.ro_max,
                'type': 'ded', 'impact': impact}
    result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('impact_SA_L2_ded.csv')