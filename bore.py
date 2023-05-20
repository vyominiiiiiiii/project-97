import random

print("Number Guessing Game")
print("Guess a number between(1 and 9):")
x=int(input("Enter you guess: "))
print(x)

if(x>5):
    print("Your guess was too high:Guess a lower number")

elif(x==5):
    print("CONGRATULATION YOU WON!!!")

else:
    print("Your guess was too low:Guess a higher number")