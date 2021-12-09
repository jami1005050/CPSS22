import pandas as pd
from functools import reduce

#region RA
impact_l1_ded_M4M6 = pd.read_csv('../test_QP/impact_test/impact_RA_L1_ded_12_03_21_M4M6.csv')
impact_l2_ded_M4M6 = pd.read_csv('../test_QP/impact_test/impact_RA_L2_ded_12_03_21_M4M6.csv')
impact_Q_C_ded_M4M6 = pd.read_csv('../test_C/impact_Test/impact_RA_QC_ded_12_03_21_M4M6.csv')
impact_NQ_C_ded_M4M6 = pd.read_csv('../test_C/impact_Test/impact_RA_NQC_ded_12_03_21_M4M6.csv')
impact_Q_H_ded_M4M6 = pd.read_csv('../test_H/impact_test/impact_RA_QH_ded_12_03_21_M4M6.csv')
impact_NQ_H_ded_M4M6 = pd.read_csv('../test_H/impact_test/impact_RA_NQH_ded_12_03_21_M4M6.csv')

impact_l1_ded_M7M9 = pd.read_csv('../test_QP/impact_test/impact_RA_L1_ded_12_03_21_M7M9.csv')
impact_l2_ded_M7M9 = pd.read_csv('../test_QP/impact_test/impact_RA_L2_ded_12_03_21_M7M9.csv')
impact_Q_C_ded_M7M9 = pd.read_csv('../test_C/impact_Test/impact_RA_QC_ded_12_03_21_M7M9.csv')
impact_NQ_C_ded_M7M9 = pd.read_csv('../test_C/impact_Test/impact_RA_NQC_ded_12_03_21_M7M9.csv')
impact_Q_H_ded_M7M9 = pd.read_csv('../test_H/impact_test/impact_RA_QH_ded_12_03_21_M7M9.csv')
impact_NQ_H_ded_M7M9 = pd.read_csv('../test_H/impact_test/impact_RA_NQH_ded_12_03_21_M7M9.csv')

impact_l1_ded_M10M12 = pd.read_csv('../test_QP/impact_test/impact_RA_L1_ded_12_03_21_M10M12.csv')
impact_l2_ded_M10M12 = pd.read_csv('../test_QP/impact_test/impact_RA_L2_ded_12_03_21_M10M12.csv')
impact_Q_C_ded_M10M12 = pd.read_csv('../test_C/impact_Test/impact_RA_QC_ded_12_03_21_M10M12.csv')
impact_NQ_C_ded_M10M12 = pd.read_csv('../test_C/impact_Test/impact_RA_NQC_ded_12_03_21_M10M12.csv')
impact_Q_H_ded_M10M12 = pd.read_csv('../test_H/impact_test/impact_RA_QH_ded_12_03_21_M10M12.csv')
impact_NQ_H_ded_M10M12 = pd.read_csv('../test_H/impact_test/impact_RA_NQH_ded_12_03_21_M10M12.csv')

impact_l1_ded_M4M12_arr = [impact_l1_ded_M4M6, impact_l1_ded_M7M9, impact_l1_ded_M10M12]
impact_l1_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_l1_ded_M4M12_arr)
impact_l1_ded_M4M12_Frame.to_csv('impact_RA_l1_ded_M4M12_Frame.csv')
impact_l2_ded_M4M12_arr = [impact_l2_ded_M4M6, impact_l2_ded_M7M9, impact_l2_ded_M10M12]
impact_l2_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_l2_ded_M4M12_arr)
impact_l2_ded_M4M12_Frame.to_csv('impact_RA_l2_ded_M4M12_Frame.csv')

impact_Q_C_ded_M4M12_arr = [impact_Q_C_ded_M4M6, impact_Q_C_ded_M7M9, impact_Q_C_ded_M10M12]
impact_Q_C_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_Q_C_ded_M4M12_arr)
impact_Q_C_ded_M4M12_Frame.to_csv('impact_RA_QC_ded_M4M12_Frame.csv')

impact_NQ_C_ded_M4M12_arr = [impact_NQ_C_ded_M4M6, impact_NQ_C_ded_M7M9, impact_NQ_C_ded_M10M12]
impact_NQ_C_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_NQ_C_ded_M4M12_arr)
impact_NQ_C_ded_M4M12_Frame.to_csv('impact_RA_NQC_ded_M4M12_Frame.csv')

impact_Q_H_ded_M4M12_arr = [impact_Q_H_ded_M4M6, impact_Q_H_ded_M7M9, impact_Q_H_ded_M10M12]
impact_Q_H_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_Q_H_ded_M4M12_arr)
impact_Q_H_ded_M4M12_Frame.to_csv('impact_RA_QH_ded_M4M12_Frame.csv')

impact_NQ_H_ded_M4M12_arr = [impact_NQ_H_ded_M4M6, impact_NQ_H_ded_M7M9, impact_NQ_H_ded_M10M12]
impact_NQ_H_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['del_avg_tr','del_avg_te','ro_mal']), impact_NQ_H_ded_M4M12_arr)
impact_NQ_H_ded_M4M12_Frame.to_csv('impact_RA_NQH_ded_M4M12_Frame.csv')


#endregion

