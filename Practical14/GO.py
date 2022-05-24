from optparse import Values
import matplotlib.pyplot as plt
import re
from xml.dom.minidom import parse
import xml.dom.minidom

tree=xml.dom.minidom.parse("go_obo.xml")
element=tree.documentElement
terms= element.getElementsByTagName('term')
print(f"The total number of terms is {terms.length}.")

list1=[]
d={}
for term in terms:
    id_=term.getElementsByTagName('id')[0]
    is_a=term.getElementsByTagName('is_a')
    C_GO=id_.firstChild.data
    P_GO=[]
    if C_GO not in d:
        d[C_GO]=[]
    for i in range(is_a.length):
        P_GO.append(is_a[i].firstChild.data)
        if P_GO[i] not in d:
            d[P_GO[i]]=[]
       
        d[P_GO[i]].append(C_GO)
        d[P_GO[i]].append(d[C_GO]) #Originally, the data structure is really complex and hard for me to organise. With the help of my classmates, 
        #I got the way of extracting the all parent datas using the structure list in lists.

def unfold(lists):
    for element in lists:
        if type(element)==str:
            list1.append(element)
        else:
            unfold(element)

for key, value in d.items():
    list1=[]
    unfold(value)
    d[key]=list(set(list1))

childnodes=list(d.values())
number_C=[len(element) for element in childnodes]
plt.boxplot(number_C)
plt.ylabel('Number of Child GOs')
plt.title('The boxplot distribution of Childnotes')
plt.show()

# Sorry for not completing the whole practical, some of the function is  out of my current range.

    



 
    
