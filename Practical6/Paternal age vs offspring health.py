#import matplotlib.
import matplotlib.pyplot as plt
#original datas.
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

#print a dictionary acroding to the data
age_risk={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
print(age_risk)
print(age_risk['30'])# Inside "[]" is what can be modified, where a requested paternal age can be changed, "30" is just an example.

#print a scatter plot with the data
plt.scatter(paternal_age,chd,marker="o")
plt.show()


