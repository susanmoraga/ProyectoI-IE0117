#!/usr/bin/python3

import pygame
import os

from classes import moving_background
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 400, 600
PLAYER_SIZE = (80, 80)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_BIG = pygame.image.load(os.path.join('Assets', 'wallpaper.jpg'))
BACKGROUND_MAIN = pygame.transform.scale(BACKGROUND_BIG, (WIDTH, HEIGHT))

PLAYER = pygame.image.load(os.path.join('Assets', 'player.png'))

ayuda = moving_background()


class player:
    def __init__(self):
        self.player = pygame.transform.scale(PLAYER, (PLAYER_SIZE))
        self.x_position = 200 - 40
        self.y_position = 600 - 80

    def show(self):
        WINDOW.blit(self.player, (self.x_position, self.y_position))

    def x_movement(self):

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT] and self.x_position < WIDTH - 65:
            self.x_position += 0.15
        elif keys_pressed[pygame.K_LEFT] and self.x_position > -15:
            self.x_position -= 0.15

    def shoot(self):
        a = 0


ru = True
player = player()
while ru:
    WINDOW.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ru = False

    player.show()
    player.x_movement()
    pygame.display.update()
