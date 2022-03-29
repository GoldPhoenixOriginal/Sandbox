import pygame

from game.parameters import parameters


def block_grid():
    block_grid_surface = pygame.Surface(parameters.size)
    block_grid_surface.set_colorkey((0, 0, 0))
    block_grid_surface.set_alpha(64)

    for y in range(parameters.blocks_y + 1):
        for x in range(parameters.blocks_x + 1):
            block_cords = x * parameters.block_size - parameters.move_x % parameters.block_size, \
                          y * parameters.block_size - parameters.move_y % parameters.block_size, \
                          parameters.block_size, parameters.block_size

            pygame.draw.rect(block_grid_surface, (255, 255, 255), block_cords, 1)
    parameters.screen.blit(block_grid_surface, (0, 0))


def chunk_grid():
    chunk_grid_surface = pygame.Surface(parameters.size)
    chunk_grid_surface.set_colorkey((0, 0, 0))
    chunk_grid_surface.set_alpha(255)

    fx = (parameters.x + parameters.move_x // parameters.block_size) // 16
    fy = (parameters.y + parameters.move_y // parameters.block_size) // 16
    for chunk_y in range(fy, fy + parameters.blocks_y // 16 + 2, 1):
        for chunk_x in range(fx, fx + parameters.blocks_x // 16 + 2, 1):
            x = ((chunk_x - fx) * 16 - parameters.move_x // parameters.block_size % 16) * parameters.block_size \
                - parameters.move_x % parameters.block_size
            y = ((chunk_y - fy) * 16 - parameters.move_y // parameters.block_size % 16) * parameters.block_size \
                - parameters.move_y % parameters.block_size

            block_cords = x, y, parameters.block_size * 16, parameters.block_size * 16

            pygame.draw.rect(chunk_grid_surface, (255, 255, 0), block_cords, 1)
    parameters.screen.blit(chunk_grid_surface, (0, 0))
