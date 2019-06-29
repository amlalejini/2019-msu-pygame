'''
Enemies (red rectangles) follow the character (green rectangle) around. Move character
with WASD.
'''

import pygame
import random
import sys

char_start_x = 450
char_start_y = 450
char_x_val = 450    #this is the x cordinate value
char_y_val = 450    #this is the y cordinate value
char_width = 30
char_height = 30
char_speed = 5      # How fast does character move?
cur_char_x_vel = 0  # What's the character's current x speed?
cur_char_y_vel = 0  # What's the character's current y speed?

FPS = 60

LIGHT_GREY = [230, 230, 230]
GREEN = [0,255,0]
RED = [255,0,0]

screen_width = 900
screen_height = 900

health = 500

character = pygame.Rect([char_x_val, char_y_val], [char_width, char_height])
screen = pygame.display.set_mode([screen_width, screen_height])
safe_space = pygame.Rect(250,250,450,450)

def get_enemy_rect():
    while True:
        enemy_width = 25
        enemy_height = 25
        enemy_x_val = random.randint(0,900)
        enemy_y_val = random.randint(0,900)

        enemy_rect = pygame.Rect([enemy_x_val,enemy_y_val],[enemy_width,enemy_height])
        if not enemy_rect.colliderect(safe_space):
            return enemy_rect

enemies = []
amount_enemies = 3
place_holder_enemies = 3

clock = pygame.time.Clock()

for i in range(amount_enemies):
    enemies.append(get_enemy_rect())

while True:
    screen.fill(LIGHT_GREY)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        #print("up arrow")
        cur_char_y_vel = -1*char_speed
        char_y_val -= 5
        char_start_y -= 5
    elif pressed_keys[pygame.K_s]:
        #print("down arrow")
        cur_char_y_vel = char_speed
        char_y_val += 5
        char_start_y += 5
    else:
        cur_char_y_vel = 0
    # - Is player moving horizontally?
    if pressed_keys[pygame.K_d]:
        #print("down arrow")
        cur_char_x_vel = char_speed
        char_x_val += 5
        char_start_x += 5
    elif pressed_keys[pygame.K_a]:
        #print("down arrow")
        cur_char_x_vel = -1*char_speed
        char_x_val -= 5
        char_start_x -= 5
    else:
        cur_char_x_vel = 0

    # Draw the character!
    character.left += cur_char_x_vel
    character.top += cur_char_y_vel
    pygame.draw.rect(screen, GREEN, character)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Are any enemies colliding with the character?
    for enemy in enemies:
        if character.colliderect(enemy):
            health = health - 1

    # Have the enemies move toward the character
    for enemy in enemies:
        if char_x_val > enemy.left:
            enemy.left += 2
        if char_x_val < enemy.left:
            enemy.left -= 2
        if char_y_val > enemy.top:
            enemy.top += 2
        if char_y_val < enemy.top:
            enemy.top -= 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)