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
tau_result_array_l1 = []
tau_result_array_l2 = []
for ro_max in ROMAX_ARRAY:
    if (len(neg_merged_list_n) < ro_max):
        for i in range(0, (ro_max - len(neg_merged_list_n))):
            neg_merged_list_n.append(0)
    if (len(pos_merged_list_p) < ro_max):
        for i in range(0, (ro_max - len(pos_merged_list_p))):
            pos_merged_list_p.append(0)
    for max_eps in max_eps_array:
        ruc_frame1,tmin_l1 = get_neg_residual_SA_l1(neg_merged_list_n,tau_min_l1,max_eps,ro_max)
        ruc_frame2,tmax_l1 = get_pos_residual_SA_l1(pos_merged_list_p,tau_max_l1,max_eps,ro_max)
        ruc_frame3, tmin_l2 = get_neg_residual_SA_l2(neg_merged_list_n, tau_min_l2, max_eps, ro_max)
        ruc_frame4, tmax_l2 = get_pos_residual_SA_l2(pos_merged_list_p, tau_max_l2, max_eps, ro_max)

        object_c_l1 = {"ro_max": ro_max, 'epsilon': max_eps,
                    'tau_max': tmin_l1, 'tau_min': tmax_l1}
        object_c_l2 = {"ro_max": ro_max, 'epsilon': max_eps,
                    'tau_max': tmin_l2, 'tau_min': tmax_l2}
        tau_result_array_l1.append(object_c_l1)
        tau_result_array_l2.append(object_c_l2)
        merged_array1 = ruc_frame1
        for x in ruc_frame2:
            merged_array1.append(x)
        df1 = pd.DataFrame(merged_array1,columns=['ruc'])
        df1.to_csv('ruc_romax'+str(ro_max)+'_sa_eps'+str(max_eps)+'.csv')


tau_result_frame_l1 = pd.DataFrame(tau_result_array_l1)
tau_result_frame_l1.to_csv('SA_tau_L1.csv')
tau_result_frame_l2 = pd.DataFrame(tau_result_array_l2)
tau_result_frame_l2.to_csv('SA_tau_L2.csv')