import pygame

from game.parameters import parameters
from game.world import world
from game.world import sprite


class Block:
    id = 'unset'


class Chunk:

    def __init__(self, x, y):
        self.surface = pygame.Surface((16 * parameters.block_size, 16 * parameters.block_size))
        self.blocks = [[Block] * 16 for _ in range(16)]
        self.chunk_x = x
        self.chunk_y = y
        self.make_chunk()

    def make_chunk(self):
        for y in range(16):
            for x in range(16):
                absolute_x = x + self.chunk_x * 16
                absolute_y = y + self.chunk_y * 16
                self.blocks[x][y].id = world.block(absolute_x, absolute_y)  # Get block id

                texture = sprite.get_sprite(self.blocks[x][y].id)  # Get sprite

                block_cords = x * parameters.block_size, y * parameters.block_size, \
                    parameters.block_size, parameters.block_size
                self.surface.blit(texture, block_cords)  # Draw sprite
