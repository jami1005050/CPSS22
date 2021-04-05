from utility.constant import *
import matplotlib.pyplot as plt
import pandas as pd
from linear.functions_LR import *
import numpy
SMALL_SIZE = 8
MEDIUM_SIZE = 18
BIGGER_SIZE = 36

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
ruc_frame = pd.read_csv('../data/training_residual.csv')
y1,target1 = get_loss_for_fixed_target_min_LR(ruc_frame, TRAINING_DATA.keys())
x = numpy.arange(len(y1))
plt.plot(x, y1, color='r', label='l1-FGAV', marker ='X',markevery = 5) # r - red colour
plt.xlabel("Number of RUC ")
plt.ylabel("Loss")
plt.legend()
plt.show()
