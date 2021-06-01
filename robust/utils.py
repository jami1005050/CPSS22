import numpy as np
from math import sqrt

def calculate_t_max_cauchy(ruc_frame, keys, tau_range, w1, w2, b=0.006):
    tau_list = list()
    cost_list = list()
    s_less_list = list()
    s_high_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 1
        cost_less = 1
        cost_high = 1
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        cost *= 1 + (((x * w2) / b) ** 2)
                        # cost_less *= 1 + ((x * w1) / b) ** 2
                    else:
                        cost *= 1 + (((x * w1) / b) ** 2)
                        # cost_high *= 1 + ((x * w2) / b) ** 2

        # s_high_list.append(cost_high)
        # s_less_list.append(cost_less)
        cost_list.append(b * b * np.log(cost))
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_min_cauchy(ruc_frame, keys, tau_range, w1, w2, b=0.006):
    tau_list = list()
    cost_list = list()
    s_less_list = list()
    s_high_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 1
        cost_less = 1
        cost_high = 1
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) < 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        cost *= 1 + (((x * w1) / b) ** 2)
                    #  cost_less *= 1 + ((x * w1) / b) ** 2
                    else:
                        cost *= 1 + (((x * w2) / b) ** 2)
                    #   cost_high *= 1 + ((x * w1) / b) ** 2

        # s_high_list.append(cost_high)
        # s_less_list.append(cost_less)
        cost_list.append(b * b * np.log(cost))
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_max_l2(ruc_frame, keys, tau_range, w1, w2, b=1):
    tau_list = list()
    cost_list = list()
    penalty_list = list()
    loss_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        penalty = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        cost += x * w1
                    else:
                        penalty += x * w2

        penalty_list.append(penalty)
        cost_list.append(cost)
        loss_list.append((cost - penalty) ** 2)
        tau_list.append(tau)

    return tau_list[np.argmin(loss_list)], loss_list, tau_list

def calculate_t_min_l2(ruc_frame, keys, tau_range, w1, w2, b=1):
    tau_list = list()
    cost_list = list()
    penalty_list = list()
    loss_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        penalty = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) < 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        cost += x * w1
                    else:
                        penalty += x * w2

        penalty_list.append(penalty)
        cost_list.append(cost)
        loss_list.append((cost - penalty) ** 2)
        tau_list.append(tau)

    return tau_list[np.argmin(loss_list)], loss_list, tau_list

def calculate_t_max_huber(ruc_frame, keys, tau_range, w1, w2, b=0.2):
    tau_list = list()
    cost_list = list()
    s_less_list = list()
    s_high_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        # cost_less = 0
        # cost_high = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        if (abs(x) * w2) <= b:
                            cost += .5 * ((abs(x) * w2) ** 2)
                        else:
                            cost += b * (abs(x) * w2) - .5 * (b ** 2)
                    #  cost_less += abs(x) * w1
                    else:
                        if (abs(x) * w1) <= b:
                            cost += .5 * ((abs(x) * w1) ** 2)
                        else:
                            cost += b * (abs(x) * w1) - (.5 * (b ** 2))
                    # cost_high += abs(x) * w2

        # s_high_list.append(cost_high)
        # s_less_list.append(cost_less)

        cost_list.append(cost)
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_min_huber(ruc_frame, keys, tau_range, w1, w2, b=0.2):
    tau_list = list()
    cost_list = list()
    s_less_list = list()
    s_high_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        # cost_less = 0
        # cost_high = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) < 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        if (abs(x) * w1) <= b:
                            cost += .5 * ((abs(x) * w1) ** 2)
                        else:
                            cost += b * (abs(x) * w1) - (.5 * (b ** 2))
                    # cost_less += abs(x) * w1
                    else:
                        if (abs(x) * w2) <= b:
                            cost += .5 * ((abs(x) * w2) ** 2)
                        else:
                            cost += b * (abs(x) * w2) - (.5 * (b ** 2))

                    # cost_high += abs(x) * w2

        # s_high_list.append(cost_high)
        # s_less_list.append(cost_less)
        cost_list.append(cost)
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_max_pseudo_huber(ruc_frame, keys, tau_range, w1, w2, b=1):
    tau_list = list()
    cost_list = list()
    s_less_list = list()
    s_high_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        cost_less = 0
        cost_high = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    if x >= 0:
                        cost += abs(x) * w1
                        cost_less += abs(x) * w1
                    else:
                        cost += abs(x) * w2
                        cost_high += abs(x) * w2

        s_high_list.append(cost_high)
        s_less_list.append(cost_less)
        cost_list.append(b * b * (sqrt(1 + (cost / b) ** 2) - 1))
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_max_cauchy_non_Q(ruc_frame, keys, tau_range, b=0.006):
    tau_list = list()
    cost_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 1
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    cost *= 1 + ((x / b) ** 2)
        cost_list.append(b * b * np.log(cost))
        tau_list.append(tau)
    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_min_cauchy_non_Q(ruc_frame, keys, tau_range, b=0.006):
    tau_list = list()
    cost_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 1
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) < 0:
                    x = getattr(row, "ruc" + key) - tau
                    cost *= 1 + ((x / b) ** 2)
        cost_list.append(b * b * np.log(cost))
        tau_list.append(tau)
    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_max_huber_non_Q(ruc_frame, keys, tau_range, b=0.1):
    tau_list = list()
    cost_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) > 0:
                    x = getattr(row, "ruc" + key) - tau
                    if (abs(x)) <= b:
                        cost += .5 * (abs(x) ** 2)
                    else:
                        cost += b * abs(x) - (.5 * (b ** 2))
        cost_list.append(cost)
        tau_list.append(tau)

    return tau_list[np.argmin(cost_list)], cost_list, tau_list

def calculate_t_min_huber_non_Q(ruc_frame, keys, tau_range, b=0.1):
    tau_list = list()
    cost_list = list()
    for tau in np.arange(tau_range[0], tau_range[1], tau_range[2]):
        cost = 0
        for row in ruc_frame.itertuples():
            for key in keys:
                if getattr(row, "ruc" + key) < 0:
                    x = getattr(row, "ruc" + key) - tau
                    if abs(x) <= b:
                        cost += .5 * (abs(x)) ** 2
                    else:
                        cost += b * abs(x) - (.5 * (b ** 2))
        cost_list.append(cost)
        tau_list.append(tau)
    return tau_list[np.argmin(cost_list)], cost_list, tau_list
