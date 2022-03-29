import pygame
from game.world import textures
from game.parameters import parameters


def get_sprite(block):
    if block == 'air':
        texture = textures.t_air
    elif block == 'stone':
        texture = textures.t_stone
    elif block == 'dirt':
        texture = textures.t_dirt
    elif block == 'grass':
        texture = textures.t_grass
    elif block == 'granite':
        texture = textures.t_granite
    elif block == 'basalt':
        texture = textures.t_basalt
    elif block == 'marble':
        texture = textures.t_marble
    elif block == 'water':
        texture = textures.t_water
    elif block == 'sand':
        texture = textures.t_sand
    elif block == 'log':
        texture = textures.t_stone
    elif block == 'planks':
        texture = textures.t_stone
    elif block == 'bricks':
        texture = textures.t_stone
    elif block == 'glass':
        texture = textures.t_stone
    else:  # if block id is unset
        texture = textures.t_stone
    sprite = pygame.transform.scale(texture, (parameters.block_size, parameters.block_size))
    return sprite
    # if (x + y) % 2 == 0:  # Block grid
    #     block_color = block_color[0] - 16, block_color[1] - 16, block_color[2] - 16
    # if (chunk_x + chunk_y) % 2 == 0:  # Chunk grid
    #     block_color = block_color[0] - 16, block_color[1] - 16, block_color[2] - 16
