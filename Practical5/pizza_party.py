#1. use for Loops to ensure the continous output of a sequence. The range should be 1-64
for i in range(1,65):
#2.define a variable p and caculate p using the formula given.
#use i  as the basic variable to p to make it a sequence output.
    p=(i**2+i+2)/2
    print(i)
    print(p)
#Both i and p printed to make it more clear.

#The code below are to calculate the number of cuts that are required for 64 slices.
m=0  #Created two new variable, use m to represent the total slices
n=1  #Use n ti represent the number of cuts
while m<=64: #Used while loop to determine whether m exceeds 64, if yes, stop the loop and output the value of n.
    n+=1
    m=(n**2+n+2)/2
print(f"The number of cuts needed for 64 slices is {n}.")
    
