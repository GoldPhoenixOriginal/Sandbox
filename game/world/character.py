import pygame

from game.world import textures
from game.parameters import parameters

width = int(parameters.block_size * 1.75) // parameters.zoom
height = int(parameters.block_size * 2.75) // parameters.zoom


def draw():

    cords = (parameters.width - width) // 2, (parameters.height - height) // 2, width, height
    sprite = pygame.transform.scale(textures.t_character, (width, height))

    parameters.screen.blit(sprite, cords)
