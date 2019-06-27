"""
This activity is intended to introduce you to Python and a
library for creating video games, PyGame. Thoughout the activity,
you'll see comments (which have a # in them) giving you instructions.

Important note: Python is very sensitive to spaces and tabs, please
ensure that as you change lines as instructed, that you do not change the
indentation of the code.

By: Josh Nahum
"""

# This section of code is needed to get everything set up.
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# This section of code determines the size of the game window
# and sets the title of the window (orginally 800, 600, and Sparty Platformer).
# Try adjusting the game window size and the title.
WINDOW_SIZE = [1200, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sparty Platformer")

# These are some names for common colors.
# A color is determined by 3 numbers (how much red, green, and blue a color has).
# Each of these three numbers use be between 0 and 255.
# Try making a custom color (we'll use it later to be the background of our game.)
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

# This section of code loads a PNG image of Sparty.
# The name of the file is Sparty.png
# If you download another small image off the web,
# place it in the same folder as this activity.py file,
# and replace the filename with the one you downloaded,
# then you will have a different sprite to play width.
# I've included a file called "helmet.png" as a alternative.
sparty_img = pygame.image.load("Sparty.png")
sparty_rectangle = sparty_img.get_rect()

# This section of code is similar to the one above,
# except it loads an image of the goal Sparty is trying
# to get to, a gold coin.
goal_img = pygame.image.load("coin.png")
goal_rectangle = goal_img.get_rect()


# Try changing Sparty's start location by changing the zeroes
# in the next to lines of code to other positive number.
# Notice that larger y values are lower on the screen.
sparty_location_x = 0
sparty_location_y = 0


# These lines determine the height and color of the platforms,
# feel free to adjust these.
platform_height = 10
platform_color = GREEN

# This code makes a single platform that runs along the bottom of the screen,
# please don't change this code.
screen_rectangle = screen.get_rect()
bottom_platform = pygame.Rect(
    screen_rectangle.left,
    screen_rectangle.bottom - platform_height,
    screen_rectangle.right - screen_rectangle.left,
    platform_height)

# This is a list of platforms, initially just 3.
# Each platform is made with 4 numbers (all denoted in pixels)
# 1. The x coordinate of the left-most edge of the rectangle.
# 2. The y coordinate of the top-most edge of the rectangle.
# 3. The width of the rectangle.
# 4. The height of the rectangle (I like my platforms to be the same height of platform_height).
#    But you can use different heights if you prefer.
# Add enough platforms to enable Sparty to reach the goal.
platforms = [
    bottom_platform,
    pygame.Rect(100, 400, 300, platform_height),
    pygame.Rect(300, 500, 150, platform_height),
    pygame.Rect(400, 300, 150, platform_height),
    pygame.Rect(500, 200, 150, platform_height),
    pygame.Rect(600, 100, 500, platform_height),
]


# These next 2 lines determine the intial x and y velocities of the
# player character. The values are the number of pixels to shift the character
# for each frame of animation drawn.
sparty_velocity_x = 0 # Larger means moving faster rightwards
sparty_velocity_y = 0 # Larger means moving faster downwards

# Sparty is subject to gravity (orginally set to 0.3 for Earth),
# try making this value smaller to simulate
# jumping on the moon (0.05). Warning, setting this value too high
# will break the physics of the game.
GRAVITATIONAL_CONSTANT = 0.1

# This variable is used later to determine if Sparty is standing
# on a platform (to determine if Sparty is allowed to jump.)
is_standing = False

# This code is the game loop that listens to key presses,
# calculates the physics,
# draws the background, platforms and Sparty.
while True:
    # The following section of code is responsible for the event loop,
    # which listens for keyboard events and does things (like
    # changing the player's velocity in response.)
    for event in pygame.event.get():
        # If the user clicks the 'X' to close the window, this closes the game and program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            # Should Sparty be allowed to jump when not standing?
            # If so uncomment the next line of code and comment out the line after it
            # This will remove the requirement that Sparty be standing to initiate a jump

            if event.key == pygame.K_UP and is_standing:
            # if event.key == pygame.K_UP:


                # Notice the next 3 numbers (orginally -5, 4, and -4)
                # This values are what the x and y velocities are changed to on button presses
                # Try changing them to make Sparty jump or run faster.
                sparty_velocity_y = -5
            if event.key == pygame.K_RIGHT:
                sparty_velocity_x = 4
            if event.key == pygame.K_LEFT:
                sparty_velocity_x = -4


        # This code ensures that when you release the left or right arrow keys
        # Sparty stops moving.
        # Try commenting out the next 5 lines of code to see what happens

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                sparty_velocity_x = 0
            if event.key == pygame.K_LEFT:
                sparty_velocity_x = 0

    # Physics
    # With every frame of animation drawn, we need to do some math to calculate
    # where Sparty should be drawn.
    # The next line makes Sparty's downward velocity increase due to gravity
    sparty_velocity_y = sparty_velocity_y + GRAVITATIONAL_CONSTANT
    # The next 2 lines calculate Sparty's coordinates given their x and y velocity.
    sparty_location_y = sparty_location_y + sparty_velocity_y
    sparty_location_x = sparty_location_x + sparty_velocity_x


    # The next four sections of code do all the drawing of objects to the screen.

    # Section 1
    # Set the screen background
    # Fill free to change this color to the name of your custom color.
    screen.fill(WHITE)


    # Section 2
    # Draw all the platforms
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)


    # Section 3
    # Draw Sparty (this is the hardest because we need to use Sparty's
    # x and y location to determine where to place them).
    sparty_rectangle.left = sparty_location_x
    sparty_rectangle.top = sparty_location_y
    # If you would prefer Sparty be replaced with a RED rectangle, comment
    # out the next line of code and uncomment out the line after.
    screen.blit(sparty_img, sparty_rectangle)
    # pygame.draw.rect(screen, RED, sparty_rectangle)


    # Section 4
    # Draw the goal (a gold coin) in the top right of the screen.
    goal_rectangle.top = screen_rectangle.top
    goal_rectangle.right = screen_rectangle.right
    screen.blit(goal_img, goal_rectangle)

    # The order in which things are drawn affects what objects
    # occlude (cover up) others. Try swaping the order of Section 2
    # with Section 3 and see what happens if you try to jump up through a platform.



    # The following section of code determines if Sparty is standing
    # on a platform and ensures they don't pass through a platform.
    # This code is a bit complicated because it needs to check which platform Sparty
    # is touching and ensures that Sparty
    # can only land on a platform if they are descending.
    is_standing = False
    index = sparty_rectangle.collidelist(platforms)
    if index != -1:
        touching_platform = platforms[index]
        is_just_touching_down = sparty_rectangle.bottom - touching_platform.top < platform_height

        # To see what happens if Sparty can land on a platform without descending,
        # Comment out the following line and uncomment out the line following.
        # Be sure to try jumping upwards through a platform.
        is_descending = sparty_velocity_y > 0
        # is_descending = True

        if is_just_touching_down and is_descending:
            sparty_location_y = touching_platform.top - sparty_rectangle.height
            is_standing = True
            sparty_velocity_y = 1


    # This section of code determines if Sparty is touching the goal
    # (the image of the gold coin). If it is, move Sparty to position (0, 0)
    # So that the game can repeat.
    if sparty_rectangle.colliderect(goal_rectangle):
        sparty_location_x = 0
        sparty_location_y = 0






    # These two lines of code are responsible for displaying all objects on the screen
    # and fixing the frame rate of our game to 30 frames per second.
    pygame.display.update()
    # Try adjusting the FPS to 10
    clock.tick(30)

# Congratulations you made it to the end!
# This activity was originally created by Dr. Josh Nahum
# and he can be reached at nahumjos@cse.msu.edu

# For more information about PyGame (and Python), check out
# this free book by Al Sweigart titled, "Invent Your Own Computer Games With Python"
# http://inventwithpython.com/