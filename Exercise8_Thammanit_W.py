username = input ("Username : ")
password = input ("Password : ")
if username == "thammanit" and password == "wisesook":
    print ("Done!")
    print ("-------Big Cat Shop-------")
    print ("-------Product List-------")
    print ("1.Melon Price 30 BHT/kg")
    print ("2.Apple Price 40 BHT/kg")
    print ("3.Banana Price 50 BHT/kg")
    userSelected = int(input("SelectItem >> "))
    if userSelected == 1:
        amountMelon = int(input("Amount Melon : "))
        print("Total", amountMelon * 30, "BHT")
    elif userSelected == 2:
        amountApple = int(input("Amount Apple : "))
        print("Total", amountApple * 40, "BHT")
    elif userSelected == 3:
        amountBanana = int(input("Amount Banana : "))
        print("Total", amountBanana * 50, "BHT")
else:
    print("Error! Please try again.")
