from utility.common import *
from tqdm import tqdm
dataframe_tau_l1 = pd.read_csv('../../robust/tau_generation_OPT_BETA/SA_tau_L1.csv')
dataframe_tau_l2 = pd.read_csv('../../robust/tau_generation_OPT_BETA/SA_tau_L2.csv')

# result_array = []
# for index,row in dataframe_tau_l1.iterrows():
#     for del_evg_te in DEL_AVG_ARRAY_ADD_TE:
#         for ro_mal in RO_MAL_ARRAY:
#             res_frame = pd.read_csv(
#                 '../../data/test_RUC_OPT_BETA/ruc_EA/Test_RUC_TE_'+str(del_evg_te)+'_RO_'+str(ro_mal)+'addM10M12.csv')
#             tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame,row.tau_max, row.tau_min)
#
#             S_QC = 0
#             if(len(false_alarm_ca)>0):
#                 for i in range(len(false_alarm_ca)):
#                     if (i == 0):
#                         S_QC += false_alarm_ca[i] - 1
#                         continue
#                     S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
#                     # print(S_Q)
#                     i += 1
#                 S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
#             object_c = {"epsilon": row.epsilon, 'del_avg_te': del_evg_te,'ro_mal':ro_mal,'efa':S_QC,'ro_max':row.ro_max,
#                         'type':'add','tau_max': row.tau_max, 'tau_min': row.tau_min,'day_detected':first_detected_org_c}
#             result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('det_SA_L1_add.csv')
#
result_array = []
for index, row in tqdm(dataframe_tau_l1.iterrows(),desc='progress l1'):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        for ro_mal in RO_MAL_ARRAY:
            res_frame = pd.read_csv(
                '../../data/test_RUC_OPT_BETA/test_RUC_SA/Test_RUC_TE_' + str(del_evg_te) + '_RO_' + str(
                    ro_mal) + 'dedM1M3.csv')
            tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
                                                                                                 row.tau_min)

            S_QC = 0
            if (len(false_alarm_ca) > 0):
                for i in range(len(false_alarm_ca)):
                    if (i == 0):
                        S_QC += false_alarm_ca[i] - 1
                        continue
                    S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
                    # print(S_Q)
                    i += 1
                S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
            object_c = {"epsilon": row.epsilon, 'del_avg_te': del_evg_te, 'ro_mal': ro_mal, 'efa': S_QC,'ro_max':row.ro_max,
                        'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min,
                        'day_detected': first_detected_org_c}
            result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_SA_L1_ded_12_03_21_M1M3.csv')

# result_array = []
# for index, row in dataframe_tau_l2.iterrows():
#     for del_evg_te in DEL_AVG_ARRAY_ADD_TE:
#         for ro_mal in RO_MAL_ARRAY:
#             res_frame = pd.read_csv(
#                 '../../data/test_RUC_OPT_BETA/ruc_EA/Test_RUC_TE_' + str(del_evg_te) + '_RO_' + str(
#                     ro_mal) + 'addM10M12.csv')
#             tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
#                                                                                                  row.tau_min)
#
#             S_QC = 0
#             if (len(false_alarm_ca) > 0):
#                 for i in range(len(false_alarm_ca)):
#                     if (i == 0):
#                         S_QC += false_alarm_ca[i] - 1
#                         continue
#                     S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
#                     # print(S_Q)
#                     i += 1
#                 S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
#             object_c = {"epsilon": row.epsilon, 'del_avg_te': del_evg_te, 'ro_mal': ro_mal, 'efa': S_QC,'ro_max':row.ro_max,
#                         'type': 'add', 'tau_max': row.tau_max, 'tau_min': row.tau_min,
#                         'day_detected': first_detected_org_c}
#             result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('det_SA_L2_add.csv')

result_array = []
for index, row in tqdm(dataframe_tau_l2.iterrows(),desc='progress l2'):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        for ro_mal in RO_MAL_ARRAY:
            res_frame = pd.read_csv(
                '../../data/test_RUC_OPT_BETA/test_RUC_SA/Test_RUC_TE_' + str(del_evg_te) + '_RO_' + str(
                    ro_mal) + 'dedM1M3.csv')
            tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
                                                                                                 row.tau_min)

            S_QC = 0
            if (len(false_alarm_ca) > 0):
                for i in range(len(false_alarm_ca)):
                    if (i == 0):
                        S_QC += false_alarm_ca[i] - 1
                        continue
                    S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
                    # print(S_Q)
                    i += 1
                S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
            object_c = {"epsilon": row.epsilon, 'del_avg_te': del_evg_te, 'ro_mal': ro_mal, 'efa': S_QC,'ro_max':row.ro_max,
                        'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min,
                        'day_detected': first_detected_org_c}
            result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_SA_L2_ded_12_03_21_M1M3.csv')
