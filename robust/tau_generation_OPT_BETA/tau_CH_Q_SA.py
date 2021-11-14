#Cauchy Huber Tau generation for Quantile version 11-14-21-- JAMI

import utils
import pandas as pd
import matplotlib.pyplot as plt
import json

from utility.constant import BETA_ARR

loss_function = 'huber'  # l2 huber pseudo_huber
f = open('../../test_QP/result/standard_limit/poison.json')

# returns JSON object as
# a dictionary
#Order of the key kappa--> romax--> epsilon--> beta
poisoning_std_limits = json.load(f)
rob_poisoin_limit ={}
for key in poisoning_std_limits.keys():
    rob_poisoin_limit[key] = {}
    for key2 in poisoning_std_limits[key].keys():
        rob_poisoin_limit[key][key2] = {}
        for key3 in poisoning_std_limits[key][key2].keys():
            rob_poisoin_limit[key][key2][key3] = {}
            data = pd.DataFrame()
            ruc_frame_attacked = pd.read_csv('../test_QP/poison_res_new/FGAV_QL1_RO_'+str(key2)+'_EPS'+str(key3)+'_K'+str(key)+'_.csv')
            data['ruc2014'] = ruc_frame_attacked['ruc']
            keys = ['2014']
            min_candidate1 = data['ruc2014'].min()
            max_candidate1 = data['ruc2014'].max()
            for beta in BETA_ARR:
                attack_t_max, attack_t_max_loss_list, attack_t_max_list = getattr(utils,
                                                                                  'calculate_t_max_' + loss_function)(
                    data, keys,
                    tau_range=[.0, max_candidate1, .0025],
                    w1=.5, w2=2., b=beta)
                attack_t_min, attack_t_min_loss_list, attack_t_min_list = getattr(utils,
                                                                                  'calculate_t_min_' + loss_function)(
                    data, keys,
                    tau_range=[min_candidate1, .0, .0025],
                    w1=.5, w2=2., b=beta)
                rob_poisoin_limit[key][key2][key3][beta] = {'tau_max':attack_t_max,'tau_min':attack_t_min}

with open("../../test_H/result/standard_limit/robust_poison_H.json", "w") as outfile:
    json.dump(rob_poisoin_limit, outfile)

tau_dict = {1.0:{'tau_max': 0.005, 'tau_min': -0.0038691378044811986},
            1.25:{ 'tau_max': 0.0025, 'tau_min': -0.0029683815875770903},
            1.5:{ 'tau_max': 0.0025, 'tau_min': -0.004567625370672981},
            1.75:{ 'tau_max': 0.0075, 'tau_min': -0.006166869153768871},
            2.0: {'tau_max': 0.0125, 'tau_min': -0.012766112936864759},
            2.25:{ 'tau_max': 0.0125, 'tau_min': -0.01186535671996054},
            2.5:{ 'tau_max': 0.01, 'tau_min': -0.010964600503056431}}

rob_res_benign = {}
#order of the key is kappa --> beta
for key in tau_dict.keys():
    rob_res_benign[key] = {}
    ruc_frame = pd.read_csv('../test_QP/cleaned_res/training_RUC_mad_'+str(key)+'csv')
    # ruc_frame_training = pd.read_csv('../data/t_RUC_benign/training_RUC_2.5csv')
    keys_TR = ['2014','2015']
    minRuc2014 = ruc_frame['ruc2014'].min()
    minRuc2015 = ruc_frame['ruc2015'].min()
    min_candidate = min(minRuc2015, minRuc2014)
    maxRuc2014 = ruc_frame['ruc2014'].max()
    maxRuc2015 = ruc_frame['ruc2015'].max()
    max_candidate = max(maxRuc2015, maxRuc2014)
    for beta in BETA_ARR:
        train_t_max, train_t_max_loss_list, train_t_max_list = getattr(utils, 'calculate_t_max_' + loss_function)(
                                                                       ruc_frame, keys_TR,
                                                                       tau_range=[.0, max_candidate, .0025],
                                                                       w1=.5, w2=2., b=beta)
        train_t_min, train_t_min_loss_list, train_t_min_list = getattr(utils, 'calculate_t_min_' + loss_function)(
                                                                       ruc_frame,  keys_TR,
                                                                       tau_range=[min_candidate, .0, .0025],
                                                                       w1=.5, w2=2., b=beta)
        rob_res_benign[key][beta] = {'tau_max':train_t_max,'tau_min':train_t_min}


