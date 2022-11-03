import numpy as np
import statistics
import displayMenu

def dataStatistics(data,statistic):
    statistic = statistic.upper()
#dataStatistics function calculates one of several possible statistics, which
#are single numbers describing an aspect of the data
#
# Usage: result = dataStatistics(data,statistic)
#
# Inputs: data(N*3 matrix with columns Temperature, Growth rate and Bacteria)
#         statistic(string specifying the statistic that should be calculated)
# Output: result(scalar containing the calculated statistic)
#
# Author: Marios Constantinou, s212684@dtu.dk, 2022
    Temp=data.iloc[:,0]
    GrowthRate=data.iloc[:,1]
    GrowthRate1 = GrowthRate
    GrowthRate2 = GrowthRate
    print(GrowthRate)
    Bacteria=data.iloc[:,2]
    if statistic == "MEAN TEMPERATURE":
        result=statistics.mean(Temp)
    elif statistic == "MEAN GROWTH RATE":
        result=statistics.mean(GrowthRate)
    elif statistic == "STD TEMPERATURE":
        result=statistics.stdev(Temp)
    elif statistic == "STD GROWTH RATE":
        result=statistics.stdev(GrowthRate)
    elif statistic == "ROWS":
        result=len(Temp)
    elif statistic == "MEAN COLD GROWTH RATE":
        GrowthRate1[Temp>=20]=0
        GrowthRate1=[i for i in GrowthRate1 if i != 0]
        result=statistics.mean(GrowthRate1)
    elif statistic == "MEAN HOT GROWTH RATE":
        GrowthRate2[Temp<=50]=0
        GrowthRate2=[i for i in GrowthRate2 if i != 0]
        result=statistics.mean(GrowthRate2)
    return result
