from utility.common import *
t_max_LR = 0.0275
t_min_LR = -0.0275
t_max_att_LR =  0.0475
t_min_att_LR = -0.055

testing_residual = pd.read_csv("../data/testing_residual_2016_deductive_attack_del100_romal_30.csv")
testing_attacked_threshold(testing_residual,t_max_LR,t_min_LR,t_max_att_LR,t_min_att_LR)