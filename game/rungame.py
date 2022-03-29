import pygame

from game.parameters import keys, parameters
from game.draw import drawworld
from game.draw.view_functions import worldmap
from game.world import tick
import time


def prepare():  # Pre-build spawn chunks
    if not parameters.display_mode == 'worldmap': return
    step = 16 * parameters.block_size
    for parameters.move_y in range(-10 * step, 10 * step, step):
        for parameters.move_x in range(-10 * step, 10 * step, step):
            worldmap.draw()


def run():
    rungame = 1
    while rungame:
        parameters.frame_start_time = time.time()
        # Events
        keys.start_functions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for end of session
                rungame = keys.shutdown()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse buttons down
                if event.button == 1: keys.lmb_pushed = True  # Check for pushing left mouse button
            elif event.type == pygame.MOUSEBUTTONUP:  # Mouse buttons up
                if event.button == 1: keys.lmb_pushed = False  # Check for releasing left mouse button
            elif event.type == pygame.KEYDOWN:  # Keys down
                if event.key == pygame.K_p: keys.take_snapshot()  # Check for pressing 'P' key
                if event.key == pygame.K_ESCAPE: rungame = keys.shutdown()  # Check for pressing 'ESC' key
                if event.key == pygame.K_q: keys.place_block('stone')  # Check for pressing 'Q' key
                if event.key == pygame.K_e: keys.place_block('air')  # Check for pressing 'E' key
                if event.key == pygame.K_r: keys.place_block('unset')  # Check for pressing 'R' key
                if event.key == pygame.K_g: tick.debug()  # Check for pressing 'R' key
            keys.key_functions()
        # Game
        # tick.tick()
        # Render
        drawworld.draw()
        pygame.display.flip()
        pygame.time.wait(8)  # Limit 120 FPS