with open("../../test_H/result/standard_limit/robust_benign_H.json", "w") as outfile:
    json.dump(rob_res_benign, outfile)


# print('training_tau_max: {:.4f}'.format(train_t_max))
# print('training_tau_min: {:.4f}'.format(train_t_min))
# print('attacked_tau_max: {:.4f}'.format(attack_t_max))
# print('attacked_tau_min: {:.4f}'.format(attack_t_min))

# plt.impact_analysis(train_t_max_list, train_t_max_loss_list, 'b-')
# plt.impact_analysis(attack_t_max_list, attack_t_max_loss_list, 'r-')
# plt.title('Training-Attacked $\\tau_{max}$')
# plt.xlabel('$\\tau$')
# plt.ylabel('Loss')
# # plt.ylim((0, 1))
# plt.legend(('Training', 'Attacked'), loc='lower right')
# plt.show()
#
# # plt.impact_analysis(train_t_min_list, train_t_min_loss_list, 'b-')
# plt.impact_analysis(attack_t_min_list, attack_t_min_loss_list, 'r-')
# plt.title('Training-Attacked $\\tau_{min}$')
# plt.xlabel('$\\tau$')
# plt.ylabel('Loss')
# # plt.ylim((0, 1))
# plt.legend(('Training', 'Attacked'), loc='lower right')
# plt.show()
#
# # plt.impact_analysis(ruc_frame_training["day"], ruc_frame_training["ruc2014"], '.b--')
# # plt.impact_analysis(ruc_frame_training["day"], ruc_frame_training["ruc2015"], '^r--')
# # plt.hlines(train_t_max, 0, 365, linestyles='dashed')
# # plt.hlines(train_t_min, 0, 365, linestyles='dashed')
# # plt.xlabel('Days')
# # plt.ylabel('RUC')
# # plt.legend(('2014', '2015'), loc='lower right')
# # plt.show()
#
# # rucFrame_attack = pd.read_csv('attacked_residual.csv')
# # plt.impact_analysis(ruc_frame_training["day"], ruc_frame_training["ruc2014"], '.b--')
# # plt.impact_analysis(ruc_frame_attacked["day"], ruc_frame_attacked["ruc2014"], '^r--')
# # plt.hlines(train_t_max, 0, 365, linestyles='dashed')
# # plt.hlines(train_t_min, 0, 365, linestyles='dashed')
# # plt.xlabel('Days')
# # plt.ylabel('RUC')
# # plt.legend(('Honest 2014', 'Attacked 2014'), loc='lower right')
# # plt.show()
#
# # plt.impact_analysis(ruc_frame_training["day"], ruc_frame_training["ruc2015"], '.b--')
# # plt.impact_analysis(ruc_frame_attacked["day"], ruc_frame_attacked["ruc2015"], '^r--')
# # plt.hlines(train_t_max, 0, 365, linestyles='dashed')
# # plt.hlines(train_t_min, 0, 365, linestyles='dashed')
# # plt.xlabel('Days')
# # plt.ylabel('RUC')
# # plt.legend(('Honest 2015', 'Attacked 2015'), loc='lower right')
# # plt.show()
#
# LOSS_FUNC = 'cauchy'
# labels = ['Training $\\tau_{{max}}$ ({:s})'.format(LOSS_FUNC),
#           'Attacked $\\tau_{{max}}$ ({:s})'.format(LOSS_FUNC),
#           'Training $\\tau_{{min}}$ ({:s})'.format(LOSS_FUNC),
#           'Attacked $\\tau_{{min}}$ ({:s})'.format(LOSS_FUNC), ]
# plt.rcParams["figure.figsize"] = 8, 6
# fig = plt.figure()
#
# ax = plt.subplot(111)
# ax.hlines(train_t_max, 0, 1, colors='red', linestyles='solid')
# ax.hlines(attack_t_max, 0, 1, colors='green', linestyles='solid')
# ax.hlines(train_t_min, 0, 1, colors='blue', linestyles='solid')
# ax.hlines(attack_t_min, 0, 1, colors='yellow', linestyles='solid')
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
# ax.legend(labels[0:4], bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()
