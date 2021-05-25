import json

from test_QP.functions_QR_CLN import *
import random
# random.seed(42)
tau_dict = {1.0:{'tau_max': 0.005, 'tau_min': -0.0038691378044811986},
            1.25:{ 'tau_max': 0.0025, 'tau_min': -0.0029683815875770903},
            1.5:{ 'tau_max': 0.0025, 'tau_min': -0.004567625370672981},
            1.75:{ 'tau_max': 0.0075, 'tau_min': -0.006166869153768871},
            2.0: {'tau_max': 0.0125, 'tau_min': -0.012766112936864759},
            2.25:{ 'tau_max': 0.0125, 'tau_min': -0.01186535671996054},
            2.5:{ 'tau_max': 0.01, 'tau_min': -0.010964600503056431}}
result = {}
for key in tau_dict.keys():
    result[key] = {}
    ruc_frame = pd.read_csv('cleaned_res/training_RUC_mad_'+str(key)+'csv')
    num_of_RUC_Pos1 = len(ruc_frame[ruc_frame['ruc2014'] > 0])
    num_of_RUC_Pos2 = len(ruc_frame[ruc_frame['ruc2015'] > 0])
    total_RUC_Pos = num_of_RUC_Pos1 + num_of_RUC_Pos2
    num_of_RUC_Neg1 = len(ruc_frame[ruc_frame['ruc2014'] < 0])
    num_of_RUC_Neg2 = len(ruc_frame[ruc_frame['ruc2015'] < 0])
    total_RUC_Neg = num_of_RUC_Neg1 + num_of_RUC_Neg2
    min_RUC_count = min(total_RUC_Neg,total_RUC_Pos)
    ROMAX_ARR = []
    for i in range(0, 5):
        n = random.randint(0, min_RUC_count)
        ROMAX_ARR.append(n)
    print(ROMAX_ARR)
    for romax in ROMAX_ARR:
        result[key][romax] = {}
        for epsilon in EPSILON_ARR:
            ruc_frame1,tmin = get_loss_for_contraint_romax_min_QR_CLN(ruc_frame, TRAINING_DATA.keys(),tau_dict[key]['tau_min'],romax,epsilon)
            ruc_frame2,tmax = get_loss_for_contraint_romax_max_QR_CLN(ruc_frame, TRAINING_DATA.keys(),tau_dict[key]['tau_max'],romax,epsilon)
            result[key][romax][epsilon] = {'tau_max':tmax,'tau_min':tmin}
            print('tmax: ',tmax," tmin: ",tmin)
            merged_array1 = ruc_frame1
            for x in ruc_frame2:
                merged_array1.append(x)
            df1 = pd.DataFrame(merged_array1,columns=['ruc'])
            # df1.to_csv('FGAV_QL1_RO_'+str(romax)+'_EPS'+str(epsilon)+'_K'+str(key)+'_.csv')
        break
    break

# with open("poison.json", "w") as outfile:
#     json.dump(result, outfile)
