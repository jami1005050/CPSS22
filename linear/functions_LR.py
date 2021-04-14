import sys
from functools import reduce
import os as o
from utility.common import *
# -0.0275 0.0275 l1 #-0.0425 0.0425 l2
lower_limit_LR = -0.0425
upper_limit_LR = 0.0425

def calculateTmax_ruc_LR(rucFrame):
    global maxThreshold
    maxSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0025, .500, 0.0025):
        costSum = 0
        costCount = 0
        for row in rucFrame:
            if (row > 0):
                costSum += abs(taoThreshold - row)
                # costSum += pow(abs(taoThreshold - row),2)
                costCount = costCount + 1
        taoSumDiff = abs(costSum)
        difference[taoThreshold] = taoSumDiff
        if (maxSum > taoSumDiff):
            maxSum = taoSumDiff
            maxThreshold = taoThreshold
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    return maxThreshold,maxSum

def calculateTmin_ruc_LR(rucFrame):
    global minThreshold
    minSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0025, .500, 0.0025):
        costSum = 0
        for row in rucFrame:
            if (row < 0):
                costSum += abs(taoThreshold*(-1) - row)
                # costSum += pow(abs(taoThreshold*(-1) - row),2)
        taoSumDiff = abs(costSum)
        difference[taoThreshold] = taoSumDiff
        if (minSum > taoSumDiff):
            minSum = taoSumDiff
            minThreshold = taoThreshold * (-1)
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    # w = csv.writer(open("../plot_helper/under_attack_loss_l2_fgsv.csv", "w"))
    # for key, val in difference.items():
    #     w.writerow([key, val])
    # x, y = zip(*lists)  # unpack a list of pairs into two tuples
    #
    # fig = plt.figure()
    # plt.plot(x, y)
    # # fig.suptitle('Cost - Penalty Plotting', fontsize=20)
    # plt.xlabel('Standard Limit')
    # plt.ylabel('Loss')
    # # fig.savefig('test.jpg')
    # plt.show()
    # print(minThreshold)
    return minThreshold,minSum

def calculateTmax_LR(rucFrame, keys):
    global maxThreshold
    maxSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0000, .500, 0.0025):
        costSum = 0
        for row in rucFrame.itertuples():
            for key in keys:
                if (getattr(row, "ruc" + key) > 0):  # previously It was greater equal
                    costSum += abs(taoThreshold - getattr(row, "ruc" + key))
                    # costSum += pow(abs(taoThreshold - getattr(row, "ruc" + key)),2)
        difference[taoThreshold] = costSum
        if (maxSum > costSum):
            maxSum = costSum
            maxThreshold = taoThreshold
    # lists = (difference.items())  # sorted by key, return a list of tuples
    # x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # plt.plot(x, y)
    # plt.xlabel('Standard Limit')
    # plt.ylabel('Loss')
    # # plt.show()
    # plt.suptitle("TAO MAX")
    return maxThreshold

def calculateTmin_LR(rucFrame, keys):
    global minThreshold
    minSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0025, .500, 0.0025):
        costSum = 0
        for row in rucFrame.itertuples():
            for key in keys:
                if (getattr(row, "ruc" + key) < 0):
                   costSum += abs(taoThreshold*(-1) - getattr(row, "ruc" + key))
                   # costSum += pow(abs(taoThreshold*(-1) - getattr(row, "ruc" + key)),2)
        difference[taoThreshold*(-1)] = costSum
        if (minSum > costSum):
            minSum = costSum
            minThreshold = taoThreshold * (-1)
    # lists = (difference.items())  # sorted by key, return a list of tuples
    # x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # plt.plot(x, y)
    # plt.xlabel('Standard Limit')
    # plt.ylabel('Loss')
    # # plt.show()
    # plt.suptitle("TAO MIN")
    return minThreshold

