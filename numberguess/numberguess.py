import random

number = random.randint(1, 50)

print("Guess the number (1 to 50)")
print("You have 3 chances")

for i in range(3):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("You win!")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
else:
    print("You lost")
    print("Number was:", number)