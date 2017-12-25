# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

def rpsls(p_choice):
    print "Player chooses ", p_choice
    p_num = name_to_number(p_choice)
    c_num = random.randint(0, 4)
    c_choice = number_to_name(c_num)
    print "Computer chooses ",c_choice
    differ = p_num - c_num

    if differ == 0:
        print "Player and computer tie!\n"
    elif differ % 5 == 1 or differ % 5 ==2:
        print "Player wins!\n"
    elif differ % 5 == 3 or differ % 5 ==4:
        print "Computer wins!\n"
    #print differ % 5


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")