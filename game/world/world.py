import os
import json

from game.parameters import parameters
from game.world import get_block


def block(x, y):
    path = f'game/saves/{parameters.current_save}/chunk[{x // 16}, {y // 16}].json'
    if os.path.exists(path):  # If chunk saved
        with open(path, 'r') as f:  # Open save
            file = json.loads(f.read())
            if f'Block [{x % 16}, {y % 16}]' in file:  # If block save exists
                block_id = file[f'Block [{x % 16}, {y % 16}]']['id']  # Load
            else:  # If not
                block_id = get_block.get(x, y)  # Generate block
    else:  # If not
        block_id = get_block.get(x, y)  # Generate block
    return block_id
