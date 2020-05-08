import os
import matplotlib.pyplot as plt
import pandas as pd

crops_data = pd.read_csv("CropsDataFile.csv")
state = crops_data["State_Name"].values.tolist()
district = crops_data["District_Name"].values.tolist()
crop_year = crops_data["Crop_Year"].values.tolist()
season = crops_data["Season"].values.tolist()
crop = crops_data["Crop"].values.tolist()
area = crops_data["Area"].values.tolist()
production = crops_data["Production"].values.tolist()
os.chdir("C:\\Users\\Rohit Sagar Shinde\\Desktop")

# It stores all data on your desktop :
A = open("Year Wise Data.txt",'w')
B = open("Crop wise Data.txt",'w')

# Main Program :
print("Enter 1 for retriving_data_year_wise , 2 for cropwise_graph , 3 for retriving_data_crop_wise , 4 for exit")
while(1):
    c = int(input("Enter the comand line : "))
    if(c==1):
        n=int(input("Enter the year for which you want to see all details : "))
        for i in range(0,len(crop_year)):
            if(crop_year[i]==n):
                A.write("\n State:"+str(state[i])+ "\n District:"+ str(district[i])+"\n Season:" +str(season[i])+"\n Crop:"+str(crop[i])+"\n Area :"+str(area[i])+ "\n Production : "+str(production[i])+"\n")
    elif(c==2):
        C=str(input("Enter the crop name for which you want to see year vs crop productivity graph : "))
        Year=[]
        Production=[]
        for i in range(0,len(crop_year)):
            if(crop[i]==C):
                Year.append(crop_year[i])
                Production.append(production[i])
        plt.bar(Year,Production) 
        plt.xlabel("Year") 
        plt.ylabel("Production") 
        plt.title(f"Year vs Crop Productivity graph of {C}",color = "Red" )
        plt.show()     
    elif(c==3):
        D=str(input("Enter the crop name for which you want to see all details : "))
        for i in range(len(crop_year)):
            if(crop[i]==D):
                B.write("\n State:"+str(state[i])+ "\n District:"+ str(district[i]) + " \n Crop Year: " +str(crop_year[i])+"\n Season:" +str(season[i])+"\n Area :"+str(area[i])+ "\n Production : "+str(production[i])+"\n")
    else:
        break            
     