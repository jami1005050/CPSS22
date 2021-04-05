from functools import reduce
from linear.functions_LR import *
from utility.common import *
from utility.constant import *
import os as o
import matplotlib.pyplot as plt
class ExistingDefense_LG:
    def __init__(self):
        self.historical_safe_margin = None
        self.tMax_ruc = None
        self.tmin_ruc = None
        self.number_of_compromised_meter = 0
        self.system_detected_unsafe = [] #track the days where false alarm happened

    def training(self, TRAINING_DATA,threshold):
        file_data = {}
        file_data_filtered = {}
        for key in TRAINING_DATA.keys():  # for each file in the dictionary
            file_relative_path = TRAINING_DATA.get(key)  # get the file path by year as key
            file_path = o.path.abspath(file_relative_path)  # relative path of the data file
            file_data[key] = read_data(file_path, key)  # call the reader function of datareader object
            file_data_filtered[key] = file_data[key][file_data[key]['use'] <= 6000]
        file_data_transformed = box_cox_transformation(file_data_filtered)
        hm_am_ratio_frame = calculateAMAndHM(file_data_transformed)
        df_merged = reduce(lambda left, right: pd.merge(left, right,on=['day']), hm_am_ratio_frame)
        df_merged['mean_ratio'] = df_merged[['ratio2014', 'ratio2015']].mean(axis=1) #take mean of two ratio per day
        mean_absolute_deviation = df_merged['mean_ratio'].std()
        safe_margin = calculate_safe_margin(df_merged,mean_absolute_deviation,threshold)
        self.historical_safe_margin = safe_margin[['day','margin_low','margin_high']].copy()
        nabla_frame_no_attack = calculate_nabla(df_merged,TRAINING_DATA.keys())
        residual_frame_no_attack = calculate_ruc(nabla_frame_no_attack, TRAINING_DATA.keys())
        self.tmax_ruc = calculateTmax_LG(residual_frame_no_attack, TRAINING_DATA.keys())# non attacked standard limit max margin
        self.tmin_ruc = calculateTmin_LG(residual_frame_no_attack, TRAINING_DATA.keys()) # non attacked standard limit min margin
        print(self.tmin_ruc, self.tmax_ruc)
        plt.show()

def main():
    main = ExistingDefense_LG()
    main.training(TRAINING_DATA, 2.00)
main()
