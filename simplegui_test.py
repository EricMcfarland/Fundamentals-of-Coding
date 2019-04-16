try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Frame example (April 26, 2014)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Simple "screensaver" program.

# Import modules
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000


# Handler for text box
def update(text):
    global message
    message = text


# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")


# Create a frame
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
timer.start()
frame.start()



# def draw(canvas):
#     canvas.draw_circle([90, 200], 20, 10, "White")
#     canvas.draw_circle([210, 200], 20, 10, "White")
#     canvas.draw_line([50, 180], [250, 180], 40, "Red")
#     canvas.draw_line([55, 170], [90, 120], 5, "Red")
#     canvas.draw_line([90, 120], [130, 120], 40, "Red")
#     canvas.draw_line([180, 108], [180, 160], 140, "Red")
#
# frame = simplegui.create_frame("Test", 300, 300)
# frame.set_canvas_background("#000000")
# frame.set_draw_handler(draw)
#
#
#
#
# frame.start()
