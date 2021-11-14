import utils
import pandas as pd
import json
from utility.constant import*

loss_function = 'cauchy'  # l2 huber pseudo_huber

rob_res_benign = {}
for del_avg in DEL_AVG_ARRAY_DED:
    rob_res_benign[del_avg] = {}
    for ro in RO_MAL_ARRAY: # need to remove the ro from the code if want to use other training residual
        rob_res_benign[del_avg][ro] = {}
        ruc_frame = pd.read_csv('t_RUC_RA/training_RUC_del_'+
                                str(del_avg)+'_romal_'+str(ro)+'csv')
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
                                                                           w1=.5, w2=2., b=beta)
            train_t_min, train_t_min_loss_list, train_t_min_list = getattr(utils, 'calculate_t_min_' + loss_function)(
                                                                           ruc_frame,  keys_TR,
                                                                           tau_range=[min_candidate, .0, .0025],
                                                                           w1=.5, w2=2., b=beta)
            rob_res_benign[del_avg][ro][beta] = {'tau_max':train_t_max,'tau_min':train_t_min}


with open("../../test_C/result_data/standard_limit/robust_C_RO_DEL_RA.json", "w") as outfile:
    json.dump(rob_res_benign, outfile)