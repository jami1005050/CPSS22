import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker

SMALL_SIZE = 12
MEDIUM_SIZE = 10
BIGGER_SIZE = 30

# plt.figure(figsize=(15,15))
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
# plt.ylim(0,11)
# plt.xlim(0,0.2)
residual = pd.read_csv('../data/training_ruc/t_RUC_benign/training_residual.csv')
print(residual)
day_array = residual[(residual['day']>5)&(residual['day']<=60)]['day'].tolist()
locator = matplotlib.ticker.MultipleLocator(4)
plt.gca().xaxis.set_major_locator(locator)
plt.plot(day_array,residual[(residual['day']>5)&(residual['day']<=60)]['ruc2014'],
         marker="<", markevery=5,label = "RUC 2014",color='b')
plt.plot(day_array, residual[(residual['day']>5)&(residual['day']<=60)]['ruc2015'],
         marker=">", markevery=5,label = "RUC 2015",color='m')
plt.axhline(y=.065, color='g', label=r'$\tau$+', linestyle='--')
plt.axhline(y=-.065, color='g', label=r'$\tau$-', linestyle='-.')
plt.axhline(y=.095, color='r',label=r'$\tau$+ Poisoned', linestyle= '--', dashes=(5,8))
plt.axhline(y=-.095, color='r',label=r'$\tau$- Poisoned', linestyle=':')
plt.xlabel('Day')
plt.ylabel('RUC')
plt.legend()
plt.show()
