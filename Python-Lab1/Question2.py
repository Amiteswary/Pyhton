num = int(input("Enter a number: "))
if(num > 0):
    if(num%2==0):
        print("The number you have entered is a EVEN POSITIVE NUMBER")
    else:
        print("The number you have entered is a ODD POSITIVE NUMBER")
elif(num<0):
    if(num%2==0):
        print("The number you have entered is a EVEN NEGATIVE NUMBER")
    else:
        print("The number you have entered is a ODD NEGATIVE NUMBER")
else:
    print("The number you have entered is ZERO")