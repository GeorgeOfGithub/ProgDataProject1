import numpy as np
import pandas as pd
import displayMenu
import dataStatistics as dS
import dataLoad as dL
import dataPlot as dP
import dataFilter as dF
pd.options.mode.chained_assignment = None

def menu():
    menuItems = np.array(["Load data from file", "Filter data","Display Statistics", "Plot data","Display data as table", "Quit"])
    filename = ""
    data = None
    while True:
        # Display menu options and ask user to choose a menu item
        print("MENU")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Load data from file
        if choice == 1:
            filename = input("Please enter name of file: ")
            Original_data = dL.dataLoad(filename)
            data = dL.dataLoad(filename)
        # ------------------------------------------------------------------
        # 2. Filter data
        elif choice == 2:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                data = dF.dataFilter(data,Original_data)
        # ------------------------------------------------------------------
        # 3. Display Statistics        
        elif choice == 3:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                statistics = input("Please enter the type of statistic wanted: ")
                stat = dS.dataStatistics(data,statistics)
                print(stat)
        # ------------------------------------------------------------------
        # 4. Plot data
        elif choice == 4:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                dP.dataPlot(Original_data)   
        # ------------------------------------------------------------------
        # 5. Display current file after filters   
        elif choice == 5:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                print(data.to_string(index=False))
        # ------------------------------------------------------------------
        # 6. Quit
        elif choice == 6:
        # End
            break        

menu()