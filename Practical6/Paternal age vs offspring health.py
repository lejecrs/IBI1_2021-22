#import matplotlib.
import matplotlib.pyplot as plt
#original datas.
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

#print a dictionary acroding to the data
age_risk=dict(zip(paternal_age,chd)) #Revised by using the function zip() so that values can be changed in lists.
print(age_risk)
print(age_risk[30])# Inside "[]" is what can be modified, where a requested paternal age can be changed, "30" is just an example.

#print a scatter plot with the data
plt.scatter(paternal_age,chd,marker="o")

plt.xticks(paternal_age)
plt.yticks(chd)
plt.xlabel('The age of the father')
plt.ylabel('The relative risk for congenital heart disease (CHD) in the offspring')
plt.show()


