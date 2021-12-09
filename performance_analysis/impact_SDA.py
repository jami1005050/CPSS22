import matplotlib.ticker
import matplotlib.pyplot as plt
import json
import pandas as pd
import matplotlib
#impact_x m4m6 impact_y m7m9 impact m10m12
SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    #

impact_l1_ded = pd.read_csv('impact_SA_l1_ded_M4M12_Frame.csv')
impact_l2_ded = pd.read_csv('impact_SA_l2_ded_M4M12_Frame.csv')
impact_Q_C_ded = pd.read_csv('impact_SA_QC_ded_M4M12_Frame.csv')
impact_NQ_C_ded = pd.read_csv('impact_SA_NQC_ded_M4M12_Frame.csv')
impact_Q_H_ded = pd.read_csv('impact_SA_QH_ded_M4M12_Frame.csv')
impact_NQ_H_ded = pd.read_csv('impact_SA_NQH_ded_M4M12_Frame.csv')

impact_l1_ded['impact_m'] = impact_l1_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_l2_ded['impact_m']= impact_l2_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_C_ded['impact_m'] = impact_Q_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_C_ded['impact_m'] = impact_NQ_C_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_Q_H_ded['impact_m'] = impact_Q_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)
impact_NQ_H_ded['impact_m'] = impact_NQ_H_ded[['impact_x', 'impact_y','impact']].mean(axis=1)

# print(impact_NQ_C_ded[impact_NQ_C_ded['impact_m'] >impact_NQ_H_ded['impact_m']])
impactl1ded_VDTE = impact_l1_ded[( impact_l1_ded['ro_max'] == 32 )&
                                 (impact_l1_ded['epsilon'] == 0.00035)&
                                 ( impact_l1_ded['ro_mal'] == 0.40)&
                                 (impact_l1_ded['del_avg_te'] <120)]#
impactl2ded_VDTE = impact_l2_ded[( impact_l2_ded['ro_max'] == 32)&
                                 (impact_l2_ded['epsilon'] == 0.00035)&
                                 ( impact_l2_ded['ro_mal'] == 0.40)&
                                 (impact_l2_ded['del_avg_te'] <120)]
impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 32 )&
                                  (impact_Q_C_ded['epsilon'] == 0.00060)&
                                  ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                  (impact_Q_C_ded['del_avg_te'] <120)]
impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 32 )&
                                   (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.30)&
                                   (impact_NQ_C_ded['del_avg_te'] <120)]
impactQHded_VDTE = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 32)&
                                  (impact_Q_H_ded['epsilon'] == 0.00035)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.40)&
                                  (impact_Q_H_ded['del_avg_te'] <120)]
impactNQHded_VDTE = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 32) &
                                    (impact_NQ_H_ded['epsilon'] == 0.00060)&
                                    (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                    (impact_NQ_H_ded['del_avg_te'] <120)
                                    ]

