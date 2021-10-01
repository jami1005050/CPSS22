import utils
import pandas as pd
import json
loss_function = 'cauchy'  # l2 huber pseudo_huber
rob_res_benign = {}
ruc_frame = pd.read_csv('../test_QP/result/residual/cleaned_res/training_RUC_mad_2.0csv')
keys_TR = ['2014','2015']
minRuc2014 = ruc_frame['ruc2014'].min()
minRuc2015 = ruc_frame['ruc2015'].min()
min_candidate = min(minRuc2015, minRuc2014)
maxRuc2014 = ruc_frame['ruc2014'].max()
maxRuc2015 = ruc_frame['ruc2015'].max()
max_candidate = max(maxRuc2015, maxRuc2014)
print(max_candidate,' ',min_candidate)
# for beta in BETA_ARR:
#     train_t_max, train_t_max_loss_list, train_t_max_list = getattr(utils, 'calculate_t_max_' + loss_function)(
#                                                                    ruc_frame, keys_TR,
#                                                                    tau_range=[.0, max_candidate, .0025],
#                                                                    w1=.5, w2=2., b=0.006)
#     train_t_min, train_t_min_loss_list, train_t_min_list = getattr(utils, 'calculate_t_min_' + loss_function)(
#                                                                    ruc_frame,  keys_TR,
#                                                                    tau_range=[min_candidate, .0, .0025],
#                                                                    w1=.5, w2=2., b=0.006)
#     rob_res_benign[key][beta] = {'tau_max':train_t_max,'tau_min':train_t_min}
#     print(train_t_min,train_t_max)
#     break
#
#
# with open("../test_H/robust_benign_H.json", "w") as outfile:
#     json.dump(rob_res_benign, outfile)
#