#region SA
impact_l1_ded_SA_M4M6 = pd.read_csv('../test_QP/impact_test/impact_SA_L1_ded_12_03_21_M4M6.csv')
impact_l2_ded_SA_M4M6 = pd.read_csv('../test_QP/impact_test/impact_SA_L2_ded_12_03_21_M4M6.csv')
impact_Q_C_ded_SA_M4M6 = pd.read_csv('../test_C/impact_Test/impact_SA_QC_ded_12_03_21_M4M6.csv')
impact_NQ_C_ded_SA_M4M6 = pd.read_csv('../test_C/impact_Test/impact_SA_NQC_ded_12_03_21_M4M6.csv')
impact_Q_H_ded_SA_M4M6 = pd.read_csv('../test_H/impact_test/impact_SA_QH_ded_12_03_21_M4M6.csv')
impact_NQ_H_ded_SA_M4M6 = pd.read_csv('../test_H/impact_test/impact_SA_NQH_ded_12_03_21_M4M6.csv')

impact_l1_ded_SA_M7M9 = pd.read_csv('../test_QP/impact_test/impact_SA_L1_ded_12_03_21_M7M9.csv')
impact_l2_ded_SA_M7M9 = pd.read_csv('../test_QP/impact_test/impact_SA_L2_ded_12_03_21_M7M9.csv')
impact_Q_C_ded_SA_M7M9 = pd.read_csv('../test_C/impact_Test/impact_SA_QC_ded_12_03_21_M7M9.csv')
impact_NQ_C_ded_SA_M7M9 = pd.read_csv('../test_C/impact_Test/impact_SA_NQC_ded_12_03_21_M7M9.csv')
impact_Q_H_ded_SA_M7M9 = pd.read_csv('../test_H/impact_test/impact_SA_QH_ded_12_03_21_M7M9.csv')
impact_NQ_H_ded_SA_M7M9 = pd.read_csv('../test_H/impact_test/impact_SA_NQH_ded_12_03_21_M7M9.csv')

impact_l1_ded_SA_M10M12 = pd.read_csv('../test_QP/impact_test/impact_SA_L1_ded_12_03_21_M10M12.csv')
impact_l2_ded_SA_M10M12 = pd.read_csv('../test_QP/impact_test/impact_SA_L2_ded_12_03_21_M10M12.csv')
impact_Q_C_ded_SA_M10M12 = pd.read_csv('../test_C/impact_Test/impact_SA_QC_ded_12_03_21_M10M12.csv')
impact_NQ_C_ded_SA_M10M12 = pd.read_csv('../test_C/impact_Test/impact_SA_NQC_ded_12_03_21_M10M12.csv')
impact_Q_H_ded_SA_M10M12 = pd.read_csv('../test_H/impact_test/impact_SA_QH_ded_12_03_21_M10M12.csv')
impact_NQ_H_ded_SA_M10M12 = pd.read_csv('../test_H/impact_test/impact_SA_NQH_ded_12_03_21_M10M12.csv')

impact_l1_ded_M4M12_arr = [impact_l1_ded_SA_M4M6, impact_l1_ded_SA_M7M9, impact_l1_ded_SA_M10M12]
impact_l1_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_l1_ded_M4M12_arr)
impact_l1_ded_M4M12_Frame.to_csv('impact_SA_l1_ded_M4M12_Frame.csv')
impact_l2_ded_M4M12_arr = [impact_l2_ded_SA_M4M6, impact_l2_ded_SA_M7M9, impact_l2_ded_SA_M10M12]
impact_l2_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_l2_ded_M4M12_arr)
impact_l2_ded_M4M12_Frame.to_csv('impact_SA_l2_ded_M4M12_Frame.csv')

impact_Q_C_ded_M4M12_arr = [impact_Q_C_ded_SA_M4M6, impact_Q_C_ded_SA_M7M9, impact_Q_C_ded_SA_M10M12]
impact_Q_C_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_Q_C_ded_M4M12_arr)
impact_Q_C_ded_M4M12_Frame.to_csv('impact_SA_QC_ded_M4M12_Frame.csv')

impact_NQ_C_ded_M4M12_arr = [impact_NQ_C_ded_SA_M4M6, impact_NQ_C_ded_SA_M7M9, impact_NQ_C_ded_SA_M10M12]
impact_NQ_C_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_NQ_C_ded_M4M12_arr)
impact_NQ_C_ded_M4M12_Frame.to_csv('impact_SA_NQC_ded_M4M12_Frame.csv')

impact_Q_H_ded_M4M12_arr = [impact_Q_H_ded_SA_M4M6, impact_Q_H_ded_SA_M7M9, impact_Q_H_ded_SA_M10M12]
impact_Q_H_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_Q_H_ded_M4M12_arr)
impact_Q_H_ded_M4M12_Frame.to_csv('impact_SA_QH_ded_M4M12_Frame.csv')

impact_NQ_H_ded_M4M12_arr = [impact_NQ_H_ded_SA_M4M6, impact_NQ_H_ded_SA_M7M9, impact_NQ_H_ded_SA_M10M12]
impact_NQ_H_ded_M4M12_Frame = reduce(lambda left,right: pd.merge(left,right,on=['epsilon','del_avg_te','ro_mal','ro_max']), impact_NQ_H_ded_M4M12_arr)
impact_NQ_H_ded_M4M12_Frame.to_csv('impact_SA_NQH_ded_M4M12_Frame.csv')

#endregion