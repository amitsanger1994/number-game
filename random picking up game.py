#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                print("Number of attempts:", attempts)
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing Guess the Number!")

guess_the_number()


# In[ ]:




