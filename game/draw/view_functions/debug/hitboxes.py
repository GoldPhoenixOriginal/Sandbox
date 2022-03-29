import pygame

from game.parameters import parameters
from game.world import character


def block_hitboxes():
    for y in range(parameters.blocks_y + 1):
        for x in range(parameters.blocks_x + 1):
            block_cords = x * parameters.block_size - parameters.move_x % parameters.block_size, \
                          y * parameters.block_size - parameters.move_y % parameters.block_size, \
                          parameters.block_size, parameters.block_size

            left_side = (parameters.width - character.width) // 2 - 1 * parameters.block_size
            right_side = (parameters.width - character.width) // 2 + character.width
            upper_side = (parameters.height - character.height) // 2 - 1 * parameters.block_size
            lower_side = (parameters.height - character.height) // 2 + character.height

            x_pos = x * parameters.block_size - parameters.move_x % parameters.block_size
            y_pos = y * parameters.block_size - parameters.move_y % parameters.block_size

            if left_side < x_pos < right_side and upper_side < y_pos < lower_side:  # If character covers the block
                pygame.draw.rect(parameters.screen, (0, 255, 0), block_cords, 1)  # Draw hitbox


def character_hitbox():
    cords = (parameters.width - character.width) // 2, (parameters.height - character.height) // 2, \
            character.width, character.height

    pygame.draw.rect(parameters.screen, (255, 0, 0), cords, 1)
