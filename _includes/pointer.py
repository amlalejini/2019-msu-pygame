import sys
import math
import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

LIGHT_GREY = [230, 230, 230]
RED = [150, 0, 0]
BLACK = [0, 0, 0]
BLUE = [0, 0, 150]

PROJECTILE_SPEED = 5
PROJECTILE_RADIUS = 10

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pointer game")

clock = pygame.time.Clock()

mid_point = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)] # We'll be shooting projectiles from the middle of the screen

projectiles = [] # Here's where we'll track projectiles

while True:
    screen.fill(LIGHT_GREY)

    mouse_pos = pygame.mouse.get_pos() # We'll be using the mouse position to fire projectiles from

    pygame.draw.circle(screen, RED, mid_point, 20) # Draw a circle in the middle of the screen (where we'll shoot from)
    pygame.draw.circle(screen, RED, mouse_pos, 10) # Draw a circle to tell the player where they're targetting

    # Draw a line from the mid point to the mouse position
    pygame.draw.line(screen, BLACK, mid_point, mouse_pos, 3)

    ############################################################################
    # Draw all of the projectiles, track on screen vs off screen
    ############################################################################
    # Let's get the unit vector for the line we just drew
    # - at the same time, we'll track what projectiles are still on the screen
    on_screen_projectiles = []
    for projectile in projectiles:
        # Move the projectile in the correct direction
        # - projection["direction"] is a unit vector pointing in the direction we want this projectile to travel
        #   - We multiply the direction vector's x and y by our speed to have the projectile
        #     move in the correction direction at the correct speed
        projectile["current_loc"][0] += (PROJECTILE_SPEED * projectile["direction"][0])
        projectile["current_loc"][1] += (PROJECTILE_SPEED * projectile["direction"][1])

        # For convenience, we'll grab the current location (that we just calculated)
        # for this projectile
        cur_loc = projectile["current_loc"]
        pygame.draw.circle(screen, BLUE, [int(cur_loc[0]), int(cur_loc[1])], PROJECTILE_RADIUS)

        # Detect whether the projectile is off of the screen
        # - To do that, we can make a bounding box around the circle and
        #   detect whether or not that circle's bounding box is colliding with
        #   a bounding box around the entire screen
        projectile_box = pygame.Rect([0,0],[0,0])
        projectile_box.centerx = cur_loc[0]
        projectile_box.centery = cur_loc[1]
        projectile_box.width = 2*PROJECTILE_RADIUS
        projectile_box.height = 2*PROJECTILE_RADIUS
        # Use that bounding box to detect if something goes off screen
        if screen.get_rect().colliderect(projectile_box):
            on_screen_projectiles.append(projectile)
    projectiles = on_screen_projectiles
    ############################################################################

    # Here's our event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Calculate the vector from where we're shooting (mid_point) to
            # where we're aiming (mouse_pos)
            # - If instead, you were shooting from a character's location, you could use
            #   that character's location instead of the mid_point of the screen.
            line_vec = [mouse_pos[0] - mid_point[0], mouse_pos[1] - mid_point[1]]
            # How long is the vector? (lookup python's math.hypot function in the
            # python docs)
            vec_len = math.hypot(line_vec[0], line_vec[1])
            # Calculate the unit vector => we'll use this to specify the direction of the projectile
            unit_vec = [line_vec[0] / vec_len, line_vec[1] / vec_len]
            # Add new projectile to projectiles list
            projectiles.append({"current_loc": [mid_point[0], mid_point[1]], "direction": unit_vec})

    pygame.display.update()
    clock.tick(FPS)
