TRAINING_DATA = {
    "2014":"../../resource/2014.csv",
    "2015":"../../resource/2015.csv",
}
TESTING_DATA = {
    "2016": "../../resource/2016.csv",
}
KAPPA = [.025,.1,.1875,.3125,.4375,.625,.8125,1.0,1.125,1.25,1.375,1.5,1.7,1.9,2.00]
# KAPPA = [.025,.0625,.1,.125,.1875,.25,.3125,.375,.4375,.50,.5625,.625,.6875,.75,.8125,
#          .875,.9375,1.0,1.0625,1.125,1.1875,1.25,1.3125,1.375,1.4375,1.5]
RO_MAL = .90 #fraction of attacked meters
RO_MAL_ARRAY = [.30,.40,.50,.60]
RO_MAL_ARRAY_N = [.70,.80]
DEL_AVG = 1500 #amount of posoning in the attacked time frame
DEL_AVG_ARRAY = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
DEL_AVG_ARRAY_DED = [50,100,150,200,250,300,350,400]
DEL_AVG_LARGE_ARRAY = [1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500]
DEL_AVG_EXTRA_LARGE = [2600,2700,2800,2900,3000,3100,3200,3300,3400]
START = 1
END = 365
E = 0.12 #avg per unit electricity cost
DAYS_INA_YEAR = 365
ITA = 1
ALPHA = .7#[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
BETA = .8#0.25
LAMBDA = 0.25
BOTTOM = 0.70
TOP = 1.00
THREASHOLD = .5
SMALL_ADDITIVE = 0
LARGE_ADDITIVE = 1
LARGE_DEDUCTIVE = 2
SMALL_DEDUCTIVE = 4
LARGE_CAMOUFLAGE = 3
SMALL_CAMOUFLAGE = 5
ATTACK_YEAR_TEST = 2016
ATTACK_YEAR = 2014
START_DATE = '2014-03-01' #day number 60
END_DATE = '2014-06-30' # day number 181
START_DATE_M = '2014-04-01' #day number 60
END_DATE_M = '2014-06-30' # day number 181
START_DATE_TEST = '2016-04-01' # this will not be used for poisoning attack cases
END_DATE_TEST = '2016-06-30'
SLIDING_FRAME = 7
RESIDUAL_BOTTOM = -1
RESIDUAL_TOP = 1
ROMAX = 50
# After Romax Tao Min LR:  -0.0525 After Romax Tao Max:  0.0475 with epsilon .05
# After Romax Tao Min LR:  -0.06 After Romax Tao Max:  0.0475 with epsilon .08
# tmin after ROMAX QR:  -0.085 #tmax after ROMAX QR:  0.0725 with epsilon .05
# tmin after ROMAX QR:  -0.1 #tmax after ROMAX QR:  0.0825 with epsilon .08
#del 50 and romal 30% deductive attack
# QR-->Tier 2 Detection for Org Threshold: 0 First Detected org: 0 First Detected atta: 0 false_alarm_tier2_org: 19 false_alarm_tier2_att: 11
# LR-->Tier 2 Detection for Org Threshold: 0 First Detected org: 0 First Detected atta: 0 false_alarm_tier2_org: 39 false_alarm_tier2_att: 28

#del 100 and romal 30% deductive attack
#QR-->Tier 2 Detection for Org Threshold: 52 First Detected org: 99 First Detected atta: 100 false_alarm_tier2_org: 19 false_alarm_tier2_att: 12
#LR-->Tier 2 Detection for Org Threshold: 56 First Detected org: 97 First Detected atta: 99 false_alarm_tier2_org: 38 false_alarm_tier2_att: 26
# optimal epsilon value
# 0.04146170788004631(mean) + 0.03840153102525633(std)*2 = 0.11826476993
# 0.04146170788004631(mean) + 0.03840153102525633(std) = 0.0798632389

#Geometric mean
 # gmean = 0.021374503333936225  mad = 0.033139772397974276
 # median = 0.0272641306322526
