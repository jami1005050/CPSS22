import pandas as pd
import matplotlib.pyplot as plt
performance_fgav = pd.read_csv('performance_fgav_t_max_U.csv')
performance_lagrangian = pd.read_csv('performance_largangian_t_max_U.csv')
merged_frame = pd.merge( performance_fgav, performance_lagrangian,
                         on=["target_tau_max","alpha_max","epsilon_max"])
# print(merged_frame.columns)
# print(merged_frame[merged_frame['time_x']>merged_frame['time_y']])
# print(merged_frame[(merged_frame['reached_tau_max_x']-merged_frame['reached_tau_max_y'])>0]
#       [['reached_tau_max_y','reached_tau_max_x','epsilon_max','alpha_max','target_tau_max']])
plot_frame = merged_frame[(merged_frame['epsilon_max']==merged_frame['epsilon_max'].max())&
                   (merged_frame['target_tau_max']==0.20)]

plt.bar(plot_frame['alpha_max'], plot_frame['time_x'], color='r')
plt.bar(plot_frame['alpha_max'], plot_frame['time_y'], color='g')
plt.ylabel('Execution Time(Seconds)')
plt.xlabel('Alpha')
plt.legend(labels=['FGAV-MAX', 'LAGRANGIAN-MAX'])
plt.show()


plt.bar(plot_frame['alpha_max'], plot_frame['reached_tau_max_y'], color='g')
plt.bar(plot_frame['alpha_max'], plot_frame['reached_tau_max_x'], color='b')

plt.ylabel('Standard Limit')
plt.xlabel('Alpha')

plt.legend(labels=[ 'LAGRANGIAN-MAX','FGAV-MAX'])
plt.show()

performance_fgav_min = pd.read_csv('performance_fgav_t_min.csv')
performance_lagrangian_min = pd.read_csv('performance_largangian_t_min.csv')
merged_frame_min = pd.merge( performance_fgav_min, performance_lagrangian_min,
                         on=["target_tau_min","alpha_max","epsilon_max"])
# print(merged_frame.columns)
# print(merged_frame[merged_frame['time_x']>merged_frame['time_y']])
# print(merged_frame[(merged_frame['reached_tau_max_x']-merged_frame['reached_tau_max_y'])>0]
#       [['reached_tau_max_y','reached_tau_max_x','epsilon_max','alpha_max','target_tau_max']])
plot_frame_min = merged_frame_min[(merged_frame_min['epsilon_max']==merged_frame_min['epsilon_max'].max())&
                   (merged_frame_min['target_tau_min']==-0.20)]

plt.bar(plot_frame_min['alpha_max'], plot_frame_min['time_x'], color='r')
plt.bar(plot_frame_min['alpha_max'], plot_frame_min['time_y'], color='g')
plt.ylabel('Execution Time(Seconds)')
plt.xlabel('Alpha')

plt.legend(labels=['FGAV-MIN', 'LAGRANGIAN-MIN'])
plt.show()


plt.bar(plot_frame_min['alpha_max'], plot_frame_min['reached_tau_min_y']*(-1), color='g')
plt.bar(plot_frame_min['alpha_max'], plot_frame_min['reached_tau_min_x']*(-1), color='b')

plt.ylabel('Standard Limit')
plt.xlabel('Alpha')

plt.legend(labels=[ 'LAGRANGIAN-MIN','FGAV-MIN'])
plt.show()