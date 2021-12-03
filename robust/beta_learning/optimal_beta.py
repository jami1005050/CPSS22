import pandas as pd
import sys
fa_frame_sa = pd.read_csv('RA_TR150_TE100_ROMAL03_CH.csv')
# fa_frame_ra = pd.read_csv('RA_FA_MD_DEL150_ROMAL03_CR_DEL_175_C.csv')
def get_cost(fa_frame):
    fa_frame['cost_c'] = None
    fa_frame['cost_h'] = None
    for index,row in fa_frame.iterrows():
        fa_frame.at[index,'cost_c'] = row.md_c*0.3+ row.fa_c*0.7
        fa_frame.at[index,'cost_h'] = row.md_h*0.3 + row.fa_h*0.7
    return fa_frame

def get_opt_beta_c(cost_frame):
    # flag = 1
    min_beta_c = None
    max_beta_c = None
    tau_min_c = None
    tau_max_c = None
    min_c = sys.float_info.max
    for index,row in cost_frame.iterrows():
        # if(flag == 1):
        #     min_beta_c = row.beta_p
        #     max_beta_c = row.beta_n
        #     min_c = row.cost_c
        #     flag = 0
        # else:
        if (row.cost_c < min_c)   :#& (row.tau_max_c != 0) & (row.tau_min_c != 0)& (row.beta_p!=0) & (row.beta_n!=0)
            print(' *** ', row.cost_c, min_c, row.tau_max_c, row.tau_min_c)
            min_c = row.cost_c
            min_beta_c = row.beta_p
            max_beta_c = row.beta_n
            tau_max_c = row.tau_max_c
            tau_min_c = row.tau_min_c
    return max_beta_c, min_beta_c, tau_max_c, tau_min_c

def get_opt_beta_h(cost_frame):
    # flag = 1
    min_beta_h = None
    max_beta_h = None
    tau_min_h = None
    tau_max_h = None
    min_h = sys.float_info.max
    for index,row in cost_frame.iterrows():
        # if(flag == 1):
        #     min_beta_h = row.beta_p
        #     max_beta_h = row.beta_n
        #     min_h = row.cost_h
        #     flag = 0
        # else:
        if(row.cost_h<min_h)  : #& (row.tau_max_h!=0) & (row.tau_min_h!=0) & (row.beta_p!=0) & (row.beta_n!=0)
            print(' *** ',row.cost_h,min_h,row.tau_max_h,row.tau_min_h)
            min_h = row.cost_h
            min_beta_h = row.beta_p
            max_beta_h = row.beta_n
            tau_max_h = row.tau_max_h
            tau_min_h = row.tau_min_h
    return max_beta_h,min_beta_h,tau_max_h,tau_min_h
cost_frame_sa = get_cost(fa_frame_sa)
max_beta_c_sa,min_beta_c_sa,tau_max_c,tau_min_c  = get_opt_beta_c(cost_frame_sa)
max_beta_h_sa,min_beta_h_sa,tau_max_h,tau_min_h = get_opt_beta_h(cost_frame_sa)
# cost_frame_ra = get_cost(fa_frame_ra)
# max_beta_c_ra,min_beta_c_ra = get_opt_beta_c(cost_frame_ra)
# max_beta_h_ra,min_beta_h_ra = get_opt_beta_h(cost_frame_ra)
# print("Cauchy OPT BETA RA: ",max_beta_c_ra,min_beta_c_ra)
print("Cauchy OPT BETA SA: ",max_beta_c_sa,min_beta_c_sa,tau_max_c,tau_min_c)
# print("Huber OPT BETA RA: ",max_beta_h_ra,min_beta_h_ra)
print("Huber OPT BETA SA: ",max_beta_h_sa,min_beta_h_sa,tau_max_h,tau_min_c)

