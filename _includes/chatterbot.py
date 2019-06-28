'''
Chatty NPC example
'''

import sys
import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60


RED = [150, 0, 0]
LIGHT_GREY = [230, 230, 230]
BLACK = [0, 0, 0]
BLUE = [0, 0, 150]
ORANGE = [245, 180, 65]

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Chatty NPC")

clock = pygame.time.Clock()

font = pygame.font.SysFont('impact', 18)

NPC_WIDTH = 25
NPC_HEIGHT = 25
NPC_X = int(0.75 * SCREEN_WIDTH)
NPC_Y = int(0.5 * SCREEN_HEIGHT)
NPC_INTERACT_RANGE = 10 # How many pixels away from the NPC can you interact with it?
best_bud = {"rect":             pygame.Rect([NPC_X, NPC_Y], [NPC_WIDTH, NPC_HEIGHT]),
            "interaction_rect": pygame.Rect([NPC_X - NPC_INTERACT_RANGE, NPC_Y - NPC_INTERACT_RANGE], [NPC_WIDTH + (2*NPC_INTERACT_RANGE), NPC_HEIGHT + (2*NPC_INTERACT_RANGE)]),
            "can_interact":     False,
            "talkietalkie":     "Hi there my good friend!",
            "text_visible":      False}


CHAR_START_X = 0
CHAR_START_Y = 0
CHAR_WIDTH = 15
CHAR_HEIGHT = 15
CHAR_SPEED = 5
character = pygame.Rect([CHAR_START_X, CHAR_START_Y], [CHAR_WIDTH, CHAR_HEIGHT])

while True:
    screen.fill(LIGHT_GREY)

    # Update character
    pressed_keys = pygame.key.get_pressed()
    cur_char_vel = [0, 0]
    # - vertical movement
    if pressed_keys[pygame.K_w]:
        cur_char_vel[1] = -1*CHAR_SPEED
    elif pressed_keys[pygame.K_s]:
        cur_char_vel[1] = CHAR_SPEED
    # - horizontal movement
    if pressed_keys[pygame.K_d]:
        cur_char_vel[0] = CHAR_SPEED
    elif pressed_keys[pygame.K_a]:
        cur_char_vel[0] = -1*CHAR_SPEED
    character.left += cur_char_vel[0]
    character.top += cur_char_vel[1]


    # Is the character in range to interact with the NPC?
    if character.colliderect(best_bud["interaction_rect"]):
        best_bud["can_interact"] = True
    else:
        best_bud["can_interact"] = False
        best_bud["text_visible"] = False

    ############################################################################
    # DRAWING
    ############################################################################

    # Draw our best bud
    # pygame.draw.rect(screen, BLACK, best_bud["interaction_rect"])
    pygame.draw.rect(screen, RED, best_bud["rect"])

    pygame.draw.rect(screen, BLUE, character)

    if best_bud["text_visible"]:
        # Text should be visible!
        text_surf = font.render(best_bud["talkietalkie"], True, BLACK)
        text_box = text_surf.get_rect()
        text_box.centerx = best_bud["rect"].centerx
        text_box.y = best_bud["rect"].y - text_box.height - 5
        pygame.draw.rect(screen, ORANGE, text_box)
        pygame.draw.rect(screen, ORANGE, text_box, 3)
        screen.blit(text_surf, text_box)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if best_bud["can_interact"]:
                    best_bud["text_visible"] = not best_bud["text_visible"]


    pygame.display.update()
    clock.tick(FPS)