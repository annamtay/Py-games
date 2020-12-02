import random
import time

# define
POSITIVE_RESPONSES = ['Yes', 'yes', 'Sure', 'Why not', 'Yep', 'Yes please']
NEGATIVE_RESPONSES = ['Nope', 'No', 'no', 'Nah', 'No way', 'No thanks']
ACCEPTED_RESPONSES = POSITIVE_RESPONSES + NEGATIVE_RESPONSES
COIN_OPTIONS = ['heads', 'tails']


# Function to verify if a user wants to play a game
def yes_or_no(answer):
    answers = []
    answers.append(answer)
    while answer not in ACCEPTED_RESPONSES:
        print("Sorry I don\'t understand your answer.")
        answer = input("Yes or no? \n")
        answers.append(answer)
        if answers[-1] in ACCEPTED_RESPONSES:
            break
    if answers[-1] in POSITIVE_RESPONSES:
        print("Woohoo let\'s play")
    elif answers[-1] in NEGATIVE_RESPONSES:
        print("FINE GAME OVER")
        return "Thanks for playing!"

# function to flip the coin and return winner or loser
def coin_flip_game(user_h_or_t_use):
    past_flips = []
    flip = random.choice(COIN_OPTIONS)
    past_flips.append(flip)
    print("And the coin says...\n..\n.\n")
    time.sleep(3)
    print(flip)
    time.sleep(1)
    if user_h_or_t_use == flip:
        print("We have a Winner!!!")
    else:
        print("Unlucky - maybe you\'ll win next time :(")


# A function to start the game
# get user input to play & strip user input of whitespace
# get user input of 'Heads or Tails'
def starting_the_game():
    decision1 = input("Would you like to play a game? \n")
    decision1_stripped = decision1.strip()
    yes_or_no(decision1_stripped)
    user_h_or_t = input("Heads or Tails? \n")
    user_h_or_t_stripped = user_h_or_t.strip()
    user_h_or_t_use = user_h_or_t_stripped.lower()
    if user_h_or_t_use in COIN_OPTIONS:
        print("You guessed " + user_h_or_t_use)
        time.sleep(1)
        coin_flip_game(user_h_or_t_use)
    elif user_h_or_t_use not in COIN_OPTIONS:
        print("I don\'t understand your answer.")
    return "Thanks for playing!"



print(starting_the_game())


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
