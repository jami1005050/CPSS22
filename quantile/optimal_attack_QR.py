import matplotlib.pyplot as plt
import pandas as pd
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
ruc_frame = pd.read_csv('../data/training_residual.csv')
y1,target1 = get_loss_for_fix_target_min_QR(ruc_frame, TRAINING_DATA.keys())
# df = pd.DataFrame(y1,columns=['loss'])
# df.to_csv('l1_QR_Loss_t_33.csv')
# ruc_frame_array = calculate_min_by_gradient(ruc_frame,TRAINING_DATA.keys())
# pd.DataFrame(ruc_frame_array).to_csv("../loss_minimization/ruc_for_l1_fgav.csv")

x = numpy.arange(len(y1))
plt.plot(x, y1, color='r', label='l1-FGAV', marker ='X',markevery = 5) # r - red colour
plt.axvline(x=target1, color='k',label='Target FGSV', linestyle='--')

plt.xlabel("Number of RUC ")
plt.ylabel("Loss")
plt.legend()
plt.show()


