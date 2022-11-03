import numpy as np
import pandas as pd
import displayMenu
import dataStatistics as dS
import dataLoad as dL
import dataPlot as dP
import dataFilter as dF
pd.options.mode.chained_assignment = None

def menu():
    menuItems = np.array(["Load data from file", "Filter data","Display Statistics", "Plot data", "Quit", "Display"])
    filename = ""
    data = None
    while True:
        # Display menu options and ask user to choose a menu item
        print("MENU")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Enter name
        if choice == 1:
        # Ask user to input name and save it in variable
            filename = input("Please enter name of file: ")
            data = dL.dataLoad(filename)
        # ------------------------------------------------------------------
        # 2. Display greeting
        elif choice == 2:
        # Is name empty?
            if data is None:
        # Display error message
                print("\nError: No file selected!\n")
            else:
        # Display greeting
                data = dF.dataFilter(data)
        elif choice == 3:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                statistics = input("Please enter the type of statistic wanted: ")
                stat = dS.dataStatistics(data,statistics)
                print(stat)
                ## load the file again here

        elif choice == 4:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                dP.dataPlot(data)   
        # ------------------------------------------------------------------
        # 3. Quit
        elif choice == 5:
        # End
            break
        elif choice == 6:
        # Is name empty?
            if data is None:
        # Display error message
                print("\nError: No file selected!\n")
            else:
        # Display greeting
                print(data.to_string(index=False))
        

menu()