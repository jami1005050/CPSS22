import matplotlib.pyplot as plt
# import pandas as pd
import numpy
from quantile.functions_QR import *
SMALL_SIZE = 8
MEDIUM_SIZE = 18
BIGGER_SIZE = 36

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
# mpl.rcParams['agg.path.chunksize'] = 10000
ruc_frame = pd.read_csv('../data/training_residual/training_residual.csv')
# sorted_frame_min = dict()
# day_frame_array_min = []
# rucFrame_array_min = []
# sorted_frame_max = dict()
# day_frame_array_max = []
# rucFrame_array_max = []
# # y1,target1 = get_loss_for_fix_target_min_QR(ruc_frame, TRAINING_DATA.keys())
# for key in TRAINING_DATA.keys():
#     difference = dict()
#     sorted_frame_min[key] = ruc_frame.sort_values(by=["ruc" + key])
#     sorted_non_zero_ruc = sorted_frame_min[key][sorted_frame_min[key]['ruc' + key] < float(0)]
#     # data_frame_array.append(sorted_non_zero_ruc)
#     day_values = sorted_non_zero_ruc['day'].values
#     day_frame_array_min.append(day_values)
#     non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
#     rucFrame_array_min.append(non_zero_ruc_array)
# merged_array_min = rucFrame_array_min[0].tolist()
# for x in rucFrame_array_min[1]:
#     merged_array_min.append(x)
# minThreshold,minSum,tao_min,loss_min = calculateTmin_ruc_QR(merged_array_min)
# t = []
# for item in tao_min:
#     t.append(item*(-1))
# index, grad = calculate_gradients_signed(loss_min,t)
# print(len(grad))
# for key in TRAINING_DATA.keys():
#     difference = dict()
#     sorted_frame_max[key] = ruc_frame.sort_values(by=["ruc" + key],ascending=False)
#     sorted_non_zero_ruc = sorted_frame_max[key][sorted_frame_max[key]['ruc' + key] > float(0)]
#     # data_frame_array.append(sorted_non_zero_ruc)
#     day_values = sorted_non_zero_ruc['day'].values
#     day_frame_array_max.append(day_values)
#     non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
#     rucFrame_array_max.append(non_zero_ruc_array)
# merged_array_max = rucFrame_array_max[0].tolist()
# for x in rucFrame_array_max[1]:
#     merged_array_max.append(x)
# maxThreshold1, maxSum,tao_max,loss_max = calculateTmax_ruc_QR(merged_array_max)
# index1, grad1 = calculate_gradients_signed(loss_max,tao_max)
# print(len(grad1))
# print("Min threshold: ",minThreshold," Max threshold: ",maxThreshold1)
# ruc_frame3 = get_loss_for_contraint_romax_min_QR_signed(ruc_frame, TRAINING_DATA.keys())
ruc_frame1 = get_loss_for_contraint_romax_min_QR(ruc_frame, TRAINING_DATA.keys())
# ruc_frame5 = get_loss_for_contraint_romax_min_QR_RUC_order(ruc_frame, TRAINING_DATA.keys())
# pd.DataFrame(ruc_frame_array).to_csv("../data/residual_l1_fgsv.csv")
# ruc_frame4 = get_loss_for_contraint_romax_max_QR_signed(ruc_frame, TRAINING_DATA.keys())
ruc_frame2 = get_loss_for_contraint_romax_max_QR(ruc_frame, TRAINING_DATA.keys())
# ruc_frame6 = get_loss_for_contraint_romax_max_QR_RUC_order(ruc_frame, TRAINING_DATA.keys())
merged_array = ruc_frame1
for x in ruc_frame2:
    merged_array.append(x)
df = pd.DataFrame(merged_array,columns=['ruc'])
df.to_csv('LQR_ROMAX50_EPS07_FGAV.csv')
# ruc_frame_array = calculate_min_by_gradient(ruc_frame,TRAINING_DATA.keys())
# pd.DataFrame(ruc_frame_array).to_csv("../loss_minimization/ruc_for_l1_fgav.csv")

# x = numpy.arange(len(y1))
# plt.plot(tao_max, grad1, color='r', label='TAO-Max', marker ='X',markevery = 5) # r - red colour
# plt.plot(t, grad, color='b', label='TAO-Min', marker ='X',markevery = 5) # r - red colour
# plt.plot(x, grad1, color='r', label='l1-FGAV', marker ='X',markevery = 5) # r - red colour
# plt.axvline(x=target1, color='k',label='Target FGSV', linestyle='--')

# plt.xlabel("Tao Max ")
# plt.ylabel("DLoss/DTao")
# plt.legend()
# plt.show()
#

