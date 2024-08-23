from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to check user's guess against the right answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    # Choose a random number between 1 and 100
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess_number = 0
    while guess_number != answer:
    #Let the user guess a number
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        turns = check_answer(guess_number, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess_number != answer:
            print("Guess again.")

game()
