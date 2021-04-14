from utility.common import *
t_max_org_QR_l1 = 0.065
t_min_org_QR_l1 = -0.065
t_max_att_QR_l1 =  0.12 # when romax -- 50 and epsilon .07
t_min_att_QR_l1 = -0.1175
t_max_org_QR_l2 = 0.08
t_min_org_QR_l2 = -0.08
t_max_att_QR_l2 =  0.1375 # when romax --50 and epsilon .07
t_min_att_QR_l2 = -0.14
testing_residual = pd.read_csv("../data/testing_residual_2016_deductive_attack_del100_romal_30.csv")
testing_attacked_threshold(testing_residual,t_max_org_QR_l1,t_min_org_QR_l1,t_max_att_QR_l1,t_min_att_QR_l1)
testing_attacked_threshold(testing_residual,t_max_org_QR_l2,t_min_org_QR_l2,t_max_att_QR_l2,t_min_att_QR_l2)