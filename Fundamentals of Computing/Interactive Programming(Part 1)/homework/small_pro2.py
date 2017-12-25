import simplegui

a = 5

def keydown_handler(key):
    global a
    a = a * 2
    print a

def keyup_handler(key):
    global a
    a = a - 3
    print a

frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)

frame.start()
