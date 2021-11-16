from test_QP.ruc_SA.functions_QR_CLN import *
import numpy as np
ruc_frame = pd.read_csv('../../robust/beta_learning/training_RUC_mad_2.0csv')
ruc_n1 = ruc_frame[ruc_frame['ruc2014']<0]['ruc2014'].tolist()
ruc_n2 = ruc_frame[ruc_frame['ruc2015']<0]['ruc2015'].tolist()
neg_merged_list_n = ruc_n1 + ruc_n2
ruc_p1 = ruc_frame[ruc_frame['ruc2014']>0]['ruc2014'].tolist()
ruc_p2 = ruc_frame[ruc_frame['ruc2015']>0]['ruc2015'].tolist()
pos_merged_list_p = ruc_p1 + ruc_p2
min_epsilon = min(neg_merged_list_n) # returns the maximum between two columns
max_epsilon = max(pos_merged_list_p)
step_size = .00025
max_eps_array = np.arange(.0001, max_epsilon, step_size)
tau_min_l1 =-0.012766112936864759
tau_max_l1 =0.0125
tau_min_l2 = -0.015266112936864758
tau_max_l2 = 0.015
tau_result_array = []
for ro_max in ROMAX_ARRAY:
    for max_eps in max_eps_array:
        ruc_frame1,tmin = get_neg_residual_SA(neg_merged_list_n,tau_min_l1,max_eps)
        ruc_frame2,tmax = get_pos_residual_SA(pos_merged_list_p,tau_max_l1,max_eps)
        object_c = {"ro_max": ro_max, 'epsilon': max_eps,
                    'tau_max': tmin, 'tau_min': tmax}
        tau_result_array.append(object_c)
        merged_array1 = ruc_frame1
        for x in ruc_frame2:
            merged_array1.append(x)
        df1 = pd.DataFrame(merged_array1,columns=['ruc'])
        df1.to_csv('ruc_romax'+str(ro_max)+'_sa_eps'+str(max_eps)+'.csv')

tau_result_frame = pd.DataFrame(tau_result_array)
tau_result_frame.to_csv('SA_tau_L2.csv')