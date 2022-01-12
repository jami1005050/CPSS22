from test_QP.ruc_SA.functions_QR_CLN import *
import  time
import numpy as np
from tqdm import tqdm

#region Read Residual Input
residual = pd.read_csv('../data/training_ruc/training_RUC_TDSC_Noisy.csv')
residual_ar_pos2014 = residual[residual['ruc2014']>0]['ruc2014'].tolist()
residual_ar_pos2015 = residual[residual['ruc2015']>0]['ruc2015'].tolist()
residual_ar_neg2014 = residual[residual['ruc2014']<0]['ruc2014'].tolist()
residual_ar_neg2015 = residual[residual['ruc2015']<0]['ruc2015'].tolist()
neg_merged_list_n = residual_ar_neg2014 + residual_ar_neg2015
pos_merged_list_n = residual_ar_pos2014 + residual_ar_pos2015
pos_merged_list_n_sr = [pos_merged_list_n[i] for i in range(0, len(pos_merged_list_n))]  # Creating a new array
pos_merged_list_n_mr = [pos_merged_list_n[i] for i in range(0, len(pos_merged_list_n))]  # Creating a new array
neg_merged_list_n_sr = [neg_merged_list_n[i] for i in range(0, len(neg_merged_list_n))]  # Creating a new array
neg_merged_list_n_mr = [neg_merged_list_n[i] for i in range(0, len(neg_merged_list_n))]  # Creating a new array

# print(residual_ar_neg2014)
# print(residual_ar_pos2014)
#endregion
#region list of Hyperparameters
lambda_c = 0.5
lambda_p = 2.0
ALPHA_MAX = 10
EPSILON_MAX = max(max(pos_merged_list_n), abs(min(neg_merged_list_n))) # considering the larges abs residual value
print((len(pos_merged_list_n)),' ',(len(neg_merged_list_n)))
alpha_max_array = np.arange(start = 2, stop = 30, step = 2)
#starting with 2 input and untill 40(considering it as a large perturbation)
epsilon_max_array = np.arange(start = min(pos_merged_list_n),
                              stop = max(pos_merged_list_n),
                              step = (max(pos_merged_list_n)-min(pos_merged_list_n))/10 )
#defining a epsilon max array within the max and min residual and deviding them into 10 potential candidate
#total number of run will be 15*10 = 150 iteration
target_tau_max_array = [0.10,0.20,0.30] #this target standard limit should be from impact
target_tau_min_array = [-0.10,-0.20,-0.30]
#endregion

#region Epsilon Functions For Largrangian
def get_lambda_Coeff(lower_set_ruc, upper_set_ruc, target_tau):
    lower_sum = 0
    upper_sum = 0
    for item in lower_set_ruc:#SUM for all points below tau ref
        lower_sum = lower_sum + lambda_c * abs(target_tau - item)
    for item in upper_set_ruc:#SUM for all points above tau ref
        upper_sum = upper_sum + lambda_p * abs(item - target_tau)
    # following line calculates the lagrangian
    return (lower_sum - upper_sum)/(len(upper_set_ruc)*lambda_p*lambda_p/2+len(lower_set_ruc)*lambda_c*lambda_c/2)

