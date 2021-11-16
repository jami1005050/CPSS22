import json

from test_QP.smart_attack.functions_QR_CLN import *
import random
# random.seed(42)
tau_dict = {1.0:{'tau_max': 0.005, 'tau_min': -0.0038691378044811986},
            1.25:{ 'tau_max': 0.0025, 'tau_min': -0.0029683815875770903},
            1.5:{ 'tau_max': 0.0025, 'tau_min': -0.004567625370672981},
            1.75:{ 'tau_max': 0.0075, 'tau_min': -0.006166869153768871},
            2.0: {'tau_max': 0.0125, 'tau_min': -0.012766112936864759},
            2.25:{ 'tau_max': 0.0125, 'tau_min': -0.01186535671996054},
            2.5:{ 'tau_max': 0.01, 'tau_min': -0.010964600503056431}}
epsilon_dict = {1.0: [0.004248316276166424, 0.006076234138183988, 0.007904152000201553, 0.009732069862219118, 0.011559987724236682],
                1.25: [0.00314847869529313, 0.004589462366018326, 0.0060304460367435215, 0.007471429707468717, 0.008912413378193913],
                1.5: [0.003270970449699103, 0.004966048261960318, 0.006661126074221532, 0.008356203886482748, 0.010051281698743962],
                1.75: [0.005923812706548744, 0.009001895919225879, 0.012079979131903014, 0.015158062344580149, 0.018236145557257284],
                2.0: [0.012840280834311983, 0.01887443094669175, 0.02490858105907152, 0.03094273117145129, 0.03697688128383106],
                2.25: [0.012277308198746825, 0.0179736747297875, 0.023670041260828174, 0.02936640779186885, 0.03506277432290952],
                2.5: [0.011714335563181763, 0.017072918512883402, 0.02243150146258504, 0.027790084412286677, 0.033148667361988314]}

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
    epsilon_array = epsilon_dict[key]
    ROMAX_ARR = []
    for i in range(0, 5):
        n = random.randint(0, min_RUC_count)
        ROMAX_ARR.append(n)
    print(ROMAX_ARR)
    for romax in ROMAX_ARR:
        result[key][romax] = {}
        for epsilon in epsilon_array:
            ruc_frame1,tmin = get_loss_for_contraint_romax_min_QR_CLN(ruc_frame, TRAINING_DATA.keys(),tau_dict[key]['tau_min'],romax,epsilon)
            ruc_frame2,tmax = get_loss_for_contraint_romax_max_QR_CLN(ruc_frame, TRAINING_DATA.keys(),tau_dict[key]['tau_max'],romax,epsilon)
            result[key][romax][epsilon] = {'tau_max':tmax,'tau_min':tmin}
            print('tmax: ',tmax," tmin: ",tmin)
            merged_array1 = ruc_frame1
            for x in ruc_frame2:
                merged_array1.append(x)
            df1 = pd.DataFrame(merged_array1,columns=['ruc'])
            df1.to_csv('FGAV_QL1_RO_'+str(romax)+'_EPS'+str(epsilon)+'_K'+str(key)+'_.csv')
    #     break
    # break

with open("../../result/standard_limit/poison.json", "w") as outfile:
    json.dump(result, outfile)
