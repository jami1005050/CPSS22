import json

from test_QP.functions_QR_CLN import *

standard_limit = {
    1.0: {'upper_limit': 0.0075, 'lower_limit': -0.008869137804481196},
    1.25: {'upper_limit': 0.0075, 'lower_limit': -0.007968381587577088},
    1.5:{'upper_limit': 0.01, 'lower_limit': -0.009567625370672978},
    1.75: {'upper_limit': 0.0125, 'lower_limit': -0.011166869153768869},
    2.0:{'upper_limit': 0.015, 'lower_limit': -0.015266112936864758},
    2.25: {'upper_limit': 0.0125, 'lower_limit': -0.014365356719960538},
    2.5: {'upper_limit': 0.0125, 'lower_limit': -0.01346460050305643}
}

Epsilon_A = [0.012840280834311983, 0.01887443094669175, 0.02490858105907152,
             0.03094273117145129, 0.03697688128383106,0.04301103139,0.0490451815,
             0.05507933161,0.06111348172,0.06714763183]
tau_max_K2 = 0.015
tau_min_K2 = -0.015266112936864758
result = {}
r_max = [2,4,6]
for ro in r_max:
    result[ro] = {}
    for epsilon in Epsilon_A:
        result[ro][epsilon] = {}
        ruc_frame = pd.read_csv('cleaned_res/training_RUC_mad_2.0csv')
        ruc_frame1,tmin = get_loss_for_contraint_romax_min_QR_CLN_L2(ruc_frame, TRAINING_DATA.keys(),tau_min_K2,ro,epsilon)
        ruc_frame2,tmax = get_loss_for_contraint_romax_max_QR_CLN_L2(ruc_frame, TRAINING_DATA.keys(),tau_max_K2,ro,epsilon)
        print('tmax: ',tmax," tmin: ",tmin)
        result[ro][epsilon] = {'tau_max': tmax, 'tau_min': tmin}
        merged_array1 = ruc_frame1
        for x in ruc_frame2:
            merged_array1.append(x)
        df1 = pd.DataFrame(merged_array1,columns=['ruc'])
        # df1.to_csv('FGAV_QL1_RO_'+str(ro)+'_EPS'+str(epsilon)+'_K2_.csv')


with open("poison_tau_K2_L2.json", "w") as outfile:
    json.dump(result, outfile)
