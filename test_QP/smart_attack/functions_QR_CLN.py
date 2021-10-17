import sys
from utility.common import *
def calculateTmax_ruc_QR(rucFrame):
    global maxThreshold1
    max_candidate = max(rucFrame)
    maxSum = sys.float_info.max
    difference = dict()
    for taoThreshold in numpy.arange(0.0000, max_candidate, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            if (row > 0):
                if (row <  taoThreshold):
                    costSum += abs(taoThreshold - row) / 2
                    costCount = costCount + 1
                else:
                    pSum += abs(taoThreshold - row) * 2
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            if (maxSum > taoSumDiff):
                maxSum = taoSumDiff
                maxThreshold1 = taoThreshold
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return maxThreshold1, maxSum

def calculateTmin_ruc_QR(rucFrame):
    global minThreshold
    minSum = sys.float_info.max
    min_candidate = min(rucFrame)
    difference = dict()
    for taoThreshold in numpy.arange(min_candidate, 0.00, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            if (row < 0):
                # print(row)
                if (row > ( taoThreshold)):
                    # temp = abs(taoThreshold*(-1) - row)/2
                    # costSum += pow(temp, 2)
                    costSum += abs(taoThreshold - row) / 2
                    costCount = costCount + 1
                else:
                    # temp = abs(taoThreshold*(-1) - row)*2
                    # pSum += pow(temp, 2)
                    pSum += abs(taoThreshold - row) * 2
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            difference[taoThreshold] = taoSumDiff
            if (minSum > taoSumDiff):
                # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold*(-1))
                minSum = taoSumDiff
                minThreshold = taoThreshold
        # print("Cost Count: ",costCount," penalty count: ",penaltyCount)
    lists = sorted(difference.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    return minThreshold,minSum

def calculateTmax_ruc_QR_L2(rucFrame):
    global maxThreshold1
    max_candidate = max(rucFrame)
    maxSum = sys.float_info.max
    for taoThreshold in numpy.arange(0.0000, max_candidate, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            if (row > 0):
                if (row <  taoThreshold):
                    temp = abs(taoThreshold - row) / 2
                    costSum += pow(temp, 2)
                    costCount = costCount + 1
                else:
                    temp = abs(taoThreshold - row) * 2
                    pSum += pow(temp, 2)
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            if (maxSum > taoSumDiff):
                maxSum = taoSumDiff
                maxThreshold1 = taoThreshold
    return maxThreshold1, maxSum

def calculateTmin_ruc_QR_L2(rucFrame):
    global minThreshold
    minSum = sys.float_info.max
    min_candidate = min(rucFrame)
    for taoThreshold in numpy.arange(min_candidate, 0.00, 0.0025):
        costSum = 0
        pSum = 0
        costCount = 0
        penaltyCount = 0
        for row in rucFrame:
            if (row < 0):
                # print(row)
                if (row > ( taoThreshold)):
                    temp = abs(taoThreshold - row) / 2
                    costSum += pow(temp, 2)
                    costCount = costCount + 1
                else:
                    temp = abs(taoThreshold - row) * 2
                    pSum += pow(temp, 2)
                    penaltyCount = penaltyCount + 1
        if (costSum != 0 and pSum != 0):
            taoSumDiff = abs(costSum - pSum)
            # taoSumDiff = pow(abs(costSum - pSum),2)
            if (minSum > taoSumDiff):
                # print("Original cost: ", costSum, " penalty: ", pSum," taothreshold: ",taoThreshold*(-1))
                minSum = taoSumDiff
                minThreshold = taoThreshold
    return minThreshold,minSum


def get_neg_residual_SA(merged_array,lower_limit,epsilon):
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] >= lower_limit):
            costSum += abs(lower_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            pSum += abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    print("Length of RUC ",len(non_zero_ruc_array_copied))
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - epsilon
    tmin, minSum = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
    return non_zero_ruc_array_copied,tmin

def get_pos_residual_SA(merged_array,upper_limit,epsilon):
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] < upper_limit):
            costSum += abs(upper_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            costFunction[l] = abs(upper_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + epsilon
    tmax, maxSum = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
    return non_zero_ruc_array_copied,tmax

def get_loss_for_contraint_romax_min_QR_CLN(rucFrame, keys, lower_limit,romax,epsilon):
    sorted_frame = dict()
    rucFrame_array = []
    ruc_count = 0
    for key in keys:
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] >= lower_limit):
            # temp = abs(lower_limit - merged_array[l])/2
            # costSum += pow(temp, 2)
            costSum += abs(lower_limit - merged_array[l]) / 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) /2
            cost_count = cost_count+ 1
        else:
            # temp = abs(lower_limit - merged_array[l])*2
            # pSum += pow(temp, 2)
            pSum += abs(lower_limit - merged_array[l]) * 2
            # costFunction[l] = abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    print("Length of RUC ",len(non_zero_ruc_array_copied))
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - epsilon
        ruc_count = ruc_count + 1
        if(ruc_count > romax):
            break
    tmin, minSum = calculateTmin_ruc_QR(non_zero_ruc_array_copied)
    print("RUC Count: ", ruc_count)
    return non_zero_ruc_array_copied,tmin

