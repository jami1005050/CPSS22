import pandas as pd
impact_nonQ = pd.read_csv('scaled_nonQ.csv')
impact_Q = pd.read_csv('scaled_Q.csv')
print(impact_nonQ)
['romax','epsilon','del_avg','impact_C','impact_Q','impact_H','Efa_Q','Efa_C','Efa_H']
dictionary = impact_nonQ[['romax','epsilon','del_avg','impact_C','impact_Q','impact_H','Efa_Q','Efa_C','Efa_H']].to_dict()
print(dictionary)