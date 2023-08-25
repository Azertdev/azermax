UserNumber = int(input("entrer un nombre : "))
if UserNumber < 0:
    print(f"{UserNumber} is negative")
elif UserNumber > 0:
    print(f"{UserNumber} is positive")
else:
     print("User Number is zero")    