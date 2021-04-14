import pandas as pd
import matplotlib.pyplot as plt

SMALL_SIZE = 8
MEDIUM_SIZE = 14
BIGGER_SIZE = 30

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

under_attack = pd.read_csv('../data/loss_vs_std_limit_l1_fgav.csv', names=['std_limit', 'loss'], header=None)
under_attack_fgsv = pd.read_csv('../data/loss_vs_std_limit_l1_fgsv.csv', names=['std_limit', 'loss'], header=None)
plt.plot(under_attack['std_limit'], under_attack['loss'],marker = "D", markevery=5)
plt.plot(under_attack_fgsv['std_limit'], under_attack_fgsv['loss'],marker = ">", markevery=5)
plt.xlabel("Standard limit")
plt.ylabel("Loss")
plt.legend(["L1 FGAV Attack","L1 FGSV Attack"])
plt.show()
