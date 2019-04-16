# Mystery computation in Python
# Takes input n and computes output named result

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math

# global state

result = []
iteration = 0
max_iterations = 1000


# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n


def update():
    global iteration, result, n
    iteration += 1
    if iteration >= max_iterations:
        timer.stop()
        print "The Highest Value is: " + str(max(result)) +". The end value is: " + str(result[-1])
    elif n <= 1:
        timer.stop()
        print "vector is: " + str(result)
        print "The Highest Value is: " + str(max(result)) +". The end value is: " + str(result[-1])

    else:
        if n % 2 == 0:
            n = n/2
            result.append(n)
            print "n is even"
            print "vector is: " + str(result)
        else:
            n = n*3 + 1
            result.append(n)
            print "n is odd"
            print "vector is: " +str(result)


# register event handlers

timer = simplegui.create_timer(1, update)

# start program

init(217)
timer.start()