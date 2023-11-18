import random
a = int(input("Guess a number: "))
b=int(random.uniform(1,10))
print(b)
if(a<b):
    print("You guessed too low")
elif(a>b):
    print("You guessed too hight")
else:
    print("YOu guessed it RIGHT!!!")