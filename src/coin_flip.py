import random
import time

'''
A game of heads or tails built without using a tutorial. 
Applying concepts learned via Codeacademy.
'''

# Defining global variables for the game
POSITIVE_RESPONSES = ['yes', 'sure', 'why not', 'yep', 'yes please', 'yeah']
NEGATIVE_RESPONSES = ['nope', 'no', 'nah', 'no way', 'no thanks']
COIN_OPTIONS = ['heads', 'tails']
all_user_choices = []
previous_coin_flips = []


# Function to strip user inputs for use in different functions throughout the game
def stripping_answer(answer):
    stripped_answer = answer.strip()
    final_answer = stripped_answer.lower()
    return final_answer


# Function to verify if a user wants to play a game
def verify_user_response(user_answer):
    answer = stripping_answer(user_answer)
    if answer in POSITIVE_RESPONSES:
        print("Woohoo let\'s play")
        return "yes"
    elif answer in NEGATIVE_RESPONSES:
        print("Oh well.. I guess that is game over!")
        return "no"
    else:
        print("Sorry I don\'t understand your answer. Please type yes or no.")
        return "unknown"


def play_game(answer):
    if answer == 'yes':
        choice = user_choice_heads_or_tails()
        coin_flip_game(choice)
    elif answer == 'no':
        return "Thanks for playing!"
    else:
        play_a_game()


# Function to allow the user to input their choice in 'heads or tails' game
def user_choice_heads_or_tails():
    user_choice = input("Heads or Tails? \n")
    choice = stripping_answer(user_choice)
    if choice in COIN_OPTIONS:
        return choice
    else:
        print("Sorry I don\'t understand your answer. Please type heads of tails.")
        return user_choice_heads_or_tails()


# Function to flip the coin and return winner or loser
def coin_flip_game(user_input):
    flip = random.choice(COIN_OPTIONS)
    all_user_choices.append(user_input)
    previous_coin_flips.append(flip)
    print("And the coin says...\n..\n.\n")
    time.sleep(3)
    print(flip)
    time.sleep(1)
    if all_user_choices[-1] == flip:
        print("We have a Winner!!!")
    else:
        print("Unlucky - maybe you\'ll win next time :(")
    time.sleep(1)
    replay_game()


# Function to replay the game
def replay_game():
    counting_coin_flips(previous_coin_flips)
    user_answer = input("Would you like to play again? \n")
    answer = verify_user_response(user_answer)
    play_game(answer)


# Function to count coin flips - take a list of 'Heads' or 'Tails' and will return the count
def counting_coin_flips(previous_coin_flips):
    count_heads = 0
    count_tails = 0
    for flip in previous_coin_flips:
        if flip == 'heads':
            count_heads += 1
        else:
            count_tails += 1
    print("So far the coin has flipped {} Heads and {} Tails".format(count_heads, count_tails))


# Function to start the gam
def play_a_game():
    user_answer = input("Would you like to play a game? \n")
    verified_answer = verify_user_response(user_answer)
    play_game(verified_answer)


play_a_game()