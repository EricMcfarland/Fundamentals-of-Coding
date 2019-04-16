'''
minimal functional requirements:
    simplegui with the following
        -a start, stop, and reset button
            -start: when pressed will begin the canvas to update the elapsed time display every one tenth of a second (0.1 seconds)
            -stop: when pressed will stop the elapsed time display and display the elapsed time since the start button was pressed
            -reset: when pressed will reset the elapsed timer display to 0:00.0 and stop and reset the current running timer
        -a canvas to display the elapsed time in A:BC.D format

    General display strategy:
    e_time will be an int counting tenth of seconds therefore e_time = 10 is 1 seconds,
                                                              e_time = 600 is 1 minute

    tenth seconds are determined by: e_time % 10 as it returns the last digit remainder
                                        ex: e_time = 425  425 % 10  => 5

    seconds are determined by: e_time//10 but with upper bound of 59
                                        ex: e_time = 425  425//10 = 4

    minutes are determined by: e_time//600 with no upper bound in this case but should be 59
                                        ex: e_time = 1025  1025//600 = 1

    in the case of minutes and seconds the leading zeros will be kept for values less than 10
    when seconds = 60 it should be reset to 00 and minutes increased

'''

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# template for "Stopwatch: The Game"

# define global variables
elapsed_time = 0               #in tenths of seconds
frame_width = 500
frame_height = 500
attempts = 0
successful_attempts = 0
tenth_seconds = 0


# define helper function
def format_time(t):
    # converts a number of int tenth second counts into the A:BC.D time format
    # 10 one hundredth seconds (D) = 1 second (BC)
    # 60 seconds = minute (A)
    # hours are ignored
    global tenth_seconds

    minutes = t // 600
    remaining_time = t % 600

    seconds = remaining_time//10
    remaining_time = remaining_time % 10

    tenth_seconds = remaining_time

    #add leading zeroes
    if minutes < 10:
        minutes = "0" + str(minutes)

    if seconds <10:
        seconds = "0" + str(seconds)


    time_string = str(minutes) + ":" + str(seconds) + "." + str(tenth_seconds)
    return time_string


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_watch():
    if not timer.is_running():
        timer.start()
    else:
        print "timer already started. Stop or Reset to proceed"


def stop_watch():
    global tenth_seconds, successful_attempts, attempts
    if timer.is_running():
        if tenth_seconds == 0:
            successful_attempts += 1

        attempts += 1

    timer.stop()



def reset_watch():
    global elapsed_time, successful_attempts, attempts
    timer.stop()
    elapsed_time = 0
    attempts = 0
    successful_attempts = 0



# define event handler for timer with 0.1 sec interval
def tick():
    global elapsed_time
    elapsed_time += 1


# define draw handler
def draw(canvas):
    global elapsed_time
    formatted_time = format_time(elapsed_time)
    canvas.draw_text(formatted_time, (200, 200), 50, "Blue")
    canvas.draw_text(str(attempts), (400, 100), 50, "Pink")
    canvas.draw_text(str(successful_attempts) + " /", (350, 100), 50, "Green")


# create frame
frame = simplegui.create_frame("Stop Watch", frame_width, frame_height)

# register event handlers
start_btn = frame.add_button("Start", start_watch)
stop_btn = frame.add_button("Stop", stop_watch)
reset_btn = frame.add_button("Reset", reset_watch)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
