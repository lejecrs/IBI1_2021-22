
import re
with open(input('Please input the file name:'),"r") as f1,open('count_fragments.fa','w') as newfile:

  f1=f1.read()
  f1=f1.replace('\n','')
  f2=re.split('>',f1)#The 3 lines above is trying to make the file without line feed and split it into a list according to different genes.
  del f2[0]#Deleting the first element in the list because it is a blank.
  gene1=[]#Creating a new list to store the gene with 'GAATTC' in it.
  for gene in f2:
    if  "GAATTC" in gene:
      gene1.append(gene)
  f3=''.join(gene1)#These 4 lines judge if the 'GAATTC' is within the gene sequence, if yes, put it in a new list.
  
  names=re.findall(r'gene:([^ ]*)',f3)#Using regular expression to find and store the names of genes.
                                                                                                                                                                                 
  seqs=re.findall(r'[ATCG]{7}[ATCG]+',f3, re.M)#Using regular expression to fid and store the sequences of genes.

  numbers=[]
  for seq in seqs:
    numbers.append(len(re.findall('GAATTC',seq)))#These three lines is to create a list that stores the number of "GAATTC" in each gene.
  
  new = ''
  for i in range(len(seqs)):
    new += f'>{names[i]}  {numbers[i]+1}\n{seqs[i]}\n'#Note that the number of the fragments it cut is the number of 'GAATTC' plus 1.
  print(new)
  newfile.write(new)#These 4 lines output the result in the format of 'gene names','numbers of fragments that can be cut by Ecoli','gene sequence',
  #and then write them in the file.