def get_loss_for_contraint_romax_max_QR_CLN(rucFrame, keys,upper_limit,romax,epsilon):
    difference = dict()
    sorted_frame = dict()
    rucFrame_array = []
    ruc_count = 0
    for key in keys:
        difference = dict()
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key], ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] < upper_limit):
            # temp = abs(upper_limit - merged_array[l])/2
            # costSum += pow(temp, 2)
            costSum += abs(upper_limit - merged_array[l]) / 2
            # costFunction[l] = abs(upper_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            # temp = abs(upper_limit - merged_array[l])*2
            # pSum += pow(temp, 2)
            costFunction[l] = abs(upper_limit - merged_array[l]) * 2
            # pSum += abs(upper_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + epsilon
        ruc_count = ruc_count + 1
        if(ruc_count > romax):
            break
    tmax, maxSum = calculateTmax_ruc_QR(non_zero_ruc_array_copied)
    # print("tmax after ROMAX QR: ", tmax)
    return non_zero_ruc_array_copied,tmax


def get_loss_for_contraint_romax_min_QR_CLN_L2(rucFrame, keys, lower_limit,romax,epsilon):
    sorted_frame = dict()
    rucFrame_array = []
    ruc_count = 0
    for key in keys:
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key])
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] < float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] >= lower_limit):
            temp = abs(lower_limit - merged_array[l])/2
            costSum += pow(temp, 2)
            # costFunction[l] = abs(lower_limit - merged_array[l]) /2
            cost_count = cost_count+ 1
        else:
            temp = abs(lower_limit - merged_array[l])*2
            pSum += pow(temp, 2)
            # costFunction[l] = abs(lower_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
        # costFunction[l] =  abs(costSum-pSum)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    print("Length of RUC ",len(non_zero_ruc_array_copied))
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] - epsilon
        ruc_count = ruc_count + 1
        if(ruc_count > romax):
            break
    tmin, minSum = calculateTmin_ruc_QR_L2(non_zero_ruc_array_copied)
    # print("tmin after ROMAX QR: ", tmin)
    return non_zero_ruc_array_copied,tmin

def get_loss_for_contraint_romax_max_QR_CLN_L2(rucFrame, keys,upper_limit,romax,epsilon):
    sorted_frame = dict()
    rucFrame_array = []
    ruc_count = 0
    for key in keys:
        sorted_frame[key] = rucFrame.sort_values(by=["ruc" + key], ascending=False)
        sorted_non_zero_ruc = sorted_frame[key][sorted_frame[key]['ruc' + key] > float(0)]
        non_zero_ruc_array = sorted_non_zero_ruc["ruc" + key].values
        rucFrame_array.append(non_zero_ruc_array)
    merged_array = rucFrame_array[0].tolist()
    for x in rucFrame_array[1]:
        merged_array.append(x)
    costSum = 0
    pSum = 0
    cost_count = 0
    penalty_count = 0
    costFunction =[0 for i in range(len(merged_array))]
    for l in range(len(merged_array)):
        if (merged_array[l] < upper_limit):
            temp = abs(upper_limit - merged_array[l])/2
            costSum += pow(temp, 2)
            # costFunction[l] = abs(upper_limit - merged_array[l]) / 2
            cost_count = cost_count+ 1
        else:
            temp = abs(upper_limit - merged_array[l])*2
            pSum += pow(temp, 2)
            # pSum += abs(upper_limit - merged_array[l]) * 2
            penalty_count = penalty_count + 1
        costFunction[l] =  abs(costSum-pSum)/(cost_count+penalty_count)
    index_of_sorted_list,gradients = calculate_gradients(costFunction,merged_array) #gradient by cost array
    non_zero_ruc_array_copied = merged_array.copy()
    for i in range(len(index_of_sorted_list)):
        non_zero_ruc_array_copied[index_of_sorted_list[i]] = non_zero_ruc_array_copied[index_of_sorted_list[i]] + epsilon
        ruc_count = ruc_count + 1
        if(ruc_count > romax):
            break
    tmax, maxSum = calculateTmax_ruc_QR_L2(non_zero_ruc_array_copied)
    # print("tmax after ROMAX QR: ", tmax)
    return non_zero_ruc_array_copied,tmax
