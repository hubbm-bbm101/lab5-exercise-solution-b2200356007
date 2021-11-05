import random
number=random.randint(1,10)
guess=int(input("guess a number between 1 and 10="))
while guess!=number:
    if guess>number:
        print("decrease your number")
    elif guess<number:
        print("increase your number")
    guess=int(input("guess a number between 1 and 10="))
if guess==number:
    print("you won!")