import pygame
import time
import json
import os

from game.parameters import parameters

lmb_pushed = False


def shutdown():
    return 0


def take_snapshot():
    pygame.image.save(parameters.screen,
                      f'Snapshots/Snapshot_{time.strftime("%d.%m.%Y-%H.%M.%S", time.localtime())}.png')


def move_screen():
    if lmb_pushed:
        move_x, move_y = pygame.mouse.get_rel()
        parameters.move_x -= move_x
        parameters.move_y -= move_y


def key_functions():
    move_screen()


def start_functions():
    pygame.mouse.get_rel()  # reset value
    parameters.frame_start_time = time.time()


def place_block(block_id):
    x = (pygame.mouse.get_pos()[0] + parameters.move_x) // parameters.block_size
    y = (pygame.mouse.get_pos()[1] + parameters.move_y) // parameters.block_size
    save_path = f'game/saves/{parameters.current_save}'
    save_save = f'/chunk[{x // 16}, {y // 16}].json'
    json_block = \
        {
            f'Block [{x % 16}, {y % 16}]': {
                'id': block_id
            }
        }
    del parameters.loaded_chunks[(x // 16, y // 16)]
    if not os.path.exists(save_path):  # If save directory not exists
        os.mkdir(save_path)  # Create
    if not os.path.exists(save_path + save_save):  # If chunk file not exists
        with open(save_path + save_save, 'w') as f:  # Create
            json.dump(json_block, f, indent=4)  # And write down
    else:
        with open(save_path + save_save, 'r') as f:
            data = json.load(f)  # Load data
            data.update(json_block)  # Merge with new data
        with open(save_path + save_save, 'w') as f:
            json.dump(data, f, indent=4)  # And write down
