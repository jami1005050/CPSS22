import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


impact = {}
impact['Q'] = []
impact ['H']= []
impact ['C'] = []

#ro 10 eps 0 2
r10_e02_imp_m4m6 = {'Q': 174.1824, 'H': 199.0656, 'C': 199.0656}
r10_e02_imp_m7m9 = {'Q': 1045.0944, 'H': 1069.9776000000002, 'C': 1069.9776000000002}
r10_e02_undetected = {'Q': 50, 'H': 52, 'C': 52}
for key in r10_e02_imp_m4m6.keys():
    impact[key].append((r10_e02_imp_m7m9[key]+r10_e02_imp_m4m6[key])/(r10_e02_undetected[key]))

#ro 10 eps 06
r10_e06_imp_m7m9 = {'Q': 1045.0944, 'H': 1069.9776000000002, 'C': 1069.9776000000002}
r10_e06_imp_m4m6 = {'Q': 174.1824, 'H': 223.94879999999998, 'C': 199.0656}
r10_e06_undetected = {'Q': 50, 'H': 53, 'C': 52}
for key in r10_e06_imp_m7m9.keys():
    impact[key].append((r10_e06_imp_m7m9[key]+r10_e06_imp_m4m6[key])/(r10_e06_undetected[key]))

#ro 10 eps 12
r10_e12_imp_m7m9 = {'Q': 1069.9776000000002, 'H': 1094.8608, 'C': 1020.2112}
r10_e12_imp_m4m6 = {'Q': 223.94879999999998, 'H': 248.832, 'C': 149.29919999999998}
r10_e12_undetected = {'Q': 53, 'H': 55, 'C': 49}
for key in r10_e12_imp_m7m9.keys():
    impact[key].append((r10_e12_imp_m7m9[key]+r10_e12_imp_m4m6[key])/(r10_e12_undetected[key]))

#ro 30 eps 02
# r30_e02_imp_m7m9 = {'Q': 1045.0944, 'H': 1069.9776000000002, 'C': 1045.0944}
# r30_e02_imp_m4m6 =  {'Q': 174.1824, 'H': 199.0656, 'C': 174.1824}
# r30_e02_undetected = {'Q': 59, 'H': 52, 'C': 50}
# for key in r30_e02_imp_m7m9.keys():
#     impact[key].append((r30_e02_imp_m7m9[key]+r30_e02_imp_m4m6[key])/(r30_e02_undetected[key]))

#ro 30 eps 06
r30_e06_imp_m4m6 = {'Q': 223.94879999999998, 'H': 248.832, 'C': 174.1824}
r30_e06_imp_m7m9 = {'Q': 1069.9776000000002, 'H': 1094.8608, 'C': 1045.0944}
r30_e06_undetected = {'Q': 53, 'H': 55, 'C': 50}
for key in r30_e06_imp_m7m9.keys():
    impact[key].append((r30_e06_imp_m7m9[key]+r30_e06_imp_m4m6[key])/(r30_e06_undetected[key]))
#ro 30 eps 12
r30_e12_imp_m4m6 = {'Q': 373.248, 'H': 646.9631999999999, 'C': 398.1312}
r30_e12_imp_m7m9 = {'Q': 1094.8608, 'H': 2189.7216, 'C': 1119.744}
r30_e12_undetected = {'Q': 60, 'H': 105, 'C': 62}
for key in r30_e12_imp_m4m6.keys():
    impact[key].append((r30_e12_imp_m7m9[key]+r30_e12_imp_m4m6[key])/(r30_e12_undetected[key]))

#ro 60 eps 02
# r60_e02_imp_m7m9 = {'Q': 1393.4592, 'H': 1426.6367999999998, 'C': 1327.1039999999998}
# r60_e02_imp_m4m6 = {'Q': 232.24319999999997, 'H': 265.4208, 'C': 165.88799999999998}
# r60_e02_undetected = {'Q': 50, 'H': 52, 'C': 46}
# for key in r60_e02_imp_m7m9.keys():
#     impact[key].append((r60_e02_imp_m7m9[key]+r60_e02_imp_m4m6[key])/(r60_e02_undetected[key]))

#ro 60 eps 06
r60_e06_imp_m7m9 = {'Q': 1094.8608, 'H': 1094.8608, 'C': 1045.0944}
r60_e06_imp_m4m6 = {'Q': 248.832, 'H': 373.248, 'C': 174.1824}
r60_e06_undetected = {'Q': 55, 'H': 60, 'C': 50}
for key in r60_e06_imp_m7m9.keys():
    impact[key].append((r60_e06_imp_m7m9[key]+r60_e06_imp_m4m6[key])/(r60_e06_undetected[key]))

#ro 60 eps .12
r60_e12_imp_m7m9 = {'Q': 2189.7216, 'H': 2214.6047999999996, 'C': 1119.744}
r60_e12_imp_m4m6 = {'Q': 646.9631999999999, 'H': 671.8463999999999, 'C': 398.1312}

r60_e12_undetected = {'Q': 115, 'H': 117, 'C': 62}
for key in r60_e12_imp_m7m9.keys():
    impact[key].append((r60_e12_imp_m7m9[key]+r60_e12_imp_m4m6[key])/(r60_e12_undetected[key]))

romax = [10,10,10,30,30,60,60]
epsilon = [0.02,0.06,0.12,0.06,0.12,0.06,0.12]
print(impact['Q'])
print(impact['H'])
print(impact['C'])
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(romax, epsilon, impact['Q'], marker="D",color ="g",label='Q')
ax.plot(romax, epsilon, impact['H'],marker="<", color="b", label='H')
ax.plot(romax, epsilon, impact['C'],marker=">", color="r", label='C')

ax.set_zlim3d(24.2,24.7)
ax.legend()
plt.show()

# fig = plt.figure(figsize=(9, 9))
# ax = plt.axes(projection='3d')

# Creating color map
# my_cmap = plt.get_cmap('hot')

# Creating impact_analysis
# trisurf = ax.plot_trisurf(romax, epsilon, impact['Q'],
#                           # cmap=my_cmap,
#                           linewidth=0.2,
#                           antialiased=True,
#                           edgecolor='grey')
# fig.colorbar(trisurf, ax=ax, shrink=0.5, aspect=5)
# ax.set_title('Tri-Surface impact_analysis')
#
# # Adding labels
# ax.set_xlabel('X-axis', fontweight='bold')
# ax.set_ylabel('Y-axis', fontweight='bold')
# ax.set_zlabel('Z-axis', fontweight='bold')

# show impact_analysis
plt.show()
