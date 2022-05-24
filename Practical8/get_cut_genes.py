#This is completed using the 're' module and the application of lists.
import re
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r") as f1:#Opening the original file in read-only mode and stored it as f1.

  f1=f1.read()
  f1=f1.replace('\n','')
  f2=re.split('>',f1)#The 3 lines above is trying to make the file without line feed and split it into a list according to different genes.
  del f2[0]#Deleting the first element in the list because it is a blank.
  gene1=[]#Creating a new list to store the gene with 'GAATTC'.
  for gene in f2:
    if  "GAATTC" in gene:
      gene1.append(gene)
  f3=''.join(gene1)#These 4 lines judge if the 'GAATTC' is within the gene sequence, if yes, put it in a new list.
  
  names=re.findall(r'gene:([^ ]*)',f3)#Using regular expression to find and store the names of genes.
                                                                                                                                                                                 
  seqs=re.findall(r'[ATCG]{7}[ATCG]+',f3, re.M)#Using regular expression to fid and store the sequences of genes.

  lenlist=[]
  for seq in seqs:
    lenlist.append(len(seq))#These three lines is to find and store the length of each gene.
  
  new = ''
  for i in range(len(seqs)):
    new += f'>{names[i]}  {lenlist[i]}\n{seqs[i]}\n'#Output the strings to write in the new file and with the format 'gene name' 'gene length' and 'sequence'
  
with open('cut_genes.fa','w') as newfile:
  newfile.write(new)#Write it into a new file.