def calculator(total_money,price):
    #This function will calulate the number of chocolate bars that can be bought and the remaining changes with total money and the price of each chocolate bar.
    #You should input the total money you have and the price of each chocolate
    number=total_money//price
    change=total_money%price
    return number,change
#An example here
print(calculator(100,7))

