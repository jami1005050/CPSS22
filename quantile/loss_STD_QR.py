from quantile.functions_QR import *

ruc_FGAV_constrained = pd.read_csv('l1_QR_ruc_romax_50_epslion_0.07_FGAV.csv')
ruc_FGAV_unconstrained = pd.read_csv('l1_QR_ruc_romax_unconstrained_epslion_0.07_FGAV.csv')
ruc_arr_CON = ruc_FGAV_constrained['ruc'].tolist()
ruc_arr_UCON = ruc_FGAV_unconstrained['ruc'].tolist()
training_unperturbed  = pd.read_csv('../data/training_ruc/t_RUC_benign/training_residual.csv')
training_unperturbed_list_2014 = training_unperturbed['ruc2014'].tolist()
training_unperturbed_list_2015 = training_unperturbed['ruc2015'].tolist()
merged_array = training_unperturbed_list_2014
for x in training_unperturbed_list_2015:
    merged_array.append(x)
print(training_unperturbed)
# calculateTmin_ruc_QR(ruc_arr_CON)
calculateTmin_ruc_QR(ruc_arr_UCON)
# calculateTmin_ruc_QR(merged_array)
# calculateTmax_ruc_QR(ruc_arr_CON)
calculateTmax_ruc_QR(ruc_arr_UCON)
# calculateTmax_ruc_QR(merged_array)