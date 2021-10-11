import pandas as pd
fa_frame_sa = pd.read_csv('false_alarm_missed_detection_ro6_eps055_large_beta.csv')
fa_frame_ra = pd.read_csv('false_alarm_missed_detection_DEL100_ROMAL03_large_beta.csv')
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
