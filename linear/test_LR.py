from utility.common import *
t_max_org_LR_l1 = 0.0275
t_min_org_LR_l1 = -0.0275
t_max_att_LR_l1 =  0.075
t_min_att_LR_l1 = -0.075
t_max_org_LR_l2 = 0.0425
t_min_org_LR_l2 = -0.0425
t_max_att_LR_l2 =  0.0875
t_min_att_LR_l2 = -0.0875

testing_residual = pd.read_csv("../data/testing_residual_2016_deductive_attack_del100_romal_30.csv")
testing_attacked_threshold(testing_residual, t_max_org_LR_l1, t_min_org_LR_l1, t_max_att_LR_l1, t_min_att_LR_l1)
testing_attacked_threshold(testing_residual, t_max_org_LR_l2, t_max_org_LR_l2, t_max_att_LR_l2, t_min_att_LR_l2)