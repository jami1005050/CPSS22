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
    is_target_reached = False
    k = 0
    while (is_target_reached == False):
        print('iteration count : ',k)
        k = k+1
        for i in range(0,len(sorted_list)): # upper points will not change the cardinality
            lower_set_ruc = [item for item in sorted_list if item < target_tau_max]  # splits into two sets
            upper_set_ruc = [item for item in sorted_list if item >= target_tau_max]
            cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
            if(sorted_list[i]>=target_tau_max):
                sorted_list[i] = sorted_list[i] + cap_lamda*lambda_p/2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_p / 2
            else:
                sorted_list[i] = sorted_list[i] + cap_lamda*lambda_c/2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_c / 2
            t_max_u, t_sum = calculateTmax_ruc_QR_l1(sorted_list)
            print("Initial set length: ", len(lower_set_ruc), ' ', len(upper_set_ruc),"calculated lambda: ", cap_lamda)
            print('tau_max: ',t_max_u)
            if(t_max_u>=target_tau_max):
                is_target_reached = True
                break

    return epsilon_vector

#problem even after adding some error in each of the point we are unable to reach the target
#we need to iterate over the points repeatedly untill get to the target
#this can be done by another while loop and checking the magnitude of the taumax
#I might not be thinking thouroughly about it but what can be stopping criteria other than target checking?

# def get_opt_epsilon_max(sorted_list,target_tau_max):
#     epsilon_vector = [0 for i in range(0,len(sorted_list))] #Declaring a epsilon vector
#     print(epsilon_vector) #printing the epsilon vector
#     lower_set_ruc = [item for item in sorted_list if item < target_tau_max]  # splits into two sets
#     upper_set_ruc = [item for item in sorted_list if item > target_tau_max]
#     cap_lamda = get_lambda_max(lower_set_ruc,upper_set_ruc,target_tau_max) #calculate lagrangian const
#     print("calculated lambda: ",cap_lamda)
#     isTarget_Reached = False
#     for i in range(0,len(upper_set_ruc)): # upper points will not change the cardinality
#         upper_set_ruc[i] = upper_set_ruc[i] + cap_lamda*lambda_p/2
#         cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
#         # print("calculated lambda: ", cap_lamda)
#         epsilon_vector[i] = cap_lamda*lambda_p/2
#         update_pos_ruc = upper_set_ruc + lower_set_ruc
#         t_max_u, t_sum = calculateTmax_ruc_QR_l1(update_pos_ruc)
#         if(t_max_u>target_tau_max):
#             isTarget_Reached = True
#             break
#     if(isTarget_Reached == False):
#         k = len(upper_set_ruc)
#         # i = len(lower_set_ruc) -1
#         i = 0
#         while i<len(lower_set_ruc):
#             # the lower points will obviously change the cardinality
#             temp = lower_set_ruc[i] + cap_lamda * lambda_c / 2
#             if(temp<target_tau_max): #if it is still less than the reference points than continue adding epsilon
#                 lower_set_ruc[i] = lower_set_ruc[i] + cap_lamda * lambda_c / 2
#                 cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
#                 # print("calculated lambda: ", cap_lamda)
#                 epsilon_vector[k+i] = cap_lamda * lambda_c / 2
#             else:
#                 print("executing else")
#                 lower_set_ruc[i] = lower_set_ruc[i] + cap_lamda * lambda_p / 2
#                 cap_lamda = get_lambda_max(lower_set_ruc, upper_set_ruc, target_tau_max)  # calculate lagrangian const
#                 # print("calculated lambda: ", cap_lamda)
#                 epsilon_vector[k + i] = cap_lamda * lambda_p / 2
#             i = i +1
#             update_pos_ruc = upper_set_ruc + lower_set_ruc
#             t_max_u, t_sum = calculateTmax_ruc_QR_l1(update_pos_ruc)
#             if (t_max_u >= target_tau_max):
#                 print("finish Execution")
#                 break
#     return epsilon_vector
# # returning the vector

taget_tau_max = 0.07 #Can be of any value
print(pos_merged_list_n)
pos_merged_list_n.sort(reverse=True)
pos_merged_list_n_copied = pos_merged_list_n.copy()
print(pos_merged_list_n_copied)
epsilon_vector = get_opt_epsilon_max(pos_merged_list_n_copied,taget_tau_max)
print('Positive RUC')
print(pos_merged_list_n)
t_max = calculateTmax_ruc_QR_l1(pos_merged_list_n)
print('T_MAX: ',t_max)
#Updating the values by epsilon vector
def add_epsilon(pos_merged_list_n, epsilon_vector):
    for i in range(0,len(pos_merged_list_n)):
        pos_merged_list_n[i] = pos_merged_list_n[i] + epsilon_vector[i]
    return pos_merged_list_n

update_pos_ruc = add_epsilon(pos_merged_list_n,epsilon_vector)
print('Epsilon ')
print(epsilon_vector)
print('Epsilon Added')
print(update_pos_ruc)
t_max_u = calculateTmax_ruc_QR_l1(update_pos_ruc)
print('T_MAX: ',t_max_u)
