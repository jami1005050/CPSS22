fa_days_Q = [18, 19, 24, 25]
fa_days_C = [17, 18, 19, 23, 24, 25, 26, 27, 28]
fa_days_H = [18, 24]

S_Q = 0
S_C = 0
S_H = 0
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