import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd 
import math




def dataPlot(data): 
    
 #name of each column of our  dataset
 data.columns = ["Temperature", "GrowthRate", "Bacteria"]
 
 #Now we will count how many of each kind of bacteria exist in this dataset 
 frequency=data["Bacteria"].value_counts()
 
 #In the entire dataset we count the frequency of the bacteria type. And put the frequencies in the dataset. 
 data['Frequency'] = data.groupby('Bacteria')['Bacteria'].transform('count')
 
 
 #we will keep the last two columns from this dataset to make our first plot
 OurData=data[['Bacteria','Frequency']]
   
 OurData = OurData.drop_duplicates(subset=['Bacteria'])
 
 #change the style of the letters for the graphs
 csfont = {'fontname':'Comic Sans MS'}
 hfont = {'fontname':'Helvetica'}
 
 #names of different types of bacteria in the x axis
 x=["Salmonella","Bacillus cereus","Listeria", "Brochothrix\nthermosphacta"]
 #length of x axis
 index = np.arange(len(x))
 #y axis
 y=frequency
 
 plt.bar(index, frequency, color=['steelblue','purple','maroon','burlywood'])
 plt.title("Number of Bacteria",fontsize=16, weight='bold',**csfont) # Set the title of the graph
 plt.xlabel("Types of Bacteria",labelpad=30, **hfont) # Set the x-axis label
 plt.ylabel("Number of each type of Bacteria", labelpad=20, **hfont) # Set the y-axis label
 new_list=(np.arange(0, max(frequency)+1, 4.0))
 
 
 plt.xticks(index,x,rotation=45, fontsize=10)
 plt.yticks(new_list)
 plt.grid(color='gray', linestyle='-', linewidth=0.5)

 plt.show()

#.......................................................................................................

 ourData2=data[['Temperature','GrowthRate','Bacteria']]
 
 #We sort our values in column Temperature, beggining from the lowest to the highest temperature
 ourData2 = ourData2.sort_values('Temperature')
 
 #Filter data by using the name of each type of bacteria
 typeOne=ourData2[ourData2["Bacteria"] == 1]
 typeTwo=ourData2[ourData2["Bacteria"] == 2]
 typeThree=ourData2[ourData2["Bacteria"] == 3]
 typeFour=ourData2[ourData2["Bacteria"] == 4]
 

 #for every type of bacteria we save in a list the temperatures
 temperatureTypeOne=typeOne['Temperature'].tolist()
 temperatureTypeTwo=typeTwo['Temperature'].tolist()
 temperatureTypeThree=typeThree['Temperature'].tolist()
 temperatureTypeFour=typeFour['Temperature'].tolist()

 #we will do the same for growth rates
 growthRateTypeOne=typeOne['GrowthRate'].tolist()
 growthRateTypeTwo=typeTwo['GrowthRate'].tolist()
 growthRateTypeThree=typeThree['GrowthRate'].tolist()
 growthRateTypeFour=typeFour['GrowthRate'].tolist()

 #plot individual lines with custom colors and labels
 plt.plot(temperatureTypeOne,growthRateTypeOne,label="Salmonela",color='steelblue')
 plt.plot(temperatureTypeTwo,growthRateTypeTwo,label="Bacillus cereus",color='purple')
 plt.plot(temperatureTypeThree,growthRateTypeThree,label="Listeria",color='maroon')
 plt.plot(temperatureTypeFour,growthRateTypeFour,label="Brochothrix\nthermosphacta",color='burlywood')

 #add legend
 plt.legend(title='Types of bacteria',loc=0,prop={'size': 6})

 #add axes labels and a title
 plt.ylabel('Growth Rate', fontsize=10,labelpad=20, **hfont)
 plt.xlabel('Temperature', fontsize=10,labelpad=30, **hfont)
 plt.title('Growth rate by temperature', fontsize=14, weight='bold',**csfont)
 

 plt.grid()
 #display plot
 plt.show()







#path = "/Users/neokl/Desktop/projects_sample.txt"

#Add sep=" " in your code, leaving a blank space between the quotes. So pandas can detect spaces between values and sort in columns. Data columns is for naming your columns.
#We load the data
#data = pd.read_csv(path, sep=" ", header=None)

#with open(path, 'r') as fp:
#    filepaths = fp.readlines()

#dataPlot(data)













