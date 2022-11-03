import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd 
import math




def dataPlot(data): 
    

 data.columns = ["Temperature", "GrowthRate", "Bacteria"]
 #print(data.columns)
 #print(data)


 #Now we will count how many of each kind of bacteria exist in this dataset 
 frequency=data["Bacteria"].value_counts()

 #BacteriaNames = data.rename({"1": "Salmonella", "2": "Bacillus cereus", "3": "Listeria", "4":"Brochothrix thermosphacta"})
 data['Frequency'] = data.groupby('Bacteria')['Bacteria'].transform('count')
 #print(data['Frequency'])
 #print(data)

 #we will keep the last two columns from this dataset to make our first plot
 OurData=data[['Bacteria','Frequency']]  
 OurData = OurData.drop_duplicates(subset=['Bacteria'])
 #print(OurData)
 x=["Salmonella","Bacillus cereus","Listeria", "Brochothrix thermosphacta"]
 index = np.arange(len(x))
 y=frequency
 plt.bar(index, frequency, color='green')
 plt.title("Number of Bacteria") # Set the title of the graph
 plt.xlabel("Types of Bacteria",labelpad=30) # Set the x-axis label
 plt.ylabel("Number of each type of Bacteria") # Set the y-axis label
 plt.xticks(index,x,rotation=45, fontsize=10)
 new_list = range(math.floor(min(y)), math.ceil(max(y))+1)
 plt.yticks(new_list)

 plt.show()

#.......................................................................................................

 ourData2=data[['Temperature','GrowthRate','Bacteria']]
 #print(OurData2)
 #We sort our values in column Temperature, beggining from the lowest to the highest temperature
 ourData2 = ourData2.sort_values('Temperature')
 #print(ourData2)
 #Filter data by using the name of each type of bacteria
 typeOne=ourData2[ourData2["Bacteria"] == 1]
 typeTwo=ourData2[ourData2["Bacteria"] == 2]
 typeThree=ourData2[ourData2["Bacteria"] == 3]
 typeFour=ourData2[ourData2["Bacteria"] == 4]
 #print(typeOne)

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
 plt.plot(temperatureTypeFour,growthRateTypeFour,label="Brochothrix thermosphacta",color='burlywood')

 #add legend
 plt.legend(title='Types of bacteria',loc=2,prop={'size': 6})

 #add axes labels and a title
 plt.ylabel('Growth Rate', fontsize=10,labelpad=20)
 plt.xlabel('Temperature', fontsize=10,labelpad=20)
 plt.title('Growth rate by temperature', fontsize=16)
 plt.xlim([10, 60])
 plt.ylim(ymin=0)


 #display plot
 plt.show()







#path = "/Users/neokl/Desktop/projects_sample.txt"

#Add sep=" " in your code, leaving a blank space between the quotes. So pandas can detect spaces between values and sort in columns. Data columns is for naming your columns.
#We load the data
#data = pd.read_csv(path, sep=" ", header=None)

#with open(path, 'r') as fp:
#    filepaths = fp.readlines()

#dataPlot(data)













