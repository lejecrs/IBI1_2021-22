
import matplotlib.pyplot as plt
import re
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np

tree=xml.dom.minidom.parse("go_obo.xml")
element=tree.documentElement
terms= element.getElementsByTagName('term')
print(f"The total number of terms is {terms.length}.") #The total number of the terms.


list0=[]
d={}
for term in terms:
    id_=term.getElementsByTagName('id')[0]
    is_a=term.getElementsByTagName('is_a')
    C_GO=id_.firstChild.data
    P_GO=[]
    defstr=term.getElementsByTagName('defstr')[0]
    if C_GO not in d:
        d[C_GO]=[]
    if re.search('translation',defstr.firstChild.data):
        list0.append(C_GO)
    for i in range(is_a.length):
        P_GO.append(is_a[i].firstChild.data)
        if P_GO[i] not in d:
            d[P_GO[i]]=[]
       
        d[P_GO[i]].append(C_GO)
        d[P_GO[i]].append(d[C_GO]) #Originally, the data structure is really complex and hard for me to organise. With the help of my classmates, 
        #I got the way of extracting the all parent datas using the structure "list in lists".

#Defining a function that can unfold the structure "list in list", which was done after disscusion with my classmates.
def unfold(lists):
    for element in lists:
        if type(element)==str:
            list1.append(element)
        else:
            unfold(element) # Input a list and it will check whether the element in list is a string type. If not, it will continue doing that by getting every element
            # and append it to a new list.

for key, value in d.items():
    list1=[]
    unfold(value)
    d[key]=list(set(list1))

childnodes=list(d.values())
number_C=[len(element) for element in childnodes]
number_T=[len(d[element]) for element in list0]
plt.boxplot(number_C)
plt.ylabel('Number of Child GOs')
plt.title('The boxplot distribution of Childnotes')
plt.show()
plt.boxplot(number_T)
plt.ylabel('Number of Childnodes associated with translation')
plt.title('The boxplot distribution of Childnodes associated with translation')
plt.show()
#Sepeartedly showed the box plot of Number of overall GO and those associated with translation.

mean_num_T=np.mean(number_T)
mean_num_C=np.mean(number_C)

print(mean_num_C,mean_num_T)
if mean_num_C>= mean_num_T:
    print('On average, ‘translation’ term contain a smaller number of  child nodes than overall GO')
else:
    print('On average, ‘translation’ term contain a larger number of  child nodes than overall GO') #From the output, we can see that translation term contain a larger number of child nodes than overall GO.

    



 
    
