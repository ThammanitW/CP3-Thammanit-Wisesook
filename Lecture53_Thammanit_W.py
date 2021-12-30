totalPrice = int (input ("Price exclude vat : "))
def vatCalculate(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result
print("Total Price : ", vatCalculate(totalPrice))
