import pandas as pd
from test_QP.ruc_SA.functions_QR_CLN import *

lambda_c = 0.5
lambda_p = 2.0
residual = pd.read_csv('../data/training_ruc/training_RUC_TDSC_Noisy.csv')
residual_ar_pos2014 = residual[residual['ruc2014']>0]['ruc2014'].tolist()
residual_ar_pos2015 = residual[residual['ruc2015']>0]['ruc2015'].tolist()
residual_ar_neg2014 = residual[residual['ruc2014']<0]['ruc2014'].tolist()
residual_ar_neg2015 = residual[residual['ruc2015']<0]['ruc2015'].tolist()
neg_merged_list_n = residual_ar_neg2014 + residual_ar_neg2015
pos_merged_list_n = residual_ar_pos2014 + residual_ar_pos2015
# print(residual_ar_neg2014)
# print(residual_ar_pos2014)

def get_lambda_max(lower_set_ruc,upper_set_ruc,target_tau_max):
    lower_sum = 0
    upper_sum = 0
    for item in lower_set_ruc:#SUM for all points below tau ref
        lower_sum = lower_sum + lambda_c * (target_tau_max - item)
    for item in upper_set_ruc:#SUM for all points above tau ref
        upper_sum = upper_sum + lambda_p * (item - target_tau_max)
    # following line calculates the lagrangian
    return (lower_sum - upper_sum)/(len(upper_set_ruc)*lambda_p*lambda_p/2+len(lower_set_ruc)*lambda_c*lambda_c/2)

def get_opt_epsilon_max(sorted_list,target_tau_max):
    epsilon_vector = [0 for i in range(0,len(sorted_list))] #Declaring a epsilon vector
    print(epsilon_vector) #printing the epsilon vector
    lower_set_ruc = [item for item in sorted_list if item < target_tau_max]  # splits into two sets
    upper_set_ruc = [item for item in sorted_list if item > target_tau_max]
    cap_lamda = get_lambda_max(lower_set_ruc,upper_set_ruc,target_tau_max) #calculate lagrangian const
    print("calculated lambda: ",cap_lamda)
    for i in range(0,len(upper_set_ruc)): # upper points will not change the cardinality
        upper_set_ruc[i] = upper_set_ruc[i] + cap_lamda*lambda_p/2
        cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
        # print("calculated lambda: ", cap_lamda)
        epsilon_vector[i] = cap_lamda*lambda_p/2

    k = len(upper_set_ruc)
    i = len(lower_set_ruc) -1
    while i>=0:
         # the lower points will obviously change the cardinality
        temp = lower_set_ruc[i] + cap_lamda * lambda_c / 2
        if(temp<=target_tau_max): #if it is still less than the reference points than continue adding epsilon
            lower_set_ruc[i] = lower_set_ruc[i] + cap_lamda * lambda_c / 2
            cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
            # print("calculated lambda: ", cap_lamda)
            epsilon_vector[k+i] = cap_lamda * lambda_p / 2
            i = i - 1
        else:# exit here as we can no longer
            break

    return epsilon_vector # returning the vector

taget_tau_max = 0.1 #Can be of any value
print(pos_merged_list_n)
pos_merged_list_n.sort(reverse=True)
print(pos_merged_list_n)
epsilon_vector = get_opt_epsilon_max(pos_merged_list_n,taget_tau_max)
print(epsilon_vector)
t_max = calculateTmax_ruc_QR_l1(pos_merged_list_n)
print('T_MAX: ',t_max)
#Updating the values by epsilon vector
def add_epsilon(pos_merged_list_n, epsilon_vector):
    for i in range(0,len(pos_merged_list_n)):
        pos_merged_list_n[i] = pos_merged_list_n[i] + epsilon_vector[i]
    return pos_merged_list_n

update_pos_ruc = add_epsilon(pos_merged_list_n,epsilon_vector)

t_max_u = calculateTmax_ruc_QR_l1(update_pos_ruc)
print('T_MAX: ',t_max_u)
