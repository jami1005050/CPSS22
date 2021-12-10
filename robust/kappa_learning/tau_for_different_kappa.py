import pandas as pd
from robust.tau_generation_OPT_BETA.utils import*
from tqdm import  tqdm
from utility.constant import KAPPA
ruc_frame_NA = pd.read_csv('../../data/training_ruc_kappa_varied/training_RUC_mad_2.0csv') #cleaned training residual
keys_TR = ['2014','2015']
beta_max_c = 0.0002
beta_min_c = 0.0002
beta_max_h = 0.0001
beta_min_h = 0.0001
def get_standard_limit_by_key(ruc_frame,keys_TR,kappa):
    max_candidate = ruc_frame[["ruc2014","ruc2015"]].max(axis = 1).max() #returns the maximum between two columns
    min_candidate = ruc_frame[["ruc2014","ruc2015"]].min(axis = 1).min() #return the minimum between two columns
    tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c  = calculate_t_max_cauchy(ruc_frame = ruc_frame,
                                     keys= keys_TR,
                                     tau_range = [0, max_candidate, 0.00025],
                                     w1 = 0.5,
                                     w2 = 2.0,
                                     b = beta_max_c)
    tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c  = calculate_t_min_cauchy(ruc_frame = ruc_frame,
                                     keys = keys_TR,
                                     tau_range = [min_candidate,0, 0.00025],
                                     w1 = 0.5,
                                     w2 = 2.0,
                                     b = beta_min_c)
    tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_max_huber(ruc_frame=ruc_frame,
                                     keys=keys_TR,
                                     tau_range=[0, max_candidate,0.00025],
                                     w1=0.5,
                                     w2=2.0,
                                     b=beta_max_h)
    tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber(ruc_frame=ruc_frame,
                                     keys=keys_TR,
                                     tau_range=[min_candidate, 0, .00025],
                                     w1=0.5,
                                     w2=2.0,
                                     b=beta_min_h)

    return tau_max_c,tau_min_c,tau_max_h,tau_min_h


tau_result_array = []
for k in tqdm(KAPPA,desc='progress For Kappa'):
    ruc_frame_NA = pd.read_csv(
        '../../data/training_ruc_kappa_varied/training_RUC_mad_'+str(k)+'csv')  # cleaned training residual
    tau_max_c,tau_min_c,tau_max_h,tau_min_h = get_standard_limit_by_key(ruc_frame_NA,keys_TR,k)
    object_c = {"kappa": k, 'tau_max_c': tau_max_c, 'tau_min_c': tau_min_c,
                'tau_max_h': tau_max_h, 'tau_min_h': tau_min_h}

    tau_result_array.append(object_c)


tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('tau_kappa_varied_CH_12_09_21.csv')