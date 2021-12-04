import os
from utility.common import *
from tqdm import tqdm
# dataframe_add_Q_C = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_C_Q_add.csv')
dataframe_ded_Q_C = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_CQ_ded_12_03_21.csv')
# dataframe_add_NQ_C = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_C_NQ_add.csv')
dataframe_ded_NQ_C = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_CNQ_ded_12_03_21.csv')

# result_array = []
# for index,row in dataframe_add_Q_C.iterrows():
#     for del_evg_te in DEL_AVG_ARRAY_ADD_TE:
#         file_exists = os.path.exists(
#             '../../data/test_RUC_OPT_BETA/additive/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
#             str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'addM10M12.csv')
#         if (file_exists == False): continue
#         res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/additive/Test_RUC_TR'+str(int(row.del_avg))+'_TE_'+
#                                 str(del_evg_te)+'_RO_'+str(row.ro_mal)+'addM10M12.csv')
#         tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame,row.tau_max, row.tau_min)
#
#         S_QC = 0
#         if(len(false_alarm_ca)>0):
#             for i in range(len(false_alarm_ca)):
#                 if (i == 0):
#                     S_QC += false_alarm_ca[i] - 1
#                     continue
#                 S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
#                 # print(S_Q)
#                 i += 1
#             S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
#         object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te,'ro_mal':row.ro_mal,'efa':S_QC,
#                     'type':'add','tau_max': row.tau_max, 'tau_min': row.tau_min,'day_detected':first_detected_org_c}
#         result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('det_RA_Q_C_add.csv')
#
result_array = []
for index, row in tqdm(dataframe_ded_Q_C.iterrows(),desc='progress QC'):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        file_exists = os.path.exists(
            '../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM1M3.csv')
        if (file_exists == False): continue
        res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM1M3.csv')
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
        object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te, 'ro_mal': row.ro_mal, 'efa': S_QC,
                    'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min, 'day_detected': first_detected_org_c}
        result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_RA_QC_ded_12_03_21_M1M3.csv')

# result_array = []
# for index, row in dataframe_add_NQ_C.iterrows():
#     for del_evg_te in DEL_AVG_ARRAY_ADD_TE:
#         file_exists = os.path.exists('../../data/test_RUC_OPT_BETA/additive/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
#                                 str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'addM10M12.csv')
#         if(file_exists == False):continue
#         res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/additive/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
#                                 str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'addM10M12.csv')
#
#         tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
#                                                                                              row.tau_min)
#
#         S_QC = 0
#         if (len(false_alarm_ca) > 0):
#             for i in range(len(false_alarm_ca)):
#                 if (i == 0):
#                     S_QC += false_alarm_ca[i] - 1
#                     continue
#                 S_QC += false_alarm_ca[i] - false_alarm_ca[i - 1]
#                 # print(S_Q)
#                 i += 1
#             S_QC += 365 - false_alarm_ca[len(false_alarm_ca) - 1]
#         object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te, 'ro_mal': row.ro_mal, 'efa': S_QC,
#                     'type': 'add', 'tau_max': row.tau_max, 'tau_min': row.tau_min, 'day_detected': first_detected_org_c}
#         result_array.append(object_c)
#
# tau_result_frame = pd.DataFrame(result_array)
# tau_result_frame.to_csv('det_RA_NQ_C_add.csv')

result_array = []
for index, row in tqdm(dataframe_ded_NQ_C.iterrows(),desc='progress for NQC'):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        file_exists = os.path.exists(
            '../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM1M3.csv')
        if (file_exists == False): continue
        res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM1M3.csv')
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
        object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te, 'ro_mal': row.ro_mal, 'efa': S_QC,
                    'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min, 'day_detected': first_detected_org_c}
        result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_RA_NQC_ded_12_03_21_M1M3.csv')