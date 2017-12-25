import simplegui
# define global variables
count = 0
time_count = 0
s_stop = 0
stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def timer_handler():
    global count, time_count
    count = count + 1
    if count % 6000 == 0:
        count = 0
        time_count = 0
    else:
        time_count = count % 6000

def format(t):
    a = str(int(t) / 600)
    if t < 100:
        bcd = "0" + str((int(t) % 600) / 10.0)
    else:
        bcd = str((int(t) % 600) / 10.0)
    return a + ":" + bcd

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    timer.start()

def button_handler2():
    timer.stop()
    global stop, s_stop
    stop = stop + 1
    if count % 1000 == 0:
        s_stop = s_stop + 1
    else:
        s_stop = s_stop

def button_handler3():
    timer.stop()
    global count, time_count, s_stop, stop
    count = 0
    time_count = 0
    s_stop = 0
    stop = 0

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_count), (55, 120), 40, 'Red')
    canvas.draw_text(str(s_stop) + "/" + str(stop), (180, 10), 12, 'Red')

# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)

# register event handlers
frame.add_button('Start', button_handler1, 50)
frame.add_button('Stop', button_handler2, 50)
frame.add_button('Reset', button_handler3, 50)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()