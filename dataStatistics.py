import numpy as np
import statistics
import displayMenu

def dataStatistics(data,statistic):
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
    Bacteria=data.iloc[:,2]
    if statistic == "Mean Temperature":
        result=statistics.mean(Temp)
    elif statistic == "Mean Growth rate":
        result=statistics.mean(GrowthRate)
    elif statistic == "Std Temperature":
        result=statistics.stdev(Temp)
    elif statistic == "Std Growth rate":
        result=statistics.stdev(GrowthRate)
    elif statistic == "Rows":
        result=len(Temp)
    elif statistic == "Mean Cold Growth rate":
        GrowthRate[Temp>=20]=0
        GrowthRate=[i for i in GrowthRate if i != 0]
        result=statistics.mean(GrowthRate)
    elif statistic == "Mean Hot Growth rate":
        GrowthRate[Temp<=50]=0
        GrowthRate1=[i for i in GrowthRate if i != 0]
        result=statistics.mean(GrowthRate1)
    return result
