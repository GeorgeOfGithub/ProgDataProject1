# Author: Lucas Buhelt

import pandas as pd
import numpy as np
import displayMenu

def dataFilter(data,Original_data):
    menuItems = np.array(["Filter for bacteria types", "Filter for growth rate","Remove filters", "Back"])

    while True:
        # Display menu options and ask user to choose a menu item
        print("Filtering")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Filter by bacteria type
        if choice == 1:
            print("Types:\n1: Salmonella enterica\n2: Bacillus cereus\n3: Listeria\n4: Brochothrix thermosphacta")
            filtertype = input("Please enter type of bacteria as number: ")
            new_data = None
            new_data = data[data.iloc[:,2]==int(filtertype)]
            return new_data
        # ------------------------------------------------------------------
        # 2. Min and max growth rates          
        elif choice == 2:
            min = input("Minimum growth rate: ")
            max = input("Maximum growth rate: ")
            new_data = data[(data.iloc[:,1]>float(min)) & (data.iloc[:,1]< float(max))]

            return new_data
        # ------------------------------------------------------------------
        # 3. Reset Filters by using original data
        elif choice == 3:
            return Original_data
        # ------------------------------------------------------------------
        # 4. Go Back      
        elif choice == 4:
            break