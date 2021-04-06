from utility.common import *
t_max_QR = 0.065
t_min_QR = -0.065
t_max_att_QR =  0.075
t_min_att_QR = -0.0875
testing_residual = pd.read_csv("../data/testing_residual_2016_deductive_attack_del100_romal_30.csv")
testing_attacked_threshold(testing_residual,t_max_QR,t_min_QR,t_max_att_QR,t_min_att_QR)