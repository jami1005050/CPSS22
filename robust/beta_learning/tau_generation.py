import pandas as pd
from robust.tau_generation.utils import*
ruc_frame_NA = pd.read_csv('training_RUC_mad_2.0csv') #cleaned training residual
ruc_frame_SA = pd.read_csv('SPA_QL1_EPS0.0069.csv')#smart attacked poisoned residual #RO==8
ruc_frame_RA = pd.read_csv('RPA_RUC_del_150_romal_0.3.csv') #random attacked poisoned residual

#if you have your residuals divided into two columns then you want to use the following functions
keys_TR = ['2014','2015']

def get_standard_limit_by_key(ruc_frame,keys_TR):
    max_candidate = ruc_frame[["ruc2014","ruc2015"]].max(axis = 1).max() #returns the maximum between two columns
    min_candidate = ruc_frame[["ruc2014","ruc2015"]].min(axis = 1).min() #return the minimum between two columns
    step_size = 0.0001 #step size will change the number of elements in the array
    #the step size should be choose according to the level of smoothness you want in your system.
    max_beta_array = np.arange(.0001,max_candidate,step_size)
    min_beta_array = np.arange(.0001,abs(min_candidate),step_size)
    tau_result_array = []
    for max_beta in max_beta_array:
        for min_beta in min_beta_array:
            tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c  = calculate_t_max_cauchy(ruc_frame = ruc_frame,
                                             keys= keys_TR,
                                             tau_range = [.0, max_candidate, .0025],
                                             w1 = 0.5,
                                             w2 = 2,
                                             b = max_beta)
            tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c  = calculate_t_min_cauchy(ruc_frame = ruc_frame,
                                             keys = keys_TR,
                                             tau_range = [min_candidate,0, .0025],
                                             w1 = 0.5,
                                             w2 = 2,
                                             b = max_beta)

            tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_max_huber(ruc_frame=ruc_frame,
                                                                                        keys=keys_TR,
                                                                                        tau_range=[.0, max_candidate,
                                                                                                   .0025],
                                                                                        w1=0.5,
                                                                                        w2=2,
                                                                                        b=max_beta)
            tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber(ruc_frame=ruc_frame,
                                                                                        keys=keys_TR,
                                                                                        tau_range=[min_candidate, 0, .0025],
                                                                                        w1=0.5,
                                                                                        w2=2,
                                                                                        b=max_beta)

            object_c = {"beta_p":max_beta,'beta_n':min_beta,
                        'tau_max_c':tau_max_c,'tau_min_c':tau_min_c,
                        'tau_max_h':tau_max_h,'tau_min_h':tau_min_h}
            tau_result_array.append(object_c)

    tau_result_frame = pd.DataFrame(tau_result_array)
    tau_result_frame.to_csv('RA_tau_DEL150_ROMAL03.csv')


def get_standard_limit_from_combined_frame(ruc_frame):
    max_candidate = ruc_frame['ruc'].max()  # returns the maximum between two columns
    min_candidate = ruc_frame["ruc"].min()  # return the minimum between two columns
    step_size = 0.0001  # step size will change the number of elements in the array
    # the step size should be choose according to the level of smoothness you want in your system.
    max_beta_array = np.arange(.0001, max_candidate, step_size)
    min_beta_array = np.arange(.0001, abs(min_candidate), step_size)
    tau_result_array = []
    for max_beta in max_beta_array:
        for min_beta in min_beta_array:
            tau_max_c, attack_t_max_loss_list_c, attack_t_max_list_c = calculate_t_max_cauchy_combined_frame(ruc_frame=ruc_frame,
                                                                                              tau_range=[.0,
                                                                                                         max_candidate,
                                                                                                         .0025],
                                                                                              w1=0.5,
                                                                                              w2=2,
                                                                                              b=max_beta)
            tau_min_c, attack_t_min_loss_list_c, attack_t_min_list_c = calculate_t_min_cauchy_combined_frame(ruc_frame=ruc_frame,
                                                                                              tau_range=[min_candidate,
                                                                                                         0, .0025],
                                                                                              w1=0.5,
                                                                                              w2=2,
                                                                                              b=max_beta)

            tau_max_h, attack_t_max_loss_list_h, attack_t_max_list_h = calculate_t_max_huber_combined_frame(ruc_frame=ruc_frame,
                                                                                             tau_range=[.0,
                                                                                                        max_candidate,
                                                                                                        .0025],
                                                                                             w1=0.5,
                                                                                             w2=2,
                                                                                             b=max_beta)
            tau_min_h, attack_t_min_loss_list_h, attack_t_min_list_h = calculate_t_min_huber_combined_frame(ruc_frame=ruc_frame,
                                                                                             tau_range=[min_candidate,
                                                                                                        0, .0025],
                                                                                             w1=0.5,
                                                                                             w2=2,
                                                                                             b=max_beta)

            object_c = {"beta_p": max_beta, 'beta_n': min_beta,
                        'tau_max_c': tau_max_c, 'tau_min_c': tau_min_c,
                        'tau_max_h': tau_max_h, 'tau_min_h': tau_min_h}
            tau_result_array.append(object_c)

    tau_result_frame = pd.DataFrame(tau_result_array)
    tau_result_frame.to_csv('SA_tau_ro_8_eps0069.csv')

# get_standard_limit_from_combined_frame(ruc_frame_SA)
get_standard_limit_by_key(ruc_frame_RA,keys_TR)