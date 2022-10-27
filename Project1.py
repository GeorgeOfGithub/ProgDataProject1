import numpy as np
import pandas as pd
import inputNumber
import displayMenu

## testing


def load_data(dataname):
    global data
    global data2

    try:
        data = pd.read_csv(dataname,delim_whitespace=True)
        print("File loaded succesfully!")
    except OSError as e:
        print("\n404 FILE NOT FOUND! TRY ANOTHER FILENAME\n")



def menu():
    menuItems = np.array(["Enter txt file", "Display First line", "Quit"])
    name = ""

    while True:
        # Display menu options and ask user to choose a menu item
        print("MENU")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Enter name
        if choice == 1:
        # Ask user to input name and save it in variable
            name = input("Please enter name of file: ")
            load_data(name)
        # ------------------------------------------------------------------
        # 2. Display greeting
        elif choice == 2:
        # Is name empty?
            if data is None:
        # Display error message
                print("Error: empty file")
            else:
        # Display greeting
                print(data)
        # ------------------------------------------------------------------
        # 3. Quit
        elif choice == 3:
        # End
            break

menu()