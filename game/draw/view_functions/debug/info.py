from game.world import world
from game.parameters import parameters
import pygame
import time


def info():
    text = pygame.font.Font(None, 24)

    x = (pygame.mouse.get_pos()[0] + parameters.move_x) // parameters.block_size
    y = (pygame.mouse.get_pos()[1] + parameters.move_y) // parameters.block_size


    coords = text.render(f'coords: {x}, {y}', True, (255, 0, 0))

    chunk = text.render(f'chunk: {x // 16}, {y // 16}', True, (255, 0, 255))

    chunk_rel = text.render(f'chunk_rel: {x % 16}, {y % 16}', True, (255, 0, 255))

    targeted_block = text.render(f'targeted_block: {world.block(x, y)}', True, (0, 255, 0))

    seed = text.render(f'seed: {parameters.seed}', True, (0, 255, 255))

    fps = text.render(f'FPS: {int(1 / (time.time() - parameters.frame_start_time))}', True, (255, 160, 0))

    parameters.screen.blit(coords, (0, 0))
    parameters.screen.blit(chunk, (0, 24))
    parameters.screen.blit(chunk_rel, (0, 48))
    parameters.screen.blit(targeted_block, (0, 72))
    parameters.screen.blit(seed, (0, 96))
    parameters.screen.blit(fps, (0, 120))
