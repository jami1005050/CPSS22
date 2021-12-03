#robust tau for Smart  Attack on cauchy and Huber 11-14-21

import pandas as pd
from robust.tau_generation_OPT_BETA.utils import *
from utility.constant import*
from tqdm import tqdm

beta_max_c = 0.0001
beta_min_c = 0.0001
beta_max_h = 0.0001
beta_min_h = 0.0001

SA_tau_frame = pd.read_csv('SA_tau_L1.csv', dtype=str)
eps_list = SA_tau_frame['epsilon'].unique().tolist()
print(len(eps_list))
#region Cauchy
tau_result_array = []
for romax in tqdm(ROMAX_ARRAY,desc='progress for cauchy'):
    print("c: ",romax)
    for eps in eps_list: # need to remove the ro from the code if want to use other training residual

        ruc_frame = pd.read_csv('../../data/training_ruc/training_SA/ruc_romax'+str(romax)+'_sa_eps'+str(eps)+'.csv')
        max_candidate = ruc_frame['ruc'].max()  # returns the maximum between two columns
        min_candidate = ruc_frame["ruc"].min()  # return the minimum between two columns
        tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c = calculate_t_max_cauchy_combined_frame(ruc_frame=ruc_frame,
                                                                                          tau_range=[.0,
                                                                                                     max_candidate,
                                                                                                     .00025],
                                                                                          w1=0.5,
                                                                                          w2=2,
                                                                                          b=beta_max_c)
        tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c = calculate_t_min_cauchy_combined_frame(ruc_frame=ruc_frame,
                                                                                          tau_range=[min_candidate,
                                                                                                     0, .00025],
                                                                                          w1=0.5,
                                                                                          w2=2,
                                                                                          b=beta_min_c)


        object_c = {"romax": romax, 'epsilon': eps,
                    'tau_max_c': tau_max_c, 'tau_min_c': tau_min_c}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('SA_tau_CQ_12_03_21.csv')
#endregion

# region Huber
tau_result_array = []
for romax in tqdm(ROMAX_ARRAY,desc='progress for huber'):
    for eps in eps_list:  # need to remove the ro from the code if want to use other training residual
        ruc_frame = pd.read_csv('../../data/training_ruc/training_SA/ruc_romax'+str(romax)+'_sa_eps'+str(eps)+'.csv')
        max_candidate = ruc_frame['ruc'].max()  # returns the maximum between two columns
        min_candidate = ruc_frame["ruc"].min()  # return the minimum between two columns
        tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_max_huber_combined_frame(ruc_frame=ruc_frame,
                                                                                          tau_range=[.0,
                                                                                                     max_candidate,
                                                                                                     .00025],
                                                                                          w1=0.5,
                                                                                          w2=2,
                                                                                          b=beta_max_h)
        tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber_combined_frame(ruc_frame=ruc_frame,
                                                                                          tau_range=[min_candidate,
                                                                                                     0, .00025],
                                                                                          w1=0.5,
                                                                                          w2=2,
                                                                                          b=beta_min_h)

        object_c = {"romax": romax, 'epsilon': eps,
                    'tau_max_h': tau_max_h, 'tau_min_h': tau_min_h}
        tau_result_array.append(object_c)
tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('SA_tau_HQ_12_03_21.csv')
# endregion
