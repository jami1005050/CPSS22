import os
from utility.common import *
from tqdm import tqdm
# dataframe_add_Q_H = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_H_Q_add.csv')
dataframe_ded_Q_H = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_HQ_ded_12_03_21.csv')
# dataframe_add_NQ_H = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_H_NQ_add.csv')
dataframe_ded_NQ_H = pd.read_csv('../../robust/tau_generation_OPT_BETA/RA_tau_OB_HNQ_ded_12_03_21.csv')
testing_residual_benign = pd.read_csv("../../data/test_ruc/test_residuals/Test_RUC_Benign.csv")  # 91-181

# result_array = []
# for index,row in dataframe_add_Q_H.iterrows():
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
# tau_result_frame.to_csv('det_RA_Q_H_add.csv')

result_array = []
for index, row in tqdm(dataframe_ded_Q_H.iterrows(),desc='progress QH'):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        file_exists = os.path.exists(
            '../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM4M6.csv')
        if (file_exists == False): continue
        res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM4M6.csv')
        tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
                                                                                             row.tau_min)

        fa_C = testing_EFA(testing_residual_benign, row.tau_max, row.tau_min)
        efa_QC = 365
        if (len(fa_C) > 1):
            T_btw_FA = 0
            for i in range(len(fa_C)):
                if (i == 0):
                    T_btw_FA += fa_C[i] - 1
                    continue
                T_btw_FA += fa_C[i] - fa_C[i - 1]
                i += 1
            T_btw_FA += 365 - fa_C[len(fa_C) - 1]
            efa_QC = T_btw_FA / (len(fa_C) - 1)

        object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te, 'ro_mal': row.ro_mal, 'efa': efa_QC,
                    'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min, 'day_detected': first_detected_org_c}
        result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_RA_QH_ded_12_03_21_M4M6.csv')

# result_array = []
# for index, row in dataframe_add_NQ_H.iterrows():
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
# tau_result_frame.to_csv('det_RA_NQ_H_add.csv')

result_array = []
for index, row in tqdm(dataframe_ded_NQ_H.iterrows(),desc='progress for NQH: '):
    for del_evg_te in DEL_AVG_ARRAY_DED_TE:
        file_exists = os.path.exists(
            '../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM4M6.csv')
        if (file_exists == False): continue
        res_frame = pd.read_csv('../../data/test_RUC_OPT_BETA/test_RUC_RA/Test_RUC_TR' + str(int(row.del_avg)) + '_TE_' +
                                str(del_evg_te) + '_RO_' + str(row.ro_mal) + 'dedM4M6.csv')
        tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(res_frame, row.tau_max,
                                                                                             row.tau_min)

        fa_C = testing_EFA(testing_residual_benign, row.tau_max, row.tau_min)
        efa_QC = 365
        if (len(fa_C) > 1):
            T_btw_FA = 0
            for i in range(len(fa_C)):
                if (i == 0):
                    T_btw_FA += fa_C[i] - 1
                    continue
                T_btw_FA += fa_C[i] - fa_C[i - 1]
                i += 1
            T_btw_FA += 365 - fa_C[len(fa_C) - 1]
            efa_QC = T_btw_FA / (len(fa_C) - 1)

        object_c = {"del_avg_tr": row.del_avg, 'del_avg_te': del_evg_te, 'ro_mal': row.ro_mal, 'efa': efa_QC,
                    'type': 'ded', 'tau_max': row.tau_max, 'tau_min': row.tau_min, 'day_detected': first_detected_org_c}
        result_array.append(object_c)

tau_result_frame = pd.DataFrame(result_array)
tau_result_frame.to_csv('det_RA_NQH_ded_12_03_21_M4M6.csv')