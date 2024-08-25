from art import logo
from art import vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

#A loop to make the game repeatable
while should_continue:
    #Position B becomes the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    # Ask user to guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #clear screen
    print("\n" * 20)
    print(logo)
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct =  check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score : {score}")
    else:
        print(f"Sorry, that's wrong. Final score : {score}")
        should_continue = False
