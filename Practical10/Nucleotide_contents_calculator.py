def percentage_nucleotide(seq):#Defining a function called percentage_nucleotide
    seq=str(seq).upper()#Unifying the format into upper case.
    A_percentage=seq.count('A')/len(seq)#The four lines below count seperately the percentage of different nucleotides in the sequence.
    T_percentage=seq.count('T')/len(seq)
    C_percentage=seq.count('C')/len(seq)
    G_percentage=seq.count('G')/len(seq)
    print(format(A_percentage,'.3%'),format(T_percentage,'.3%'),format(C_percentage,'.3%'),format(G_percentage,'.3%'))#Output the percentage and keep three decimal places.


percentage_nucleotide('GAATTCCCtGGCCAAACCTATCGGaaC')# An example.
