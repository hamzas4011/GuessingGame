import random

print("Welcome to the Number Guessing Game!")
print("You have 3 chances to guess a number between 0 and 9.")

number_to_guess = random.randint(0, 9)
chances = 3
current_attempt = 0

while current_attempt < chances:
    current_attempt += 1
    my_guess = int(input("Enter your guess: "))

    if my_guess == number_to_guess:
        print(f"Correct! The number is {number_to_guess}. You guessed it in {current_attempt} attempts.")
        break
    elif current_attempt >= chances:
        print(f"Sorry, the number was {number_to_guess}. Better luck next time!")
    elif my_guess > number_to_guess:
        print("Your guess is too high!")
    elif my_guess < number_to_guess:
        print("Your guess is too low!")
