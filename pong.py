'''
   The goal is to recreate the arcade game known as Pong. The game consists of two paddles that can move vertically
along the left and right wall respectively. A ball is spawned in the middle, moving in a random direction. When the
ball collides with the top and bottom wall it bounces off and continues in its previous x direction. However, if the
ball reaches the gutter areas on the left or right side it does one of two things. If the player has moved their paddle
to collide with the ball it bounces towards the direction of the other side. If the paddle is not there to
meet the ball then the opposing player scores a point and the ball is respawned in the middle with a new initial direction
Each collision made the velocity of the ball is increased.

Minimal functional requirements:
    - A rectangluar game board exists to contain all of the required elements
    - A ball object is spawned at the start of each new game with an initial velocity. The velocity must have an x value
    - A paddle exists on both sides of the board. Movement of these paddles must be controlled by individual keyboard
        presses and may only move in the vertical direction, and must remain in the bounds of the board
    - When the ball object collides with either the top and bottom wall, or the paddle edge the ball's velocity
        must reverse in the perpendicular direction to the collision, increasing the speed by 10%. The parallel
        velocity will remain unchanged other than the speed
    - When the border of the ball object reaches the edge of the gutter on either side of the board a point must
        be awarded to the player on the opposite side and the ball must respawn in the center of the board with a
        random velocity (must have an x velocity)

Approach:
    -Define and draw game board and all objects
        -update each of these objects each draw frame
    -Make functions to implement the motion types of moveable objects
        -spawn the ball
        -give ball velocity
        -check for collision
            -change velocity or score and respawn ball accordingly based on collision type
    -Create handlers to control user input
        -movement of paddles
        -start new game button
    -Make AI?


'''


# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = [PAD_WIDTH/2, HEIGHT/2 - PAD_HEIGHT/2]
paddle1_vel = 0
paddle2_pos = [WIDTH-PAD_WIDTH/2, HEIGHT/2 - PAD_HEIGHT/2]
paddle2_vel = 0
score_left = 0
score_right = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]

    if direction:
        ball_vel[0] = random.randrange(2, 5)
        ball_vel[1] = random.randrange(1, 4)
    else:
        ball_vel[0] = -1*random.randrange(2, 5)
        ball_vel[1] = -1*random.randrange(1, 4)


# helper to detect collision with top/bot walls, paddle, or gutter
def collision(ball_position, paddle1_position, paddle2_position):
    global ball_vel, score_left, score_right

    # Set possible collision points for the ball. The cardinal direction
    ball_collision_points = [ball_position[0] - BALL_RADIUS, ball_position[0] + BALL_RADIUS, ball_position[1] - BALL_RADIUS, ball_position[1] + BALL_RADIUS]
    # print ball_collision_points

    if ball_collision_points[2] <= 0:                                       #Top bounce
        reverse_direction("y", 0.2)
    elif ball_collision_points[3] >= HEIGHT:                                #Bot bounce
        reverse_direction("y", 0.2)
    elif ball_collision_points[0] <= PAD_WIDTH:                             # Left Bounce or OOB
        if paddle1_position[1] <= ball_position[1] <= paddle1_position[1] + PAD_HEIGHT:    #hit left paddle
            reverse_direction("x", 0.2)
        else:                                                               #hit left gutter
            # print "ball: " + str(ball_position)
            # print "left paddle between: " + str(paddle1_pos) + " - [" + str(paddle1_pos[0]) +"," + str(paddle1_pos[1]+PAD_HEIGHT)+ "]"
            spawn_ball(RIGHT)
            score_right += 1
    elif ball_collision_points[1] >= (WIDTH - PAD_WIDTH):                   #Right Paddle Bounce
        if paddle2_position[1] <= ball_position[1] <= paddle2_position[1]+PAD_HEIGHT:      #hit right paddle
            reverse_direction("x", 0.2)
        else:                                                               #right gutter
            # print "ball: " + str(ball_position)
            # print "right paddle between: " + str(paddle2_pos) + " - [" + str(paddle2_pos[0]) +"," + str(paddle2_pos[1]+PAD_HEIGHT) + "]"
            spawn_ball(LEFT)
            score_left += 1


# helper to reverse direction after collision
def reverse_direction(direction, speed):
    global ball_vel
    if direction == "x":
        ball_vel[0] = -(1+speed)*ball_vel[0]
    elif direction == "y":
        ball_vel[1] = -(1+speed)*ball_vel[1]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_left, score_right  # these are ints
    paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle1_vel = 0
    paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle2_vel = 0
    score_left = 0
    score_right = 0
    spawn_ball(RIGHT)


def draw(canvas):
    global score_left, score_right, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    # draw mid line and gutters

    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    if ball_vel == [0, 0]:
        canvas.draw_text("Press Space to Start Game",(WIDTH/5, HEIGHT/2-70) , 40, "White")
        canvas.draw_text("Blue paddle use 'w' and 's' keys. Red use 'up' and 'down' arrows", (WIDTH/12 -10 , 2*HEIGHT/3), 25, "LightSlateGrey")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    ball = canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel

    # test if at edges
    if paddle1_pos[1] <= 0:
        paddle1_pos[1] = 0
    elif paddle1_pos[1] +PAD_HEIGHT >= HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT

    paddle2_pos[1] += paddle2_vel

    # test if at edges
    if paddle2_pos[1] <=0:
        paddle2_pos[1] = 0
    elif paddle2_pos[1] + PAD_HEIGHT >= HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT

    # draw paddles
    canvas.draw_line(paddle1_pos, (paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT), PAD_WIDTH, "Blue")
    canvas.draw_line(paddle2_pos, (paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT), PAD_WIDTH, "Red")

    # determine whether paddle and ball collide
    collision(ball_pos, paddle1_pos, paddle2_pos)

    # draw scores
    canvas.draw_text(str(score_left), (WIDTH / 3, HEIGHT / 5), 50, "Blue")
    canvas.draw_text(str(score_right), (2 * WIDTH / 3, HEIGHT / 5), 50, "Red")


def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    vel = 4
    max_vel = 20
    # move lef paddle up
    if key == simplegui.KEY_MAP["w"]:
        if paddle1_vel <= max_vel:
                paddle1_vel -= vel

    # move left paddle down
    elif key == simplegui.KEY_MAP["s"]:
        if paddle1_vel >= -max_vel:
                paddle1_vel += vel

    # move right paddle up
    elif key == simplegui.KEY_MAP["up"]:
        if paddle2_vel <= max_vel:
                paddle2_vel -= vel

    # move right paddle down
    elif key == simplegui.KEY_MAP["down"]:
        if paddle2_vel >= -max_vel:
                paddle2_vel += vel

    elif key == simplegui.KEY_MAP["space"]:
        new_game()


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Start New Game", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
