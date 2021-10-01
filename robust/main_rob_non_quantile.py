import utils
import pandas as pd
import json

from utility.constant import BETA_ARR

loss_function = 'cauchy_non_Q'  # l2 huber pseudo_huber
# f = open('../test_QP/poison_tau_K2.json')
#
# # returns JSON object as
# # a dictionary
# #Order of the key kappa--> romax--> epsilon--> beta
# poisoning_std_limits = json.load(f)
# rob_poisoin_limit ={}
# for key2 in poisoning_std_limits.keys():
#     rob_poisoin_limit[key2] = {}
#     for key3 in poisoning_std_limits[key2].keys():
#         rob_poisoin_limit[key2][key3] = {}
#         data = pd.DataFrame()
#         ruc_frame_attacked = pd.read_csv('../test_QP/poison_res_k2/FGAV_QL1_RO_'+str(key2)+'_EPS'+str(key3)+'_K2_.csv')
#         data['ruc2014'] = ruc_frame_attacked['ruc']
#         keys = ['2014']
#         min_candidate1 = data['ruc2014'].min()
#         max_candidate1 = data['ruc2014'].max()
#         for beta in BETA_ARR:
#             attack_t_max, attack_t_max_loss_list, attack_t_max_list = getattr(utils,'calculate_t_max_' + loss_function)(
#                 data, keys,tau_range=[.0, max_candidate1, .0025], b=beta)
#             attack_t_min, attack_t_min_loss_list, attack_t_min_list = getattr(utils,'calculate_t_min_' + loss_function)(
#                 data, keys,tau_range=[min_candidate1, .0, .0025], b=beta)
#             rob_poisoin_limit[key2][key3][beta] = {'tau_max':attack_t_max,'tau_min':attack_t_min}
#
# with open("../test_H/robust_poison_H_non_Q_K2.json", "w") as outfile:
#     json.dump(rob_poisoin_limit, outfile)

tau_dict = {1.0:{'tau_max': 0.005, 'tau_min': -0.0038691378044811986},
            1.25:{ 'tau_max': 0.0025, 'tau_min': -0.0029683815875770903},
            1.5:{ 'tau_max': 0.0025, 'tau_min': -0.004567625370672981},
            1.75:{ 'tau_max': 0.0075, 'tau_min': -0.006166869153768871},
            2.0: {'tau_max': 0.0125, 'tau_min': -0.012766112936864759},
            2.25:{ 'tau_max': 0.0125, 'tau_min': -0.01186535671996054},
            2.5:{ 'tau_max': 0.01, 'tau_min': -0.010964600503056431}}

rob_res_benign = {}
#order of the key is kappa --> beta
for key in tau_dict.keys():
    rob_res_benign[key] = {}
    # ruc_frame = pd.read_csv('../test_QP/cleaned_res/training_RUC_mad_'+str(key)+'csv')
    ruc_frame = pd.read_csv('../test_QP/result/residual/cleaned_res/training_RUC_mad_2.0csv')
    keys_TR = ['2014','2015']
    minRuc2014 = ruc_frame['ruc2014'].min()
    minRuc2015 = ruc_frame['ruc2015'].min()
    min_candidate = min(minRuc2015, minRuc2014)
    maxRuc2014 = ruc_frame['ruc2014'].max()
    maxRuc2015 = ruc_frame['ruc2015'].max()
    max_candidate = max(maxRuc2015, maxRuc2014)
    for beta in BETA_ARR:
        train_t_max, train_t_max_loss_list, train_t_max_list = getattr(utils, 'calculate_t_max_' + loss_function)(
                                                                       ruc_frame, keys_TR,
                                                                       tau_range=[.0, max_candidate, .0025],
                                                                       b=0.006)
        train_t_min, train_t_min_loss_list, train_t_min_list = getattr(utils, 'calculate_t_min_' + loss_function)(
                                                                       ruc_frame,  keys_TR,
                                                                       tau_range=[min_candidate, .0, .0025],
                                                                       b=0.006)
        rob_res_benign[key][beta] = {'tau_max':train_t_max,'tau_min':train_t_min}
        print(train_t_min,train_t_max)

        break
    break


# with open("../test_H/robust_benign_H.json", "w") as outfile:
#     json.dump(rob_res_benign, outfile)
