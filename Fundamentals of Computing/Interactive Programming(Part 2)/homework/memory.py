import simplegui
import random

deck = range(1, 9) + range(1, 9)
random.shuffle(deck)

exposed = [True, True , True, True, True, True, True, True, True, True, True, True, True, True, True, True]

turn = 0

# helper function to initialize globals
def new_game():
    global turn, exposed
    turn = 0
    label.set_text("Turns = 0")
    random.shuffle(deck)
    exposed = [True, True , True, True, True, True, True, True, True, True, True, True, True, True, True, True]



def countF():
    listF = list()
    for i in range(16):
        if exposed[i] == False:
            listF.append(i)
    return len(listF)



# define event handlers
def mouseclick(pos):
    x = countF()
    for i in range(16):
        if (0 + 50 * i) < pos[0] < (50 + 50 * i):
            if exposed[i] == True:
                global turn
                turn = turn + 1
                label.set_text("Turns = " + str(turn/2))
                if x == 0:
                    exposed[i] = False
                elif x == 1:
                    if deck[exposed.index(False)] == deck[i]:
                        exposed[i] = 'P'
                        exposed[exposed.index(False)] = 'P'
                    else:
                        exposed[i] = False
                elif x == 2:
                    exposed[exposed.index(False)] = True
                    exposed[exposed.index(False)] = True
                    exposed[i] = False



# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(16):
        canvas.draw_text(str(deck[i]), (15 + 50 * i, 65), 40, 'White')
        if exposed[i] == True:
            canvas.draw_polygon([(0 + 50 * i, 0), (50 + 50 * i, 0), (50 + 50 * i, 100), (0 + 50 * i, 100)], 1, 'Black', 'Gold')
        elif exposed[i] == False:
            canvas.draw_polygon([(0 + 50 * i, 0), (50 + 50 * i, 0), (50 + 50 * i, 100), (0 + 50 * i, 100)], 1, 'Gold')
        elif exposed[i] == 'P':
            canvas.draw_polygon([(0 + 50 * i, 0), (50 + 50 * i, 0), (50 + 50 * i, 100), (0 + 50 * i, 100)], 1, 'Gold')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()