from utility.common import *
t_max_org_LR_l1 = 0.0275
t_min_org_LR_l1 = -0.0275
t_max_att_LR_l1 =  0.075
t_min_att_LR_l1 = -0.075
t_max_org_LR_l2 = 0.0425
t_min_org_LR_l2 = -0.0425
t_max_att_LR_l2 =  0.0875
t_min_att_LR_l2 = -0.0875

testing_residual = pd.read_csv("../data/test_ruc/test_residuals/TR_DA_del100_romal_30_M4M6_old.csv")
testing_attacked_threshold(testing_residual, t_max_org_LR_l1, t_min_org_LR_l1, t_max_att_LR_l1, t_min_att_LR_l1)
testing_attacked_threshold(testing_residual, t_max_org_LR_l2, t_max_org_LR_l2, t_max_att_LR_l2, t_min_att_LR_l2)