def get_loss_for_fixed_target_min_LR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    std_limit_array = []
    loss_array = []
    rucFrame_array = []
    target_t_min = -0.17
    target_ruc_num = 0
    is_visited = False
    day_frame_array = []
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    print("Days")
    print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        costSum += abs(lower_limit_LR - merged_array[l])
        # costSum += pow(abs(lower_limit_LR - merged_array[l]),2)
        costFunction[l] =  abs(costSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        if(gradients[index_of_sorted_list[i]]<0):
            sign = (-1)*1
        else:sign = 1
        costSum = 0
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.15
        tmin, minSum  = calculateTmin_ruc_LR(non_zero_ruc_array_copied)
        std_limit_array.append(tmin*(-1))
        loss_array.append(minSum)
        if((tmin < target_t_min) and (is_visited == False)):
            is_visited = True
            target_ruc_num = i
            print("For altering: ", i ,"Number of RUCs from ",len(non_zero_ruc_array_copied)," we can reach the targeted max")
        for l in range(len(non_zero_ruc_array_copied)):
            costSum += abs(lower_limit_LR - non_zero_ruc_array_copied[l])
            # costSum += pow(abs(lower_limit_LR - non_zero_ruc_array_copied[l]),2)
        difference[i] = costSum
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    print("taget ruc number: ",target_ruc_num)
    df = pd.DataFrame(std_limit_array,columns=['std_limit'])
    df1 = pd.DataFrame(loss_array,columns=['loss'])
    merged_fr = pd.concat([df['std_limit'],df1['loss']],axis = 1, keys = ['std_limit','loss'])
    print(merged_fr)
    # merged_fr.to_csv("std_LR_l1.csv")
    return y,target_ruc_num

def get_loss_for_contraint_romax_min_LR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    print("Days")
    print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        costSum += abs(lower_limit_LR - merged_array[l])
        # costSum += pow(abs(lower_limit_LR - merged_array[l]),2)
        costFunction[l] =  abs(costSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        if(ruc_count >= ROMAX):
            tmin, minSum = calculateTmin_ruc_LR(non_zero_ruc_array_copied)
            print("After Romax Tao Min: ",tmin)
            break
        if(gradients[index_of_sorted_list[i]]<0):
            sign = (-1)*1
        else:sign = 1
        costSum = 0
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.07
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - 0.05451427573
        ruc_count = ruc_count + 1
        for l in range(len(non_zero_ruc_array_copied)):
            costSum += abs(lower_limit_LR - non_zero_ruc_array_copied[l])
            # costSum += pow(abs(lower_limit_LR - non_zero_ruc_array_copied[l]),2)
        difference[i] = costSum
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples

def get_loss_for_contraint_romax_max_LR(rucFrame, keys):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    day_frame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        day_values = sorted_non_zero_ruc['day'].values
        day_frame_array.append(day_values)
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    day_array = day_frame_array[0].tolist()
    for x in day_frame_array[1]:
        day_array.append(x)
    print("Days")
    print(day_array)
    for x in rucFrame_array[1]:
        merged_array.append(x)
    # print("length merged: ",len(merged_array)," lenght 1: ",len(rucFrame_array[0])," length 2: ",len(rucFrame_array[1]))
    costSum = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        costSum += abs(upper_limit_LR - merged_array[l])
        # costSum += pow(abs(lower_limit_LR - merged_array[l]),2)
        costFunction[l] =  abs(costSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        if(ruc_count >= ROMAX):
            tmax, maxSum = calculateTmax_ruc_LR(non_zero_ruc_array_copied)
            print("After Romax Tao Max: ",tmax)
            break
        if(gradients[index_of_sorted_list[i]]<0):
            sign = (-1)*1
        else:sign = 1
        costSum = 0
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.07
        # non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + 0.05451427573
        ruc_count = ruc_count + 1
        for l in range(len(non_zero_ruc_array_copied)):
            costSum += abs(upper_limit_LR - non_zero_ruc_array_copied[l])
            # costSum += pow(abs(lower_limit_LR - non_zero_ruc_array_copied[l]),2)
        difference[i] = costSum
    lists = (difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples



