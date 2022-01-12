from utility.common import *
testing_residual_benign = pd.read_csv("../data/test_ruc/test_residuals/Test_RUC_Benign.csv")  # 91-181
def calculate_efa(tau_max,tau_min):
    fa_C = testing_EFA(testing_residual_benign, tau_max,tau_min)
    print(len(fa_C))
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
    return efa_QC
tau_max_l1,tau_min_l1 = 0.0125, -0.012766112936864703
tau_max_l2,tau_min_l2 =0.015, -0.015266112936864758
tau_max_QC,tau_min_QC = 0.00275,-0.002766112936864684
tau_max_QH,tau_min_QH = 0.0175,-0.017516112936864697
tau_max_NQC,tau_min_NQC = 0.00275,-0.002766112936864684
tau_max_NQH,tau_min_NQH = 0.00275,-0.002766112936864684
efa_l1 = calculate_efa(tau_max_l1,tau_min_l1)
efa_l2 = calculate_efa(tau_max_l2,tau_min_l2)
efa_QC = calculate_efa(tau_max_QC,tau_min_QC)
efa_QH = calculate_efa(tau_max_QH,tau_min_QH)
efa_NQC = calculate_efa(tau_max_NQC,tau_min_NQC)
efa_NQH = calculate_efa(tau_max_NQH,tau_min_NQH)
print('efa_l1: ',efa_l1,' efa_l2: ', efa_l2, ' efa_QC: ', efa_QC,' efa_QH: ',efa_QH,
      ' efa_NQC: ',efa_NQC,' efa_NQH: ',efa_NQH)