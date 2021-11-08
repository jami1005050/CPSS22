import pandas as pd
fa_frame_sa = pd.read_csv('SA_FA_MD_RO_8_EPS_0069_CR_DEL_90.csv')
fa_frame_ra = pd.read_csv('RA_FA_MD_DEL150_ROMAL03_CR_DEL_100.csv')
def get_cost(fa_frame):
    fa_frame['cost_c'] = None
    fa_frame['cost_h'] = None
    for index,row in fa_frame.iterrows():
        fa_frame.at[index,'cost_c'] = row.md_c*0.3+ row.fa_c*0.7
        fa_frame.at[index,'cost_h'] = row.md_h*0.3 + row.fa_h*0.7
    return fa_frame

def get_opt_beta_c(cost_frame):
    flag = 1
    min_beta_c = None
    max_beta_c = None
    min_c = None
    for index,row in cost_frame.iterrows():
        if(flag == 1):
            min_beta_c = row.beta_p
            max_beta_c = row.beta_n
            min_c = row.cost_c
            flag = 0
        else:
            if(row.cost_c<min_c):
                min_c = row.cost_c
                min_beta_c = row.beta_p
                max_beta_c = row.beta_n
    return max_beta_c,min_beta_c

def get_opt_beta_h(cost_frame):
    flag = 1
    min_beta_h = None
    max_beta_h = None
    min_h = None
    for index,row in cost_frame.iterrows():
        if(flag == 1):
            min_beta_h = row.beta_p
            max_beta_h = row.beta_n
            min_h = row.cost_h
            flag = 0
        else:
            if(row.cost_h<min_h):
                min_h = row.cost_h
                min_beta_h = row.beta_p
                max_beta_h = row.beta_n
    return max_beta_h,min_beta_h
cost_frame_sa = get_cost(fa_frame_sa)
max_beta_c_sa,min_beta_c_sa = get_opt_beta_c(cost_frame_sa)
max_beta_h_sa,min_beta_h_sa = get_opt_beta_h(cost_frame_sa)
cost_frame_ra = get_cost(fa_frame_ra)
max_beta_c_ra,min_beta_c_ra = get_opt_beta_c(cost_frame_ra)
max_beta_h_ra,min_beta_h_ra = get_opt_beta_h(cost_frame_ra)
print("Cauchy OPT BETA RA: ",max_beta_c_ra,min_beta_c_ra)
print("Cauchy OPT BETA SA: ",max_beta_c_sa,min_beta_c_sa)
print("Huber OPT BETA RA: ",max_beta_h_ra,min_beta_h_ra)
print("Huber OPT BETA SA: ",max_beta_h_sa,min_beta_h_sa)
print("Values for Smart Attack: Cauchy  ")
print(cost_frame_sa [(cost_frame_sa['beta_p'] == max_beta_c_sa) &
                     (cost_frame_sa['beta_n'] == min_beta_c_sa)][['tau_max_c','tau_min_c']])
print("Values for Adversarial Attack:  Cauchy ")
print(cost_frame_ra [(cost_frame_ra['beta_p'] == max_beta_c_ra) &
                     (cost_frame_ra['beta_n'] == min_beta_c_ra)][['tau_max_c','tau_min_c']])

print("Values for Smart Attack: Huber  ")

print(cost_frame_sa [(cost_frame_sa['beta_p'] == max_beta_h_sa) &
                     (cost_frame_sa['beta_n'] == min_beta_h_sa)][['tau_max_h','tau_min_h']])

print("Values for Adversarial Attack:  Huber ")

print(cost_frame_ra [(cost_frame_ra['beta_p'] == max_beta_h_ra) &
                     (cost_frame_ra['beta_n'] == min_beta_h_ra)][['tau_max_h','tau_min_h']])