print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_max'].unique().tolist())
print(impact_NQ_C_ded[(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['ro_mal'].unique().tolist())
print(impact_NQ_C_ded[(impact_NQ_C_ded['ro_max']>=20)&(impact_NQ_C_ded['impact_m'] < impact_Q_C_ded['impact_m'])]['epsilon'].value_counts()) #['epsilon'].unique().tolist()
#
# plt.plot(impactl1ded_VDTE['del_avg_te'],impactl1ded_VDTE['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# plt.plot(impactl2ded_VDTE['del_avg_te'],impactl2ded_VDTE['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
plt.plot(impactQCded_VDTE['del_avg_te'],impactQCded_VDTE['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
plt.plot(impactNQCded_VDTE['del_avg_te'],impactNQCded_VDTE['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# plt.plot(impactQHded_VDTE['del_avg_te'],impactQHded_VDTE['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# plt.plot(impactNQHded_VDTE['del_avg_te'],impactNQHded_VDTE['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
plt.xlabel(r'Evasion Strength($\delta_{avg}^{(te)}$)')
plt.ylabel('Impact(USD)')
plt.legend()
plt.show()
#region bar--plot LS

impactl1ded_VDTE = impact_l1_ded[( impact_l1_ded['ro_max'] == 24 )&
                                 (impact_l1_ded['epsilon'] == 0.0001)&
                                 ( impact_l1_ded['ro_mal'] == 0.30)&
                                 (impact_l1_ded['del_avg_te'] ==60)]['impact_m'].tolist()#
impactl2ded_VDTE = impact_l2_ded[( impact_l2_ded['ro_max'] == 24)&
                                 (impact_l2_ded['epsilon'] == 0.0001)&
                                 ( impact_l2_ded['ro_mal'] == 0.30)&
                                 (impact_l2_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactQCded_VDTE = impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 32 )&
                                  (impact_Q_C_ded['epsilon'] == 0.00060)&
                                  ( impact_Q_C_ded['ro_mal'] == 0.40)&
                                  (impact_Q_C_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactNQCded_VDTE= impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 32 )&
                                   (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                   ( impact_NQ_C_ded['ro_mal'] == 0.30)&
                                   (impact_NQ_C_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactQHded_VDTE = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 24)&
                                  (impact_Q_H_ded['epsilon'] == 0.0001)&
                                  ( impact_Q_H_ded['ro_mal'] == 0.30)&
                                  (impact_Q_H_ded['del_avg_te'] ==60)]['impact_m'].tolist()
impactNQHded_VDTE = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 32) &
                                    (impact_NQ_H_ded['epsilon'] == 0.00060)&
                                    (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                    (impact_NQ_H_ded['del_avg_te'] ==60)
                                    ]['impact_m'].tolist()
# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VDTE[0],impactl2ded_VDTE[0],impactQCded_VDTE[0],impactQHded_VDTE[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])

plt.bar(["NQC","NQH"],
        [impactNQCded_VDTE[0],impactNQHded_VDTE[0]],
        color=['tab:green','tab:olive'])

# plt.bar(["QC","NQC"],
#         [impactQCded_VDTE[0],impactNQCded_VDTE[0]],
#         color=[ 'cyan','tab:green'])
plt.ylabel('Impact(USD)')
plt.ylim(50,70)
# plt.legend()
plt.show()



#endregion


impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 10 )&
                                   (impact_l1_ded['epsilon'] == 0.00485)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] < 140)]#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 10)&
                                   (impact_l2_ded['epsilon'] == 0.00485)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] < 140)]
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 16 )&
                                   (impact_Q_C_ded['epsilon'] == 0.0036)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 16 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00485)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]#&( impact_NQ_C_ded['del_avg_te']< 140)]
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 10)&
                                    (impact_Q_H_ded['epsilon'] == 0.00485)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] < 140)]
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 16) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0036)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                      (( impact_NQ_H_ded['del_avg_te']< 140)&( impact_NQ_H_ded['del_avg_te']>=60))]

# plt.plot(impactl1ded_VROMAL['del_avg_te'],impactl1ded_VROMAL['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# plt.plot(impactl2ded_VROMAL['del_avg_te'],impactl2ded_VROMAL['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VROMAL['del_avg_te'],impactQCded_VROMAL['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VROMAL['del_avg_te'],impactNQCded_VROMAL['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# # plt.plot(impactQHded_VROMAL['del_avg_te'],impactQHded_VROMAL['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# # plt.plot(impactNQHded_VROMAL['del_avg_te'],impactNQHded_VROMAL['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Evasion Strength$\delta_{te}$')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()
#region bar--plot MS

impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 10 )&
                                   (impact_l1_ded['epsilon'] == 0.00485)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] == 90)]['impact_m'].tolist()#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 10)&
                                   (impact_l2_ded['epsilon'] == 0.00485)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] == 90)]['impact_m'].tolist()
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 16 )&
                                   (impact_Q_C_ded['epsilon'] == 0.0036)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_NQ_C_ded['del_avg_te']< 140)&( impact_NQ_C_ded['del_avg_te']>=60))]['impact_m'].tolist()
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 16 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00485)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']==90))]['impact_m'].tolist()
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 10)&
                                    (impact_Q_H_ded['epsilon'] == 0.00485)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] == 90)]['impact_m'].tolist()
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 16) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0036)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.40)&
                                      (( impact_NQ_H_ded['del_avg_te']==90))]['impact_m'].tolist()

# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VROMAL[0],impactl2ded_VROMAL[0],impactQCded_VROMAL[0],impactQHded_VROMAL[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])

# plt.bar(["QC","NQC"],
#         [impactQCded_VROMAL[0],impactNQCded_VROMAL[0]],
#         color=[ 'cyan','tab:green'])
# plt.ylabel('Impact(USD)')
# # plt.ylim(80,160)
# # plt.legend()
# plt.show()


#endregion


impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 4 )&
                                   (impact_l1_ded['epsilon'] == 0.0156)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] < 140)]#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 4)&
                                   (impact_l2_ded['epsilon'] == 0.0156)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] < 140)]
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 4 )&
                                   (impact_Q_C_ded['epsilon'] == 0.00060)&
                                   (impact_Q_C_ded['ro_mal'] == 0.30)&
                                   (( impact_Q_C_ded['del_avg_te']< 150)&( impact_Q_C_ded['del_avg_te']>60))]
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 4 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      (( impact_NQ_C_ded['del_avg_te']< 150)&( impact_NQ_C_ded['del_avg_te']>60))]
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 4)&
                                    (impact_Q_H_ded['epsilon'] == 0.0156)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] < 140)]
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 4) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0156)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                      (impact_NQ_H_ded['del_avg_te'] < 140)]


