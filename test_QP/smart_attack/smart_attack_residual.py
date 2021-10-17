from test_QP.smart_attack.functions_QR_CLN import *
import statistics
#First Calculate the standard deviation of the residual
ruc_frame = pd.read_csv('../../robust/beta_learning/training_RUC_mad_2.0csv')
ruc_n1 = ruc_frame[ruc_frame['ruc2014']<0]['ruc2014'].tolist()
ruc_n2 = ruc_frame[ruc_frame['ruc2015']<0]['ruc2015'].tolist()
neg_merged_list_n = ruc_n1 + ruc_n2
print("STD N: ",statistics.stdev(neg_merged_list_n))
print("Mean N: ",statistics.mean(neg_merged_list_n))

ruc_p1 = ruc_frame[ruc_frame['ruc2014']>0]['ruc2014'].tolist()
ruc_p2 = ruc_frame[ruc_frame['ruc2015']>0]['ruc2015'].tolist()
pos_merged_list_p = ruc_p1 + ruc_p2
print("STD P: ",statistics.stdev(pos_merged_list_p))
print("Mean P: ",statistics.mean(pos_merged_list_p))
tau_min_K2 =-0.0128
tau_max_K2 = 0.0125
epsilon = 0.0069 ## mean of the residuals
ruc_frame1,tmin = get_neg_residual_SA(neg_merged_list_n,tau_min_K2,epsilon)
ruc_frame2,tmax = get_pos_residual_SA(pos_merged_list_p,tau_max_K2,epsilon)
print('tmax: ',tmax,' tmin: ',tmin)
merged_array1 = ruc_frame1
for x in ruc_frame2:
    merged_array1.append(x)
df1 = pd.DataFrame(merged_array1,columns=['ruc'])
df1.to_csv('FGAV_QL1_EPS'+str(epsilon)+'.csv')
