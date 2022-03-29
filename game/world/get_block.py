from game.parameters import parameters
from game.noises import get_noise


def is_air(x, y):  # Stone setup
    if y / parameters.limit_height >= get_noise.get('shifty', x, y) + 1:
        return False
    else:
        return True


def is_water(y):
    if y / parameters.limit_height - 1 <= 0.1:  # TODO: Оптимизоровать
        return False
    else:
        return True


def get(x, y):
    if is_air(x, y):
        block_id = 'air'
        if is_water(y):
            block_id = 'water'
    else:
        block_id = 'stone'
        if 0.25 <= get_noise.get('simplex', x, y, octaves=5, freq=64):
            block_id = 'granite'
        if 0.25 <= get_noise.get('simplex', x, y, octaves=5, freq=64, seed_shift=1):
            block_id = 'basalt'
        if 0.45 <= get_noise.get('simplex', x, y, octaves=5, freq=64, seed_shift=2):
            block_id = 'marble'
        if is_air(x, y - 10):
            block_id = 'dirt'
            if is_air(x, y - 1) and not is_water(y - 1):  # If above is air (water not depends on x)
                block_id = 'grass'
            if y >= get_noise.get('shifty', x, y, octaves=1, freq=10, amplitude=10,
                                  shift_amplitude=0, seed_shift=-1) * 5 + 560:
                block_id = 'sand'
    return block_id
