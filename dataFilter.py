import pandas as pd
import numpy as np

import displayMenu

def dataFilter(data):
    return menu(data)


def menu(data):
    menuItems = np.array(["Filter for bacteria types", "Filter for growth rate","Remove filters", "Quit"])
    new_data = None
    while True:
        # Display menu options and ask user to choose a menu item
        print("Filtering")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Enter name
        if choice == 1:
        # Ask user to input name and save it in variable
            print("Types:\n1: Salmonella enterica\n2: Bacillus cereus\n3: Listeria\n4: Brochothrix thermosphacta")
            filtertype = input("Please enter type of bacteria: ")
            new_data = None
            new_data = data[data.iloc[:,2]==int(filtertype)]
            return new_data
        elif choice == 2:
            min = input("Minimum growth rate: ")
            max = input("Maximum growth rate: ")
            new_data = data[(data.iloc[:,1]> float(min)) & data.iloc[:,1]< float(max)]
            #new_data = data[data.iloc[:,1]< float(min) or (data.iloc[:,1]> float(max))]
            #new_data = data[data.iloc[:,1]<float(max)]
            return new_data
        # ------------------------------------------------------------------
        # 2. Display greeting
        elif choice == 3:
            break
        elif choice == 4:
            break