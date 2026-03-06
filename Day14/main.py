"""Imports"""
from art import logo, vs
import random
from game_data import data
account_b = random.choice(data)

""" Format the account data into printable format."""
def format_data(account):
    # Current format: {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States'}
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

"""Use if statement to check if user is correct"""
def check_answer(user_guess, a_followers, b_followers):
    # Take a user's guess and the follower counts and returns if they got it right.
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True

"""Make the game repeatable"""
while game_should_continue:
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    # Generate a random account from the game data.
    if account_a == account_b:
        account_b = random.choice(data) # Making sure the two accounts are different

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    """Ask user for a guess"""
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    """Clear the screen"""
    print("\n" * 20)
    print(logo)

    """Check if user is correct
    Get follower count of each account"""
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_corrrect = check_answer(user_guess, a_followers, b_followers)

    """Give user feedback on their guess
    Score keeping:"""
    if is_corrrect:
        score += 1
        print(f"You're right! Current score: {score}") # while loop continues to run, as game_should_continue is still True
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False # exits the while loop and ends the game.
