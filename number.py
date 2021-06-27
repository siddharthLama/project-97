import random
 
i = random.randint(1,9)

chance = 0

print("guess a number (between 1 and 9):")
while chance < 5 :
    guess= int(input("enter your guess -"))

    if guess == i:
        print(" You Won :)")       
    elif guess > i:
        print("Try guessing a lower number than",guess)
    else:
        print("Try guessing a higher number than",guess)  

        chance += 1

if chance < 5:
    print("You Lose :( the number was",i)          