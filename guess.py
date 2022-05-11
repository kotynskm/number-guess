"""A number-guessing game.

The computer will choose a random number between 1-100 and ask the user to guess the number.

Once the user guesses, the computer will tell the user if their guess was too high or too low.

The game is over once the user guesses the computer's number. When the game is over,
the computer the total number of guesses the user made before getting the right answer.

If the user inputs a number that isn't between 1-100 as requested, ask them to enter a valid number.

When the user guesses the correct number, ask them if they'd like to play again and restart the game, rather than exiting after a correct guess."""

# Play a number guessing game (multiple versions)

import random
# variables
random_num = random.randint(1,100)
print("Welcome to number guessing game!")
username = input("What's your name? ")
print(f'Hi {username}')
user_guess = 0
num_guesses = 0
user_choice = ''
play_again = True

# play game while play again is True
while play_again:
    # Get number guess from the user
    user_guess = int(input("Guess a number between 1 and 100. "))
    # increment number of guesses, and check that guess is valid, guess is too high, or guess is too low
    num_guesses += 1
    if user_guess < 0 or user_guess > 100:
        print("Nice try, that number is out of Range.")
        print("Enter a valid guess ")
    elif user_guess > random_num:
        print(f'Your guess {user_guess} is too high. Guess again.')
    elif user_guess < random_num:
        print(f'Your guess {user_guess} is too low. Guess again.')
        # if user guesses the correct number, print congrats message and ask if they want to play the game again
    elif user_guess == random_num:
        print(f'Congratulations you guessed my number in {num_guesses} tries!')
        user_choice = input("Do you want to play again?")
        if user_choice == 'no':
            play_again = False
        elif user_choice == 'yes':
            random_num = random.randint(1,100)
            num_guesses = 0


# code using max guess variable
import random

random_num = random.randint(1,100)
print("Welcome to number guessing game!")
username = input("What's your name? ")
print(f'Hi {username}')
user_guess = 0
num_guesses = 0
user_choice = ''
max_guesses = 0
# play_again = True

while max_guesses <= 5:
    user_guess = int(input("Guess a number between 1 and 100. "))
    num_guesses += 1
    max_guesses += 1
    if user_guess < 0 or user_guess > 100:
        print("Nice try, that number is out of Range.")
        print("Enter a valid guess ")
    if max_guesses == 5:
        print("Sorry you used all your guess! Game over")
        user_choice = input("Do you want to play again? ")
        if user_choice == 'no':
            print("See you next time.")
            break
        elif user_choice == 'yes':
            random_num = random.randint(1,100)
            num_guesses = 0
            max_guesses = 0
    elif user_guess > random_num:
        print(f'Your guess {user_guess} is too high. Guess again.')
    elif user_guess < random_num:
        print(f'Your guess {user_guess} is too low. Guess again.')
    elif user_guess == random_num:
        print(f'Congratulations you guessed my number in {num_guesses} tries!')
        user_choice = input("Do you want to play again?")
        if user_choice == 'no':
            play_again = False
        elif user_choice == 'yes':
            random_num = random.randint(1,100)
            num_guesses = 0


# code with a number range chosen by the user
import random

# random_num = random.randint(1,100)
print("Welcome to number guessing game!")
username = input("What's your name? ")
print(f'Hi {username}')
start_num = int(input("What would you like the starting number to be? "))
end_num = int(input("What would you like the end number to be? "))
random_num = random.randint(start_num, end_num)
# user_guess = 0
num_guesses = 0
user_choice = ''
max_guesses = 0
# play_again = True

while max_guesses <= 5:
    num_guesses += 1
    max_guesses += 1
    user_guess = int(input(f"Guess a number between {start_num} and {end_num}. "))
    if user_guess < start_num or user_guess > end_num:
        print("Nice try, that number is out of Range.")
        print("Enter a valid guess ")
    if max_guesses == 5:
        print("Sorry you used all your guesses! Game over")
        user_choice = input("Do you want to play again? ")
        if user_choice == 'no':
            print("See you next time.")
            break
        elif user_choice == 'yes':
            start_num = int(input("What would you like the starting number to be? "))
            end_num = int(input("What would you like the end number to be? "))
            random_num = random.randint(start_num, end_num)
            num_guesses = 0
            max_guesses = 0
    elif user_guess > random_num:
        print(f'Your guess {user_guess} is too high. Guess again.')
    elif user_guess < random_num:
        print(f'Your guess {user_guess} is too low. Guess again.')
    elif user_guess == random_num:
        print(f'Congratulations you guessed my number in {num_guesses} tries!')
        user_choice = input("Do you want to play again? ")
        if user_choice == 'no':
            print("See you next time.")
            break
        elif user_choice == 'yes':
            start_num = int(input("What would you like the starting number to be? "))
            end_num = int(input("What would you like the end number to be? "))
            random_num = random.randint(start_num, end_num)
            num_guesses = 0


# code with best guesses variable to keep track of lowest number of guesses made by the user
import random

# random_num = random.randint(1,100)
print("Welcome to number guessing game!")
username = input("What's your name? ")
print(f'Hi {username}')
start_num = int(input("What would you like the starting number to be? "))
end_num = int(input("What would you like the end number to be? "))
random_num = random.randint(start_num, end_num)
# user_guess = 0
num_guesses = 0
user_choice = ''
max_guesses = 0
best_guess = 5
# play_again = True

while max_guesses <= 10:
    num_guesses += 1
    best_guess += 1
    max_guesses += 1
    user_guess = int(input(f"Guess a number between {start_num} and {end_num}. "))
    if user_guess < start_num or user_guess > end_num:
        print("Nice try, that number is out of Range.")
        print("Enter a valid guess ")
    if max_guesses == 10:
        print("Sorry you used all your guesses! Game over")
        user_choice = input("Do you want to play again? ")
        if user_choice == 'no':
            print("See you next time.")
            break
        elif user_choice == 'yes':
            start_num = int(input("What would you like the starting number to be? "))
            end_num = int(input("What would you like the end number to be? "))
            random_num = random.randint(start_num, end_num)
            num_guesses = 0
            max_guesses = 0
    elif user_guess > random_num:
        print(f'Your guess {user_guess} is too high. Guess again.')
    elif user_guess < random_num:
        print(f'Your guess {user_guess} is too low. Guess again.')
    elif user_guess == random_num:
        print(f'Congratulations you guessed my number in {num_guesses} tries!')
        if num_guesses < best_guess:
            best_guess = num_guesses
            print(f"Your best number of guesses is {best_guess}")
        user_choice = input("Do you want to play again? ")
        if user_choice == 'no':
            print("See you next time.")
            break
        elif user_choice == 'yes':
            start_num = int(input("What would you like the starting number to be? "))
            end_num = int(input("What would you like the end number to be? "))
            random_num = random.randint(start_num, end_num)
            num_guesses = 0











