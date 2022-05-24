seq='ATGCAATCGACTACGATCAATCGAGGGCC'#This is the variable 'seq'.
import re
seq2 = re.sub('GAATTC', 'G^AATTC', seq)#Substituing the GAATTC to G^AATTC for segmentation and counting the number of fragements.
seq3 = seq2.split('^') #Split the sequence into fragments according to '^'.
print(len(seq3))  #Output the number of fragments. From this output we can see that there is no GAATTC sequence in this 'seq', 
                  #so the number of fragements will be 1, which is still the original sequence.