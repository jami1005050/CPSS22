fa_days_Q = [14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
fa_days_C = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
fa_days_H = [17, 18, 19, 23, 24, 25, 26, 27, 28]
fa_QC = [305, 306]
fa_NQC = [228, 229, 235, 236, 305, 306, 330, 346, 361]
S_Q = 0
S_C = 0
S_H = 0

S_QC = 0
S_NQC = 0
for i in range(len(fa_days_Q)):
    if(i==0):
        S_Q+= fa_days_Q[i] - 1
        continue
    S_Q+=fa_days_Q[i]-fa_days_Q[i-1]
    # print(S_Q)
    i+=1
S_Q+= 365 - fa_days_Q[len(fa_days_Q)-1]
print(S_Q/(len(fa_days_Q)-1))

for i in range(len(fa_days_C)):
    if(i==0):
        S_C+= fa_days_C[i] - 1
        continue
    S_C+=fa_days_C[i]-fa_days_C[i-1]
    i+=1
S_C+= 365 - fa_days_C[len(fa_days_C)-1]
print(S_C/(len(fa_days_C)-1))

for i in range(len(fa_days_H)):
    if(i==0):
        S_H+= fa_days_H[i] - 1
        continue
    S_H+=fa_days_H[i]-fa_days_H[i-1]
    i+=1
S_H+= 365 - fa_days_H[len(fa_days_H)-1]
print(S_H/(len(fa_days_H)-1))

if (len(fa_QC) > 1):
    T_btw_FA = 0
    for i in range(len(fa_QC)):
        if (i == 0):
            T_btw_FA += fa_QC[i] - 1
            continue
        T_btw_FA += fa_QC[i] - fa_QC[i - 1]
        i += 1
    T_btw_FA += 365 - fa_QC[len(fa_QC) - 1]
    Efa_QC = T_btw_FA / (len(fa_QC) - 1)
else:
    Efa_QC = 365

if (len(fa_NQC) > 1):
    T_btw_FA = 0
    for i in range(len(fa_NQC)):
        if (i == 0):
            T_btw_FA += fa_NQC[i] - 1
            continue
        T_btw_FA += fa_NQC[i] - fa_NQC[i - 1]
        i += 1
    T_btw_FA += 365 - fa_NQC[len(fa_NQC) - 1]
    Efa_NQC = T_btw_FA / (len(fa_NQC) - 1)
else:
    Efa_NQC = 365

print(Efa_QC,' ',Efa_NQC)