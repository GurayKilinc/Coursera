import random
import simplegui

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

def get_p(p_choice):
    print "Player chooses ", p_choice
    p_num = name_to_number(p_choice)
    return p_num

def get_c():
    c_num = random.randint(0, 4)
    c_choice = number_to_name(c_num)
    print "Computer chooses ",c_choice
    return c_num

def rpsls(p_choice):
    differ = get_p(p_choice) - get_c()
    if differ == 0:
        print "Draw!\n"
    elif differ % 5 == 1 or differ % 5 ==2:
        print "Player wins!\n"
    elif differ % 5 == 3 or differ % 5 ==4:
        print "Computer wins!\n"

frame = simplegui.create_frame("RPSLS", 200, 200)
frame.add_input("Enter your guess: ", rpsls, 200)

frame.start()