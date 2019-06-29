'''
Hover your mouse over one of the 6 squares to adjust the background color.
'''

import sys
import random
import pygame

# Initialize pygame
pygame.init()

# Some constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

LIGHT_GREY = [230, 230, 230]

# Create the display surface
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Collider Demo")

# Make a clock to manage frames per second
clock = pygame.time.Clock()

mouse_rect = pygame.Rect([0, 0], [30, 30])
whitered_wall_rect = pygame.Rect([250, 200], [100, 100])
whitegreen_wall_rect = pygame.Rect([550, 200], [100, 100])
whiteblue_wall_rect = pygame.Rect([850, 200], [100, 100])
blackred_wall_rect = pygame.Rect([250, 350], [100, 100])
blackgreen_wall_rect = pygame.Rect([550, 350], [100, 100])
blackblue_wall_rect = pygame.Rect([850, 350], [100, 100])

# Game loop
w_color = [0, 0, 0]
while True:
    # Set the background color
    screen.fill(w_color)

    mouse_position = pygame.mouse.get_pos()
    mouse_rect.centerx = mouse_position[0]
    mouse_rect.centery = mouse_position[1]

    if mouse_rect.colliderect(whitered_wall_rect):
        if w_color[0] <= 254:
            w_color[0] = (w_color[0] + 1)
    if mouse_rect.colliderect(whitegreen_wall_rect):
        if w_color[1] <= 254:
            w_color[1] = (w_color[1] + 1)
    if mouse_rect.colliderect(whiteblue_wall_rect):
        if w_color[2] <= 254:
            w_color[2] = (w_color[2] + 1)
    if mouse_rect.colliderect(blackred_wall_rect):
        if w_color[0] >= 1:
            w_color[0] = (w_color[0] - 1)
    if mouse_rect.colliderect(blackgreen_wall_rect):
        if w_color[1] >= 1:
            w_color[1] = (w_color[1] - 1)
    if mouse_rect.colliderect(blackblue_wall_rect):
        if w_color[2] >= 1:
            w_color[2] = (w_color[2] - 1)


    pygame.draw.rect(screen, [255, 100, 100], whitered_wall_rect)
    pygame.draw.rect(screen, [100, 255, 100], whitegreen_wall_rect)
    pygame.draw.rect(screen, [100, 100, 255], whiteblue_wall_rect)
    pygame.draw.rect(screen, [155, 0, 0], blackred_wall_rect)
    pygame.draw.rect(screen, [0, 155, 0], blackgreen_wall_rect)
    pygame.draw.rect(screen, [0, 0, 155], blackblue_wall_rect)
    pygame.draw.rect(screen, [0, 0, 0], mouse_rect)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display, tick clock
    pygame.display.update()
    clock.tick(FPS)
