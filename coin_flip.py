import random

# define
POSITIVE_RESPONSES = ['Yes', 'yes', 'Sure', 'Why not', 'Yep', 'Yes please']
NEGATIVE_RESPONSES = ['Nope', 'No', 'no', 'Nah', 'No way', 'No thanks']
COIN_OPTIONS = ['Heads', 'Tails']


# function to flip the coin and return winner or loser
def coin_flip_game(user_h_or_t):
    past_flips = []
    flip = random.choice(COIN_OPTIONS)
    past_flips.append(flip)
    print("And the coin says...\n..\n.\n" + flip)
    if user_h_or_t == flip:
        print("We have a Winner!!!")
    else:
        print("Unlucky - maybe you\'ll win next time :(")


# A function to start the game
# get user input to play & strip user input of whitespace
# get user input of 'Heads or Tails'
def starting_the_game():
    user_h_or_t = 0
    decision1 = input("Would you like to play a game? \n")
    decision1_stripped = decision1.strip()
    if decision1_stripped in NEGATIVE_RESPONSES:
        return "Oh no - that\'s a shame! Maybe next time!"
    elif decision1_stripped in POSITIVE_RESPONSES:
        user_h_or_t = input("Woohoo! Heads or Tails? \n")
        if user_h_or_t not in COIN_OPTIONS:
            print("I don\'t understand your answer.")
        elif user_h_or_t in COIN_OPTIONS:
            coin_flip_game(user_h_or_t)
    else:
        return("I don\'t understand your answer. Let\'s try again in the future")
    return "Thanks for playing!"


print(starting_the_game())
