import os
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
#Practical 7 4.
os.chdir ("c:/Users/ljc/Desktop/source/code/03Python works/Practical7")                  
covid_data = pd.read_csv("full_data.csv")   
print(covid_data.iloc[10:21,[0,2]]) #showing first and thrid column from row 10~20 (inclusive)


#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
my_columns = [False, False, False, False, True, False]
print(covid_data.iloc[0:82,my_columns])
print(covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"]) 
#Line 12 and line 13 actually generated the same thing, but is a different way of using Boolean.

china_new_data= covid_data.loc[covid_data['location'] == 'China',["date","new_cases","new_deaths"]]
china_new_cases=covid_data.loc[covid_data['location'] == 'China',"new_cases"]
china_new_deaths=covid_data.loc[covid_data['location'] == 'China',"new_deaths"]
mean_c=np.mean(china_new_data["new_cases"])
mean_d=np.mean(china_new_data["new_deaths"])
print(f'This is seperately the mean number of new cases and new deaths in China {mean_c}, {mean_d}')
#This is seperately the mean number of new cases and new deaths in China.

plt.boxplot(china_new_cases)
plt.xlabel('new_cases')
plt.ylabel('numbers')
plt.title('The boxplot of new cases')
plt.show()
plt.boxplot(china_new_deaths)
plt.xlabel('new_deaths')
plt.ylabel('numbers')
plt.title('The boxplot of new deaths')
plt.show()
# The boxplot of new cases in China and new deaths in China has been printed.

china_dates=covid_data.loc[covid_data['location'] == 'China',"date"]
y1=china_new_cases
y2=china_new_deaths

plt.plot(china_dates,y1,"b+",china_dates,y2,"r+")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.xlabel('dates')
plt.ylabel('The numbers of new cases and deaths')
plt.legend(['new cases','new deaths'])
plt.title('The plot of new cases and new deaths with regard to time')
plt.show()
#The plot of new cases and new deaths with regard to time has been printed.


#Answering additional question.
#How have new cases and total cases developed over time in Spain?
n1=spain_new_cases=covid_data.loc[covid_data["location"]=="Spain","new_cases"]
n2=spain_total_cases=covid_data.loc[covid_data["location"]=="Spain","total_cases"]
x=spain_dates=covid_data.loc[covid_data["location"]=="Spain","date"]
plt.plot(x,n1,"b",x,n2,"g")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.xlabel('dates')
plt.ylabel('number of cases')
plt.title('New cases and total cases developed over time in Spain')
plt.legend(['new cases','new deaths'])
plt.show()

