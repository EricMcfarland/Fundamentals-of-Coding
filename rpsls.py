# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random


def name_to_number(name):

    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "No cheating!" + name + " is not a valid option."

    return number


def number_to_name(number):

    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "That number isn't associated with an option"

    return name


def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)

    print ""
    print "Player chooses " + player_choice
    print "Computer chooses " + comp_choice

    difference = (comp_number - player_number) % 5
    # print "diff:" + str(difference)

    if difference == 0:
        # print "diff:" + str(difference)
        print "Player and computer tie!"
    elif (difference == 1) or (difference == 2):
        # print "diff:" + str(difference)
        print "Computer Wins! Boo"
    elif (difference == 3) or (difference == 4):
        # print "diff:" + str(difference)
        print "Player Wins! Yay"
    else:
        print ""


    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
