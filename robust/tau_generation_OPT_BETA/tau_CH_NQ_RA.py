# robust tau for Random Attack on cauchy and Huber 11-14-21
import pandas as pd
from robust.tau_generation_OPT_BETA.utils import *
from utility.constant import *

keys_TR = ['2014', '2015']
beta_max_c = 0.0001
beta_min_c = 0.0002
beta_max_h = 0.0001
beta_min_h = 0.0001

# region Cauchy additive
tau_result_array = []
for del_avg in DEL_AVG_ARRAY_ADD:
    for ro in RO_MAL_ARRAY:  # need to remove the ro from the code if want to use other training residual
        ruc_frame = pd.read_csv('../../data/training_ruc/additive_RUC/training_RUC_del_'+str(del_avg)+
                                '_romal_'+str(ro)+'_type_add.csv')
        max_candidate = ruc_frame[["ruc2014", "ruc2015"]].max(axis=1).max()  # returns the maximum between two columns
        min_candidate = ruc_frame[["ruc2014", "ruc2015"]].min(axis=1).min()  # return the minimum between two columns
        tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c = calculate_t_min_cauchy_non_Q(ruc_frame=ruc_frame,
                                                                                          keys=keys_TR,
                                                                                          tau_range=[.0,
                                                                                                     max_candidate,
                                                                                                     .00025],
                                                                                          b=beta_max_c)
        tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c = calculate_t_min_cauchy_non_Q(ruc_frame=ruc_frame,
                                                                                          keys=keys_TR,
                                                                                          tau_range=[min_candidate,
                                                                                                     0, .00025],
                                                                                          b=beta_min_c)

        object_c = {"del_avg_tr": del_avg, 'ro_mal': ro, 'type': 'add',
                    'tau_max_c': tau_max_c, 'tau_min_c': tau_min_c}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('RA_tau_OB_C_NQ_add.csv')
# endregion
# region cauchy Deductive
tau_result_array = []
for del_avg in DEL_AVG_ARRAY_DED:
    for ro in RO_MAL_ARRAY:  # need to remove the ro from the code if want to use other training residual
        ruc_frame = pd.read_csv('../../data/training_ruc/deductive_RUC/training_RUC_del_' + str(del_avg) +
                                '_romal_' + str(ro) + '_type_ded.csv')
        max_candidate = ruc_frame[["ruc2014", "ruc2015"]].max(axis=1).max()  # returns the maximum between two columns
        min_candidate = ruc_frame[["ruc2014", "ruc2015"]].min(axis=1).min()  # return the minimum between two columns
        tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c = calculate_t_min_cauchy_non_Q(ruc_frame=ruc_frame,
                                                                                          keys=keys_TR,
                                                                                          tau_range=[.0,
                                                                                                     max_candidate,
                                                                                                     .00025],
                                                                                          b=beta_max_c)
        tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c = calculate_t_min_cauchy_non_Q(ruc_frame=ruc_frame,
                                                                                          keys=keys_TR,
                                                                                          tau_range=[min_candidate,
                                                                                                     0, .00025],
                                                                                          b=beta_min_c)

        object_c = {"del_avg_tr": del_avg, 'ro_mal': ro, 'type': 'ded',
                    'tau_max_c': tau_max_c, 'tau_min_c': tau_min_c}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('RA_tau_OB_C_NQ_ded.csv')

# endregion


# region Huber additive
tau_result_array = []
for del_avg in DEL_AVG_ARRAY_ADD:
    for ro in RO_MAL_ARRAY:  # need to remove the ro from the code if want to use other training residual
        ruc_frame = pd.read_csv('../../data/training_ruc/additive_RUC/training_RUC_del_' + str(del_avg) +
                                '_romal_' + str(ro) + '_type_add.csv')
        max_candidate = ruc_frame[["ruc2014", "ruc2015"]].max(axis=1).max()  # returns the maximum between two columns
        min_candidate = ruc_frame[["ruc2014", "ruc2015"]].min(axis=1).min()  # return the minimum between two columns
        tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_min_huber_non_Q(ruc_frame=ruc_frame,
                                                                                         keys=keys_TR,
                                                                                         tau_range=[.0,
                                                                                                    max_candidate,
                                                                                                    .00025],
                                                                                         b=beta_max_h)
        tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber_non_Q(ruc_frame=ruc_frame,
                                                                                         keys=keys_TR,
                                                                                         tau_range=[min_candidate,
                                                                                                    0, .00025],
                                                                                         b=beta_min_h)

        object_c = {"del_avg_tr": del_avg, 'ro_mal': ro, 'type': 'add',
                    'tau_max_h': tau_max_h, 'tau_min_h': tau_min_h}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('RA_tau_OB_H_NQ_add.csv')
# endregion
# region Huber Deductive
tau_result_array = []
for del_avg in DEL_AVG_ARRAY_DED:
    for ro in RO_MAL_ARRAY:  # need to remove the ro from the code if want to use other training residual
        ruc_frame = pd.read_csv('../../data/training_ruc/deductive_RUC/training_RUC_del_' + str(del_avg) +
                                '_romal_' + str(ro) + '_type_ded.csv')
        max_candidate = ruc_frame[["ruc2014", "ruc2015"]].max(axis=1).max()  # returns the maximum between two columns
        min_candidate = ruc_frame[["ruc2014", "ruc2015"]].min(axis=1).min()  # return the minimum between two columns
        tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_min_huber_non_Q(ruc_frame=ruc_frame,
                                                                                         keys=keys_TR,
                                                                                         tau_range=[.0,
                                                                                                    max_candidate,
                                                                                                    .00025],
                                                                                         b=beta_max_h)
        tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber_non_Q(ruc_frame=ruc_frame,
                                                                                         keys=keys_TR,
                                                                                         tau_range=[min_candidate,
                                                                                                    0, .00025],
                                                                                         b=beta_min_h)

        object_c = {"del_avg_tr": del_avg, 'ro_mal': ro, 'type': 'ded',
                    'tau_max_h': tau_max_h, 'tau_min_h': tau_min_h}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('RA_tau_OB_H_NQ_ded.csv')

# endregion