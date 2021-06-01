import pandas as pd
import matplotlib.pyplot as plt

SMALL_SIZE = 14
MEDIUM_SIZE = 18
BIGGER_SIZE = 36


plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.ylim(0,11)
plt.xlim(0,0.2)
not_attack = pd.read_csv('../data/loss_vs_tmin_l1.csv', names=['std_limit', 'loss'], header=None)
under_attack_constrained = pd.read_csv('../data/loss_vs_std/loss_vs_tmin_l1_fgav_CON.csv', names=['std_limit', 'loss'], header=None)
under_attack_unconstrained = pd.read_csv('../data/loss_vs_std/loss_vs_tmin_l1_fgav_UNCON_2.csv', names=['std_limit', 'loss'], header=None)
plt.plot(not_attack['std_limit'], not_attack['loss'],marker = "D", markevery=5)
# plt.impact_analysis(under_attack_constrained['std_limit'], under_attack_constrained['loss'],marker = ">", markevery=5)
plt.plot(under_attack_unconstrained['std_limit'], under_attack_unconstrained['loss'],marker = ">", markevery=5)
plt.xlabel(r'$\tau$-')
plt.ylabel("Loss")
# plt.title("Histogram of IQ: " r'$\mu = 100, \sigma$ =15')

plt.legend(["Free of Attack","L1-FGAV Unconstrained"])
plt.show()
