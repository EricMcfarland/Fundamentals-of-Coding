try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# initializing global variables.
secret_number = -1
remaining_guesses = -1
game_mode = 100

frame_width = 500
frame_height = 300

def new_game_100():
    global secret_number, remaining_guesses, game_mode
    secret_number = random.randrange(0, 100)
    print "new game started. Select a number between 0-99"
    remaining_guesses = 7
    game_mode = 100


def new_game_1000():
    global secret_number, remaining_guesses,game_mode
    secret_number = random.randrange(0, 1000)
    print "new game started. Select a number between 0-999"
    remaining_guesses = 10
    game_mode = 1000


def start_new_game(game_mode):
    if game_mode == 100:
        new_game_100()
    elif game_mode == 1000:
        new_game_1000()
    else:
        "Help!"


def input_guess(guess):
    global remaining_guesses, game_mode
    guess_int = int(guess)
    print "Guess was " + guess

    if guess_int > secret_number:
        print "Go Lower"

    elif guess_int == secret_number:
        print "Correct!"

        # once secret number has been found start the game over in the current mode
        start_new_game(game_mode)

        # Break from current event handling
        return
    elif guess_int < secret_number:
        print "Go Higher"

    else:
        print "Something went wrong"

    remaining_guesses -= 1
    print "You have " + str(remaining_guesses) + " guesses left"
    print ""
    if remaining_guesses < 1:
        print "You lose"
        start_new_game(game_mode)


# initialize game mode to 0-99
new_game_100()

f = simplegui.create_frame("Guess The Number!", frame_width, frame_height)
input_box = f.add_input("Guess a value", input_guess, 50)
game_100 = f.add_button("Start new game between 0-99", new_game_100, 100)
game_1000 = f.add_button("Start new game between 0-999", new_game_1000, 100)

f.start()

