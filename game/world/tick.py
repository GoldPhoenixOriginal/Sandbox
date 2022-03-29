from game.parameters import parameters
from game.world import character
from game.world import world


def tick():
    parameters.move_y += int(parameters.free_fall_time ** 2 * 1)
    parameters.free_fall_time += parameters.free_fall_speed

    left_side = (parameters.width - character.width) // 2 - 1 * parameters.block_size
    right_side = (parameters.width - character.width) // 2 + character.width
    upper_side = (parameters.height - character.height) // 2 - 1 * parameters.block_size
    lower_side = (parameters.height - character.height) // 2 + character.height

    for y in range(upper_side, lower_side + 1):
        for x in range(left_side, right_side + 1):

            block_x = (x + parameters.move_x) // parameters.block_size + 1
            block_y = (y + parameters.move_y) // parameters.block_size + 1
            current_block = world.block(block_x, block_y)

            if current_block != 'air':
                parameters.free_fall_time = 0


def debug():
    left_side = (parameters.width - character.width) // 2 - 1 * parameters.block_size
    right_side = (parameters.width - character.width) // 2 + character.width
    upper_side = (parameters.height - character.height) // 2 - 1 * parameters.block_size
    lower_side = (parameters.height - character.height) // 2 + character.height
    for y in range(upper_side, lower_side, parameters.block_size):
        for x in range(left_side, right_side, parameters.block_size):

            block_x = (x + parameters.move_x) // parameters.block_size + 1
            block_y = (y + parameters.move_y) // parameters.block_size + 1
            current_block = world.block(block_x, block_y)
            print(f'{current_block} [{block_x}; {block_y}]', end=', ')
        print()
    print()
