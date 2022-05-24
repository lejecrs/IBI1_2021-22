#import matplotlib.
import matplotlib.pyplot as plt
#original data.
marks=[45,36,86,57,53,92,65,45]
#use .sort method to sort the list of marks
marks.sort()
print(marks)
#draw the boxplot using matplotlib.
plt.boxplot(x=marks)
plt.title('The boxplot of marks of Rob')
plt.xlabel('Rob')
plt.ylabel('Marks') # Revised by adding titles and marks.
plt.show()
#calculate the average mark of Rob.
a=sum(marks)/8 
print(a)
#from this result, we can know that Rob has failed this ICA.
