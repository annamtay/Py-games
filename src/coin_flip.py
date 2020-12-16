import random
import time

# Defining global variables for the game
POSITIVE_RESPONSES = ['Yes', 'yes', 'Sure', 'Why not', 'Yep', 'Yes please']
NEGATIVE_RESPONSES = ['Nope', 'No', 'no', 'Nah', 'No way', 'No thanks']
ACCEPTED_RESPONSES = POSITIVE_RESPONSES + NEGATIVE_RESPONSES
COIN_OPTIONS = ['heads', 'tails']


# Function to verify if a user wants to play a game
def yes_or_no():
    user_answer = input("Would you like to play a game? \n")
    stripped_answer = user_answer.strip()
    answer = stripped_answer.lower()
    if answer in POSITIVE_RESPONSES:
        print("Woohoo let\'s play")
        return "yes"
    elif answer in NEGATIVE_RESPONSES:
        print("Oh well.. I gues that is game over!")
        return "no"
    elif answer not in ACCEPTED_RESPONSES:
        print("Sorry I don\'t understand your answer. Please type yes or no.")
        return yes_or_no()


# Function to flip the coin and return winner or loser
def coin_flip_game(user_input):
    all_user_choices = []
    all_user_choices.append(user_input)
    past_flips = []
    flip = random.choice(COIN_OPTIONS)
    past_flips.append(flip)
    print("And the coin says...\n..\n.\n")
    time.sleep(3)
    print(flip)
    time.sleep(1)
    if all_user_choices[-1] == flip:
        print("We have a Winner!!!")
    else:
        print("Unlucky - maybe you\'ll win next time :(")


# Function to allow the user to input their choice in 'heads or tails' game
def user_choice_heads_or_tails():
    user_choice = input("Heads or Tails? \n")
    choice_stripped = user_choice.strip()
    choice = choice_stripped.lower()
    if choice in COIN_OPTIONS:
        return choice
    elif choice not in COIN_OPTIONS:
        print("Sorry I don\'t understand your answer. Please type heads of tails.")
        return user_choice_heads_or_tails()


# Function to play a game
def play_a_game():
    print("Welcome to TayTay's playhouse! It's full of fun and games!")
    answer = yes_or_no()
    if answer == 'yes':
        choice = user_choice_heads_or_tails()
        coin_flip_game(choice)
    return "Thanks for playing!"



print(play_a_game())


# #function to count coin flips - take a list of 'Heads' or 'Tails' and will return the count
# def counting_coin_flips(past_flips):
#     count_heads = 0
#     count_tails = 0
#     for flip in past_flips:
#         if flip == 'Heads':
#             count_heads += 1
#         elif flip == 'Tails':
#             count_tails += 1
#     return count_heads, count_tails