#(impact_Q_C_ded['ro_max']==4)&

# plt.plot(impactl1ded_VROMAL['del_avg_te'],impactl1ded_VROMAL['impact_m'],label = 'L1',linestyle = '--',dashes =(5,1),marker = 'o')
# plt.plot(impactl2ded_VROMAL['del_avg_te'],impactl2ded_VROMAL['impact_m'],label = 'L2',linestyle = ':',dashes =(5,1),marker = '<')
# plt.plot(impactQCded_VROMAL['del_avg_te'],impactQCded_VROMAL['impact_m'],label = 'QC',linestyle = '-.',dashes =(5,1),marker = '>')
# plt.plot(impactNQCded_VROMAL['del_avg_te'],impactNQCded_VROMAL['impact_m'],label = 'NQC',linestyle = '--',dashes =(10,1),marker='o')
# # plt.plot(impactQHded_VROMAL['del_avg_te'],impactQHded_VROMAL['impact_m'],label = 'QH',linestyle = '--',dashes =(10,2),marker = 'v')
# # plt.plot(impactNQHded_VROMAL['del_avg_te'],impactNQHded_VROMAL['impact_m'],label = 'NQH',linestyle = '--',dashes =(5,2),marker='D')
# plt.xlabel(r'Evasion Strength ($\delta_{te}$)')
# plt.ylabel('Impact(USD)')
# plt.legend()
# plt.show()

#region bar--plot SA
impactl1ded_VROMAL = impact_l1_ded[( impact_l1_ded['ro_max'] == 4 )&
                                   (impact_l1_ded['epsilon'] == 0.0156)&
                                   (impact_l1_ded['ro_mal'] == 0.30)&
                                   ( impact_l1_ded['del_avg_te'] == 60)]['impact_m'].tolist()#
impactl2ded_VROMAL = impact_l2_ded[( impact_l2_ded['ro_max'] == 4)&
                                   (impact_l2_ded['epsilon'] == 0.0156)&
                                   (impact_l2_ded['ro_mal'] == 0.30)&
                                   ( impact_l2_ded['del_avg_te'] == 60)]['impact_m'].tolist()
impactQCded_VROMAL= impact_Q_C_ded[( impact_Q_C_ded['ro_max'] == 4 )&
                                   (impact_Q_C_ded['epsilon'] == 0.00060) &
                                   (impact_Q_C_ded['ro_mal'] == 0.30) &
                                   (impact_Q_C_ded['del_avg_te'] == 100)]['impact_m'].tolist()
impactNQCded_VROMAL = impact_NQ_C_ded[( impact_NQ_C_ded['ro_max'] == 4 )&
                                      (impact_NQ_C_ded['epsilon'] == 0.00060)&
                                      (impact_NQ_C_ded['ro_mal'] == 0.30)&
                                      ( impact_NQ_C_ded['del_avg_te']== 100)]['impact_m'].tolist()
impactQHded_VROMAL = impact_Q_H_ded[( impact_Q_H_ded['ro_max'] == 4)&
                                    (impact_Q_H_ded['epsilon'] == 0.0156)&
                                    (impact_Q_H_ded['ro_mal'] == 0.30)&
                                    ( impact_Q_H_ded['del_avg_te'] == 60)]['impact_m'].tolist()
impactNQHded_VROMAL = impact_NQ_H_ded[(impact_NQ_H_ded['ro_max'] == 4) &
                                      (impact_NQ_H_ded['epsilon'] == 0.0156)&
                                      (impact_NQ_H_ded['ro_mal'] == 0.30)&
                                      (impact_NQ_H_ded['del_avg_te'] == 60)]['impact_m'].tolist()

# plt.bar(["QL1","QL2","QC","QH"],
#         [impactl1ded_VROMAL[0],impactl2ded_VROMAL[0],impactQCded_VROMAL[0],impactQHded_VROMAL[0]],
#         color=[ 'violet','blue','cyan','tab:orange'])
#
# plt.bar(["QC","NQC"],
#         [impactQCded_VROMAL[0],impactNQCded_VROMAL[0]],
#         color=['cyan', 'tab:green'])#'tab:olive'
# plt.ylabel('Impact(USD)')
# plt.ylim(90,115)
# # plt.legend()
# plt.show()

#endregion barplot--sa
