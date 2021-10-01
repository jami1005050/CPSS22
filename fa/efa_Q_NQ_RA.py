import sys

import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib.ticker
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #

#random attack type
fa_NQCRA = open('../test_C/result_data/false_alarm/fa_NQCRA.json')
fa_QCRA = open('../test_C/result_data/false_alarm/fa_QCRA.json')
fa_QHRA = open('../test_H/result/false_alarm/fa_QHRA.json')
fa_NQHRA = open('../test_H/result/false_alarm/fa_NQHRA.json')
fa_QRA = open('../test_QP/result/false_alarm/fa_QRA.json')

eQC = json.load(fa_QCRA)
eNQC = json.load(fa_NQCRA)
eQH = json.load(fa_QHRA)
eNQH = json.load(fa_NQHRA)
eQL1 = json.load(fa_QRA)
result_CQ = []
for key in eQC.keys():
    fa_C = eQC[key]['0.006']['false_alarm']
    if (len(fa_C) > 1):
        T_btw_FA = 0
        for i in range(len(fa_C)):
            if (i == 0):
                T_btw_FA += fa_C[i] - 1
                continue
            T_btw_FA += fa_C[i] - fa_C[i - 1]
            i += 1
        T_btw_FA += 365 - fa_C[len(fa_C) - 1]
        Efa_Q = T_btw_FA / (len(fa_C) - 1)
    else:
        Efa_Q = 365
    temp = {'del_avg':key,'Efa_QC':Efa_Q}
    result_CQ.append(temp)
result_CNQ = []
for key in eNQC.keys():
    fa_Q = eNQC[key]['0.006']['false_alarm']
    if (len(fa_Q) > 1):
        T_btw_FA = 0
        for i in range(len(fa_Q)):
            if (i == 0):
                T_btw_FA += fa_Q[i] - 1
                continue
            T_btw_FA += fa_Q[i] - fa_Q[i - 1]
            i += 1
        T_btw_FA += 365 - fa_Q[len(fa_Q) - 1]
        Efa_Q = T_btw_FA / (len(fa_Q) - 1)
    else:
        Efa_Q = 365
    temp = {'del_avg':key,'Efa_NQC':Efa_Q}
    result_CNQ.append(temp)
result_HQ = []
for key in eQH.keys():
    fa_Q = eQH[key]['0.006']['false_alarm']
    if (len(fa_Q) > 1):
        T_btw_FA = 0
        for i in range(len(fa_Q)):
            if (i == 0):
                T_btw_FA += fa_Q[i] - 1
                continue
            T_btw_FA += fa_Q[i] - fa_Q[i - 1]
            i += 1
        T_btw_FA += 365 - fa_Q[len(fa_Q) - 1]
        Efa_Q = T_btw_FA / (len(fa_Q) - 1)
    else:
        Efa_Q = 365
    temp = {'del_avg':key,'Efa_H':Efa_Q}
    result_HQ.append(temp)
result_NHQ = []
for key in eNQH.keys():
    fa_Q = eNQH[key]['0.006']['false_alarm']
    if (len(fa_Q) > 1):
        T_btw_FA = 0
        for i in range(len(fa_Q)):
            if (i == 0):
                T_btw_FA += fa_Q[i] - 1
                continue
            T_btw_FA += fa_Q[i] - fa_Q[i - 1]
            i += 1
        T_btw_FA += 365 - fa_Q[len(fa_Q) - 1]
        Efa_Q = T_btw_FA / (len(fa_Q) - 1)
    else:
        Efa_Q = 365
    temp = {'del_avg':key,'Efa_NQH':Efa_Q}
    result_NHQ.append(temp)

result_Ql1 = []
for key in eQL1.keys():
    fa_Q = eQL1[key]['false_alarm']
    if (len(fa_Q) > 1):
        T_btw_FA = 0
        for i in range(len(fa_Q)):
            if (i == 0):
                T_btw_FA += fa_Q[i] - 1
                continue
            T_btw_FA += fa_Q[i] - fa_Q[i - 1]
            i += 1
        T_btw_FA += 365 - fa_Q[len(fa_Q) - 1]
        Efa_Q = T_btw_FA / (len(fa_Q) - 1)
    else:
        Efa_Q = 365
    temp = {'del_avg':key,'Efa_QL1':Efa_Q}
    result_Ql1.append(temp)
#012840280834311983  #06714763183
result_frame_QL1 = pd.DataFrame(result_Ql1)
result_frame_CQ = pd.DataFrame(result_CQ)
result_frame_CNQ = pd.DataFrame(result_CNQ)
result_frame_HQ = pd.DataFrame(result_HQ)
result_frame_NHQ = pd.DataFrame(result_NHQ)
print(result_frame_QL1[(result_frame_QL1['del_avg']==str(100))])
print(result_frame_CQ[(result_frame_CQ['del_avg']==str(100))])
print(result_frame_CNQ[(result_frame_CNQ['del_avg']==str(100))])
print(result_frame_HQ[(result_frame_HQ['del_avg']==str(100))])
print(result_frame_NHQ[(result_frame_NHQ['del_avg']==str(100))])


