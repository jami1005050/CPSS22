import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

impact_nonQ = pd.read_csv('scaled_nonQ.csv')
impact_Q = pd.read_csv('scaled_Q.csv')
print(impact_nonQ)
# ['romax','epsilon','del_avg','impact_C','impact_Q','impact_H','Efa_Q','Efa_C','Efa_H']
dictionary = impact_nonQ[['romax','epsilon','del_avg','impact_C','impact_Q','impact_H','Efa_Q','Efa_C','Efa_H']].to_dict()
print(dictionary)

file_name = "../../data/test_ruc/test_residual_random_attack/Test_RUC_PWith_100Del_100_M7M9.csv"
ruc_frame = pd.read_csv(file_name)
array = np.arange(len(ruc_frame['ruc2016']))
# "0.006": {"tau_max": 0.005, "tau_min": -0.004282239270649808},# "100":{"tau_max": 0.01, "tau_min": -0.009282239270649875}
# "0.006": {"tau_max": 0.0125, "tau_min": -0.011782239270649805},

plt.plot(array, ruc_frame['ruc2016'],marker='^',markevery = 20)
plt.axhline(y=0.0125, color='g', linestyle='--',  dashes =(5,5),label = 'T max QC')
plt.axhline(y=-0.011782239270649805, color='g', linestyle='-.', label = 'T min QC')
plt.axhline(y=0.005, color='r', linestyle=':',label = 'T max Non QC')
plt.axhline(y=-0.004282239270649808, color='r', linestyle='--', dashes = (10,5), label = 'T min Non QC')
plt.xlabel("Number of RUC ")
plt.ylabel("RUC")
plt.legend()
plt.show()