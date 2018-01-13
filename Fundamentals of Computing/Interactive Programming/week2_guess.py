import random
import simplegui

# helper function to start and restart the game
def new_game():
    global secret_num, max_guess, count
    secret_num = random.randint(0, 100)
    max_guess = 7
    count = 7
    print "New game! Range is 0 to 100."
    print "The limited number of guesses is 7.\n"

# define event handlers for control panel
def range100():
    global secret_num, max_guess, count
    secret_num = random.randint(0, 100)
    max_guess = 7
    count = 7
    print "New game! Range is 0 to 100."
    print "The limited number of guesses is 7.\n"

def range1000():
    global secret_num, max_guess, count
    secret_num = random.randint(0, 1000)
    max_guess = 10
    count = 10
    print "New game! Range is 0 to 1000."
    print "The limited number of guesses is 10.\n"

def input_guess(guess):
    global max_guess, count
    if count > 0:
        print "The limited number of guesses is ", (count - 1)
        print "Guess was ", guess
        if int(guess) == secret_num:
            print "Correct!\n"
        elif int(guess) < secret_num:
            print "Higher!\n"
        elif int(guess) > secret_num:
            print "Lower!\n"
        else:
            print "Out of guesses!\n"
        count = count - 1
    elif count == 0:
        print "Play again! New game starts!\n"
        if max_guess == 7:
            range100()
        elif max_guess == 10:
            range1000()


# create frame
frame = simplegui.create_frame("Guess", 200, 200)
inp = frame.add_input("Input your gusee!", input_guess, 200)
b1 = frame.add_button("Range(0-100)", range100, 100)
b2 = frame.add_button("Range(0-1000)", range1000, 100)

# register event handlers for control elements and start frame
frame.start()

# call new_game
new_game()