def get_epsilon_w_t_std_limit(sorted_list, target_tau, type):
    epsilon_vector = [0 for i in range(0,len(sorted_list))] #Declaring a epsilon vector
    is_target_reached = False
    k = 0
    while (is_target_reached == False):
        print('iteration count : ',k)
        k = k+1
        for i in range(0,len(sorted_list)): # upper points will not change the cardinality
            lower_set_ruc = [item for item in sorted_list if abs(item) < abs(target_tau)]  # splits into two sets
            upper_set_ruc = [item for item in sorted_list if abs(item) >= abs(target_tau)]
            cap_lamda = get_lambda_Coeff(lower_set_ruc, upper_set_ruc, target_tau)  # calculate lagrangian const
            if(abs(sorted_list[i])>=abs(target_tau)):
                if(type == 0):
                    sorted_list[i] = sorted_list[i] + cap_lamda*lambda_p/2
                else:
                    sorted_list[i] = sorted_list[i] - cap_lamda * lambda_p / 2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_p / 2
            else:
                if (type == 0):
                    sorted_list[i] = sorted_list[i] + cap_lamda * lambda_c / 2
                else:
                    sorted_list[i] = sorted_list[i] - cap_lamda * lambda_c / 2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_c / 2
            if(type == 0):
                t_max_u, t_sum = calculateTmax_ruc_QR_l1(sorted_list)
                # print('tau_max: ', t_max_u)
                if (abs(t_max_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
            else:
                t_min_u, t_sum = calculateTmin_ruc_QR_l1(sorted_list)
                # print('tau_min: ', t_min_u)
                if (abs(t_min_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
            # print("Initial set length: ", len(lower_set_ruc), ' ', len(upper_set_ruc),"calculated lambda: ", cap_lamda)
    return epsilon_vector

def check_for_stopping_criteria(epsilon_vector,is_target_reached,alpha_max,epsilon_max):
    if(is_target_reached == True):
        print("Target Reached")
        return True #if target reached there is no need to add more perturbation
    else: #if not reached the target check if it has more scope of perturbation
        k = 0
        for item in epsilon_vector:
            if(k == alpha_max):break # check epsilon for alpha max as only you can add perturbation to those points only
            if(item <= epsilon_max):
                return False
            k = k+1
        print("Epsilon Max Reached")
        return True

def get_epsilon_w_t_std_limit_cons_alpha(sorted_list, target_tau, type,alpha_max,epsilon_max):#can use alpha max and epsilon max as parameters
    epsilon_vector = [0 for i in range(0,len(sorted_list))] #Declaring a epsilon vector
    is_target_reached = False
    while (True):
        is_stopping_criteria_met = check_for_stopping_criteria(epsilon_vector,is_target_reached,alpha_max,epsilon_max)
        if(is_stopping_criteria_met == True):break
        for i in range(0,alpha_max): # upper points will not change the cardinality
            lower_set_ruc = [item for item in sorted_list if abs(item) < abs(target_tau)]  # splits into two sets
            upper_set_ruc = [item for item in sorted_list if abs(item) >= abs(target_tau)]
            cap_lamda = get_lambda_Coeff(lower_set_ruc, upper_set_ruc, target_tau)  # calculate lagrangian const
            if(abs(sorted_list[i])>=abs(target_tau)):
                if(type == 0):
                    sorted_list[i] = sorted_list[i] + cap_lamda*lambda_p/2
                else:
                    sorted_list[i] = sorted_list[i] - cap_lamda * lambda_p / 2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_p / 2
            else:
                if (type == 0):
                    sorted_list[i] = sorted_list[i] + cap_lamda * lambda_c / 2
                else:
                    sorted_list[i] = sorted_list[i] - cap_lamda * lambda_c / 2
                epsilon_vector[i] = epsilon_vector[i]+ cap_lamda * lambda_c / 2
            if(type == 0):
                t_max_u, t_sum = calculateTmax_ruc_QR_l1(sorted_list)
                # print('tau_max: ', t_max_u)
                if (abs(t_max_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
            else:
                t_min_u, t_sum = calculateTmin_ruc_QR_l1(sorted_list)
                # print('tau_min: ', t_min_u)
                if (abs(t_min_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
            # print("Initial set length: ", len(lower_set_ruc), ' ', len(upper_set_ruc),"calculated lambda: ", cap_lamda)
    return epsilon_vector
#endregion
#region Compile Lagrangian Single Run
taget_tau_max = 0.7 #Can be of any value
print("Original List")
print(pos_merged_list_n_sr)
pos_merged_list_n_copied = [pos_merged_list_n_sr[i] for i in range(0, len(pos_merged_list_n_sr))]  # Creating a new array
pos_merged_list_n_sr.sort(reverse=True)
print("Sorted List")
print(pos_merged_list_n)
t_max,tsum_max = calculateTmax_ruc_QR_l1(pos_merged_list_n_copied)
t_min,tsum_min = calculateTmin_ruc_QR_l1(neg_merged_list_n)
print('T_MAX: ',t_max,' T_Min: ',t_min)
type = 0 # 0 means run for tmax otherwise run for tmin
Start_time = time.perf_counter()
epsilon_vector = get_epsilon_w_t_std_limit_cons_alpha(pos_merged_list_n_sr, taget_tau_max, type, ALPHA_MAX, EPSILON_MAX)
End_time = time.perf_counter()
print("Time for Lagrangian: ",(End_time - Start_time))
#Updating the values by epsilon vector
# def add_epsilon(pos_merged_list_n, epsilon_vector):
#     for i in range(0,len(pos_merged_list_n)):
#         pos_merged_list_n[i] = pos_merged_list_n[i] + epsilon_vector[i]
#     return pos_merged_list_n
# update_pos_ruc = add_epsilon(pos_merged_list_n_copied,epsilon_vector)
print('Epsilon ')
print(epsilon_vector)
print('Epsilon Added')
print(pos_merged_list_n)
t_max_u,tsum = calculateTmax_ruc_QR_l1(pos_merged_list_n_sr)
print('T_MAX After perturbation: ',t_max_u)
#endregion
#region Compile Lagrangian For Multiple Run
performance_result = []
for alpha_max in tqdm(alpha_max_array,desc='progress for Lagrangian TMAX'):
    for epsilon_max in epsilon_max_array:
        for  c_t_max in target_tau_max_array:
            print("Original List")
            print(pos_merged_list_n_mr)
            pos_merged_list_n_copied = [pos_merged_list_n_mr[i] for i in range(0, len(pos_merged_list_n_mr))]  # Creating a new array
            pos_merged_list_n_copied.sort(reverse=True)
            print("Sorted List")
            print(pos_merged_list_n_copied)
            # t_max,tsum_max = calculateTmax_ruc_QR_l1(pos_merged_list_n_copied)
            # t_min,tsum_min = calculateTmin_ruc_QR_l1(neg_merged_list_n)
            # print('T_MAX: ',t_max,' T_Min: ',t_min)
            type = 0 # 0 means run for tmax otherwise run for tmin
            Start_time = time.perf_counter()
            epsilon_vector = get_epsilon_w_t_std_limit_cons_alpha(pos_merged_list_n_copied,c_t_max, type,alpha_max,epsilon_max)
            End_time = time.perf_counter()
            print("Time for Lagrangian: ",(End_time - Start_time))
            print('Epsilon ')
            print(epsilon_vector)
            print('Epsilon Added')
            print(pos_merged_list_n_copied)
            t_max_u,tsum = calculateTmax_ruc_QR_l1(pos_merged_list_n_copied)
            print('T_MAX After perturbation: ',t_max_u)
            temp = {'target_tau_max':c_t_max,'epsilon_max':epsilon_max,
                    'alpha_max':alpha_max,'time':(End_time - Start_time),
                    'reached_tau_max':t_max_u,"perturbation_array": [epsilon_vector]}
            performance_result.append(temp)

performance_result_frame = pd.DataFrame(performance_result)
performance_result_frame.to_csv('performance_largangian_t_max_U.csv')


performance_result = []
for alpha_max in tqdm(alpha_max_array,desc='progress for Lagrangian TMIN'):
    for epsilon_max in epsilon_max_array:
        for  c_t_min in target_tau_min_array:
            print("Original List")
            print(neg_merged_list_n_mr)
            neg_merged_list_n_mr_copied = [neg_merged_list_n_mr[i] for i in range(0, len(neg_merged_list_n_mr))]  # Creating a new array
            neg_merged_list_n_mr_copied.sort(reverse=True)
            print("Sorted List")
            print(neg_merged_list_n_mr_copied)
            # t_max,tsum_max = calculateTmax_ruc_QR_l1(pos_merged_list_n_copied)
            # t_min,tsum_min = calculateTmin_ruc_QR_l1(neg_merged_list_n)
            # print('T_MAX: ',t_max,' T_Min: ',t_min)
            type = 1 # 0 means run for tmax otherwise run for tmin
            Start_time = time.perf_counter()
            epsilon_vector = get_epsilon_w_t_std_limit_cons_alpha(neg_merged_list_n_mr_copied,c_t_min, type,alpha_max,epsilon_max)
            End_time = time.perf_counter()
            print("Time for Lagrangian: ",(End_time - Start_time))
            print('Epsilon ')
            print(epsilon_vector)
            print('Epsilon Added')
            print(neg_merged_list_n_mr_copied)
            t_min_u,tsum = calculateTmin_ruc_QR_l1(neg_merged_list_n_mr_copied)
            print('T_MIN After perturbation: ',t_min_u)
            temp = {'target_tau_min':c_t_min,'epsilon_max':epsilon_max,
                    'alpha_max':alpha_max,'time':(End_time - Start_time),
                    'reached_tau_min':t_min_u,"perturbation_array": [epsilon_vector]}
            performance_result.append(temp)

performance_result_frame = pd.DataFrame(performance_result)
performance_result_frame.to_csv('performance_largangian_t_min.csv')

#endregion
#region Function For FGAV
def get_cost_function(residual_array,org_limit):
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction = [0 for i in range(len(residual_array))]
    for l in range(len(residual_array)):
        if (abs(residual_array[l]) <= abs(org_limit)):
            costSum += abs(org_limit - residual_array[l]) / 2
            cost_count = cost_count + 1
        else:
            pSum += abs(org_limit - residual_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] = abs(costSum - pSum) / (cost_count + penalty_count)
    return costFunction

def get_Gradient_sort(index_of_sorted_list,residual_array):
    sorted_list = [0 for i in range(0,len(residual_array))] #Declaring a sorted inital vector
    for i in range(len(index_of_sorted_list)): #fetch the index and corresponding residual to get the sorted list
        sorted_list[i] = residual_array[index_of_sorted_list[i]]
    return sorted_list

def get_eps_fgav_w_cons_alpha(sorted_ruc,target_tau,type,alpha_max,epsilon_max):
    epsilon_vector = [0 for i in range(0,len(sorted_ruc))] #Declaring a epsilon vector
    is_target_reached = False
    eps = 0
    eps_step = epsilon_max/1000
    while (True):
        is_stopping_criteria_met = check_for_stopping_criteria(epsilon_vector,is_target_reached,alpha_max,epsilon_max)
        if(is_stopping_criteria_met == True):break
        eps = eps + eps_step
        for i in range(alpha_max):
            if(type == 0):
                sorted_ruc[i] = sorted_ruc[i] + eps
            else:
                sorted_ruc[i] = sorted_ruc[i] - eps

            epsilon_vector[i] = epsilon_vector[i] + eps
            if (type == 0):
                t_max_u, t_sum = calculateTmax_ruc_QR_l1(sorted_ruc)
                # print('tau_max: ', t_max_u)
                if (abs(t_max_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
            else:
                t_min_u, t_sum = calculateTmin_ruc_QR_l1(sorted_ruc)
                # print('tau_min: ', t_min_u)
                if (abs(t_min_u) >= abs(target_tau)):
                    is_target_reached = True
                    break
    return epsilon_vector
#endregion
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

#region Compile and Single Run FGAV
# taget_tau_max = 0.7 #Can be of any value
print("Original List")
print(pos_merged_list_n_copied)
tmax_org =  0.05
tmin_org =  -0.05042896139729035
cost_function = get_cost_function(pos_merged_list_n_copied,tmax_org)
grad_index_list,gradients = calculate_gradients(cost_function,pos_merged_list_n_copied)
pos_merged_list_n_sorted = get_Gradient_sort(grad_index_list,pos_merged_list_n_copied)
print("FGAV Sorted List")
print(pos_merged_list_n_sorted)
type = 0 # 0 means run for tmax otherwise run for tmin
Start_time = time.perf_counter()
epsilon_vector = get_eps_fgav_w_cons_alpha(pos_merged_list_n_sorted, taget_tau_max, type,ALPHA_MAX,EPSILON_MAX)
End_time = time.perf_counter()
print("Time for FGAV: ",(End_time - Start_time))
# update_pos_ruc = add_epsilon(pos_merged_list_n_sorted,epsilon_vector)
print('Epsilon ')
print(epsilon_vector)
print('Epsilon Added')
print(pos_merged_list_n_sorted)
t_max_u,tsum1 = calculateTmax_ruc_QR_l1(pos_merged_list_n_sorted)
print('T_MAX: ',t_max_u,' tsum: ',tsum1)
#endregion SI single run
#region Compile and multiple RUN FGAV

performance_result = []
for alpha_max in tqdm(alpha_max_array,desc='progress for FGAV TMAX'):
    for epsilon_max in epsilon_max_array:
        for  c_t_max in target_tau_max_array:
            pos_merged_list_n_copied = [pos_merged_list_n_mr[i] for i in range(0, len(pos_merged_list_n_mr))]  # Creating a new array
            print("Original List")
            print(pos_merged_list_n_copied)
            tmax_org = 0.05
            tmin_org = -0.05042896139729035
            cost_function = get_cost_function(pos_merged_list_n_copied, tmax_org)
            grad_index_list, gradients = calculate_gradients(cost_function, pos_merged_list_n_copied)
            pos_merged_list_n_sorted = get_Gradient_sort(grad_index_list, pos_merged_list_n_copied)
            print("FGAV Sorted List")
            print(pos_merged_list_n_sorted)
            type = 0  # 0 means run for tmax otherwise run for tmin
            Start_time = time.perf_counter()
            epsilon_vector = get_eps_fgav_w_cons_alpha(pos_merged_list_n_sorted, c_t_max, type,alpha_max,epsilon_max)
            End_time = time.perf_counter()
            print("Time for FGAV: ", (End_time - Start_time))
            # update_pos_ruc = add_epsilon(pos_merged_list_n_sorted,epsilon_vector)
            print('Epsilon ')
            print(epsilon_vector)
            print('Epsilon Added')
            print(pos_merged_list_n_sorted)
            t_max_u, tsum1 = calculateTmax_ruc_QR_l1(pos_merged_list_n_sorted)
            print('T_MAX: ', t_max_u, ' tsum: ', tsum1)
            temp = {'target_tau_max':c_t_max,'epsilon_max':epsilon_max,
                    'alpha_max':alpha_max,'time':(End_time - Start_time),
                    'reached_tau_max':t_max_u,"perturbation_array": [epsilon_vector]}
            performance_result.append(temp)

performance_result_frame = pd.DataFrame(performance_result)
performance_result_frame.to_csv('performance_fgav_t_max_U.csv')


#performance Result for Negative Residuals
performance_result = []
for alpha_max in tqdm(alpha_max_array,desc='progress for FGAV TMIN'):
    for epsilon_max in epsilon_max_array:
        for  c_t_min in target_tau_min_array:
            neg_merged_list_n_mr_copied = [neg_merged_list_n_mr[i] for i in range(0, len(neg_merged_list_n_mr))]  # Creating a new array
            print("Original List")
            print(neg_merged_list_n_mr_copied)
            tmax_org = 0.05
            tmin_org = -0.05042896139729035
            cost_function = get_cost_function(neg_merged_list_n_mr_copied, tmin_org)
            grad_index_list, gradients = calculate_gradients(cost_function, neg_merged_list_n_mr_copied)
            neg_merged_list_n_mr_sorted = get_Gradient_sort(grad_index_list, neg_merged_list_n_mr_copied)
            print("FGAV Sorted List")
            print(neg_merged_list_n_mr_sorted)
            type = 1  # 0 means run for tmax otherwise run for tmin
            Start_time = time.perf_counter()
            epsilon_vector = get_eps_fgav_w_cons_alpha(neg_merged_list_n_mr_sorted, c_t_min, type,alpha_max,epsilon_max)
            End_time = time.perf_counter()
            print("Time for FGAV: ", (End_time - Start_time))
            # update_pos_ruc = add_epsilon(pos_merged_list_n_sorted,epsilon_vector)
            print('Epsilon ')
            print(epsilon_vector)
            print('Epsilon Added')
            print(neg_merged_list_n_mr_sorted)
            t_min_u, tsum1 = calculateTmin_ruc_QR_l1(neg_merged_list_n_mr_sorted)
            print('T_MIN: ', t_min_u, ' tsum: ', tsum1)
            temp = {'target_tau_min':c_t_min,'epsilon_max':epsilon_max,
                    'alpha_max':alpha_max,'time':(End_time - Start_time),
                    'reached_tau_min':t_min_u,"perturbation_array": [epsilon_vector]}
            performance_result.append(temp)

performance_result_frame = pd.DataFrame(performance_result)
performance_result_frame.to_csv('performance_fgav_t_min.csv')

#endregion
