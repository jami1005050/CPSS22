import pandas as pd
det_RA_L1 = pd.read_csv('det_RA_L1_ded.csv')
det_RA_L2 = pd.read_csv('det_RA_L2_ded.csv')
det_SA_L1 = pd.read_csv('det_SA_L1_ded.csv')
det_SA_L2 = pd.read_csv('det_SA_L2_ded.csv')

fa_ra_ar_l1 = []
f_ra_l1 = det_RA_L1[ det_RA_L1['day_detected'] == 0].groupby('del_avg_tr')
for index, group in f_ra_l1:
    # print(index)
    max_del = max(group['del_avg_te'].tolist())
    temp = group[group['del_avg_te'] == max_del]
    index_ar = temp.index
    ob = {'del_avg_tr':index,'del_avg_te':temp.at[index_ar[0],'del_avg_te'],'ro_mal':temp.at[index_ar[0],'ro_mal']}
    fa_ra_ar_l1.append(ob)
fa_ra_ar_frame_l1 = pd.DataFrame(fa_ra_ar_l1)
fa_ra_ar_frame_l1.to_csv('RA_NDA_L1.csv')
print(fa_ra_ar_frame_l1)


fa_ra_ar_l2 = []
f_ra_l2 = det_RA_L2[ det_RA_L2['day_detected'] == 0].groupby('del_avg_tr')
for index, group in f_ra_l2:
    # print(index)
    max_del = max(group['del_avg_te'].tolist())
    temp = group[group['del_avg_te'] == max_del]
    index_ar = temp.index
    ob = {'del_avg_tr': index, 'del_avg_te': temp.at[index_ar[0], 'del_avg_te'],
          'ro_mal': temp.at[index_ar[0], 'ro_mal']}
    fa_ra_ar_l2.append(ob)
fa_ra_ar_frame_l2 = pd.DataFrame(fa_ra_ar_l2)
fa_ra_ar_frame_l2.to_csv('RA_NDA_L2.csv')
print(fa_ra_ar_frame_l2)


# f_sa_l1 = det_SA_L1[ det_SA_L1['day_detected'] == 0].groupby('del_avg_tr')
# f_sa_l2 = det_SA_L2[ det_SA_L2['day_detected'] == 0].groupby('del_avg_tr')
# print(f_ra_l1)