from utility.common import*

tau_frame = pd.read_csv('RA_tau_DEL150_ROMAL03.csv')
# print(tau_frame.tau_min_c.unique())
attack_start_date = 60
attack_end_date = 273
result = []
for index, row in tau_frame.iterrows():
    #Now check with the benign Test set residual
    #As a cross validation set we can consider 6 months of data
    test_residual_benign = pd.read_csv('Test_RUC_Benign.csv')
    test_residual_attack = pd.read_csv('Test_RUC_kappa2.0_TE_Del_175_RO_0.3_M3M9.csv') #ROMAL 30%
    cv_residual_benign = test_residual_benign[(test_residual_benign['day']>=60) & (test_residual_benign['day'] <= 273)]
    cv_residual_attack = test_residual_attack[(test_residual_benign['day']>=60) & (test_residual_benign['day'] <= 273)]
    #CAUCHY
    false_alarm_c = testing_EFA(cv_residual_benign, row.tau_max_c, row.tau_min_c)
    tier1_anomaly_c, tier2_for_org_c, first_detected_org_c, false_alarm_ca = testing_tau(cv_residual_attack,row.tau_max_c, row.tau_min_c)

    #HUBER
    false_alarm_h = testing_EFA(cv_residual_benign, row.tau_max_h, row.tau_min_h)
    tier1_anomaly_h, tier2_for_org_h, first_detected_org_h, false_alarm_ha = testing_tau(cv_residual_attack,row.tau_max_h, row.tau_min_h)
    missed_detection_c = 0
    missed_detection_h = 0
    # print(first_detected_org_c,' ',first_detected_org_h)
    if(first_detected_org_c == 0):
        missed_detection_c = attack_end_date - attack_start_date
    else:
        missed_detection_c = first_detected_org_c - attack_start_date

    if(first_detected_org_h == 0):
        missed_detection_h = attack_end_date - attack_start_date
    else:
        missed_detection_h = first_detected_org_h - attack_start_date

    object_fm = {"beta_p":row.beta_p,'beta_n':row.beta_n,
                 'tau_max_c':row.tau_max_c,'tau_min_c':row.tau_min_c,
                 'fa_c':len(false_alarm_c),'md_c':missed_detection_c,
                 'tau_max_h':row.tau_max_h,'tau_min_h':row.tau_min_h,
                 'fa_h':len(false_alarm_h),'md_h':missed_detection_h}
    result.append(object_fm)
fm_result_frame = pd.DataFrame(result)
fm_result_frame.to_csv('RA_FA_MD_DEL150_ROMAL03_CR_DEL_175.csv')