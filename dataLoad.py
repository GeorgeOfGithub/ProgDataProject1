import pandas as pd
import numpy as np


def dataLoad(dataname):
    # Author: Lucas Buhelt
    data = None
    # reads the data with delimiters set as whitespaces
    try:
        data = pd.read_csv(dataname,delim_whitespace=True)
        data,error_amount = scan(data)
        print("File loaded succesfully with errors in " + str(error_amount) + " lines.")
        print("These have been removed. Returning to main menu...")
    except OSError:
        print("\n404 FILE NOT FOUND! TRY ANOTHER FILENAME\n")
    return data

def scan(data):
    # This function goes through the dataframe and searches for lines with errors
    # Printing the errors and removing the errors are 2 different things
    before = len(data)

    # 3 for-loops for the 3 different columns where errors are printed
    for i in range(len(data)):
        if(data.iloc[i,0]<10.0 or data.iloc[i,0]>60.0):
         print("Error in line "  + str(i) +" :Temperature outside scope")

    for i in range(len(data)):
        if(data.iloc[i,1]<0):
            print("Error in line "  + str(i) +" :Negative growth")

    for i in range(len(data)):
        if(data.iloc[i,2]<1 or data.iloc[i,2]>4):
            print("Error in line "  + str(i) +" :Wrong bacteria type")

    # Using the drop function from pandas, using a new drop function for each condition
    # because we couldnt get it to work in one function with "and"
    data = data.drop(data[data.iloc[:,0] > 60.0].index)
    data = data.drop(data[data.iloc[:,0] < 10.0].index)
    data = data.drop(data[data.iloc[:,1] < 0.0].index)
    data = data.drop(data[data.iloc[:,2] < 1.0].index)
    data = data.drop(data[data.iloc[:,2] > 4.0].index)

    # Returns amount of error lines
    return(data, before - len(data))        
