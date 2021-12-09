import json
import pandas as pd

#FGAV attack type
FA_QC = open('../../test_C/result_data/false_alarm/FA_QC.json')
FA_NQC = open('../../test_C/result_data/false_alarm/FA_NQC.json')
FA_QH = open('../../test_H/result/false_alarm/FA_QH.json')
FA_NQH = open('../../test_H/result/false_alarm/FA_NQH.json')
FA_Q = open('../../test_QP/result/false_alarm/FA_Q.json')
eQC = json.load(FA_QC)
eNQC = json.load(FA_NQC)
eQH = json.load(FA_QH)
eNQH = json.load(FA_NQH)
eQL1 = json.load(FA_Q)
result_CQ = []
for key in eQC.keys():
    for key1 in eQC[key].keys():
        fa_C = eQC[key][key1]['0.006']['false_alarm']
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
        temp = {'romax':key,'epsilon':key1,'Efa_QC':Efa_Q}
        result_CQ.append(temp)
result_CNQ = []
for key in eNQC.keys():
    for key1 in eNQC[key].keys():
        fa_Q = eNQC[key][key1]['0.006']['false_alarm']
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
        temp = {'romax':key,'epsilon':key1,'Efa_NQC':Efa_Q}
        result_CNQ.append(temp)
result_HQ = []
for key in eQH.keys():
    for key1 in eQH[key].keys():
        fa_Q = eQH[key][key1]['0.006']['false_alarm']
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
        temp = {'romax':key,'epsilon':key1,'Efa_H':Efa_Q}
        result_HQ.append(temp)
result_NHQ = []
for key in eNQH.keys():
    for key1 in eNQH[key].keys():
        fa_Q = eNQH[key][key1]['0.006']['false_alarm']
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
        temp = {'romax':key,'epsilon':key1,'Efa_NQH':Efa_Q}
        result_NHQ.append(temp)
result_Ql1 = []
for key in eQL1.keys():
    for key1 in eQL1[key].keys():
        fa_Q = eQL1[key][key1]['false_alarm']
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
        temp = {'romax':key,'epsilon':key1,'Efa_QL1':Efa_Q}
        result_Ql1.append(temp)
#012840280834311983  #06714763183
result_frame_QL1 = pd.DataFrame(result_Ql1)
result_frame_CQ = pd.DataFrame(result_CQ)
result_frame_CNQ = pd.DataFrame(result_CNQ)
result_frame_HQ = pd.DataFrame(result_HQ)
result_frame_NHQ = pd.DataFrame(result_NHQ)
print(result_frame_QL1[(result_frame_QL1['romax']==str(6)) &  (result_frame_QL1['epsilon']==str(0.012840280834311983))])
print(result_frame_CQ[(result_frame_CQ['romax']==str(6)) &  (result_frame_CQ['epsilon']==str(0.012840280834311983))])
print(result_frame_CNQ[(result_frame_CNQ['romax']==str(6)) &  (result_frame_CNQ['epsilon']==str(0.012840280834311983))])
print(result_frame_HQ[(result_frame_HQ['romax']==str(6)) &  (result_frame_HQ['epsilon']==str(0.012840280834311983))])
print(result_frame_NHQ[(result_frame_NHQ['romax']==str(6)) &  (result_frame_NHQ['epsilon']==str(0.012840280834311983))])


print("Medium Scale attack")

print(result_frame_QL1[(result_frame_QL1['romax']==str(2)) &  (result_frame_QL1['epsilon']==str(0.06714763183))])
print(result_frame_CQ[(result_frame_CQ['romax']==str(2)) &  (result_frame_CQ['epsilon']==str(0.06714763183))])
print(result_frame_CNQ[(result_frame_CNQ['romax']==str(2)) &  (result_frame_CNQ['epsilon']==str(0.06714763183))])
print(result_frame_HQ[(result_frame_HQ['romax']==str(2)) &  (result_frame_HQ['epsilon']==str(0.06714763183))])
print(result_frame_NHQ[(result_frame_NHQ['romax']==str(2)) &  (result_frame_NHQ['epsilon']==str(0.06714763183))])

