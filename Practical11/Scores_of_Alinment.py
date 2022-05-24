
import pandas as pd
BLOSUM=pd.read_excel('C:/Users/ljc/Desktop/source/code/03Python works/Practical11/BLOSUM.xlsx',index_col=0)#Read the excel file, and set index to the first colum.

seq1='MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY'
#This is the amino acid sequence of human.
seq2='MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY'
#This is the amino acid sequence of mouse.
seq3='GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP'
#This is the random sequence.

def Count(seq4,seq5):#Defining a function (function1) that output the total alignment score.
    total=0
    for i,n in zip(seq4,seq5):
        val=BLOSUM.loc[i,n]
        total+=val
    return total

#Do this function in different sequences.
print(Count(seq1,seq2))
print(Count(seq2,seq3))
print(Count(seq1,seq3))

def percentage(seq4,seq5):#Defining a function (function2) that output the percentage of identical amino acids in each comparison.
    num=0
    for i in range(len(seq4)):
        if seq4[i]==seq5[i]:
            num+=1
    percentage=num/len(seq4)
    return percentage

#Do this function to different sequences.
print(percentage(seq1,seq2))
print(percentage(seq2,seq3))
print(percentage(seq1,seq3))


        

