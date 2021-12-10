import random;
print("Number Gusseing Game")
number=random.randint(1,9)
chances=0
print("Gusse A Number (between 1 and 9):")

while chances < 5:
    guess=int(input("Enter Your Guess:-"))


    if guess == number:
        print("Congratulation You Win!!!")
        break
    elif guess < number:
        print("Your Guess Is Too Low:Guess A Number Higher Than",guess)
    else:
        print("Your Guess Is Too High:Guess A Number Lower Than",guess) 

    chances = chances+1

if not chances < 5:
    print("You Lose!!! The Number Is",number)   