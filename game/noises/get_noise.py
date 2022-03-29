from game.noises.noise_functions import shifty
from game.noises.noise_functions import simplex
from game.noises.noise_functions import rigged
from game.parameters import parameters


def get(noise_type, x, y, octaves=parameters.noise_octaves, freq=parameters.noise_frequnce,
        amplitude=parameters.limit_height, shift_octaves=parameters.shift_octaves,
        shift_freq=parameters.shift_frequence, shift_amplitude=parameters.shift_amplitude, seed_shift=0):
    if noise_type == 'simplex':
        return simplex.get(x, y, octaves=octaves, freq=freq,  seed_shift=seed_shift)
    if noise_type == 'shifty':
        return shifty.get(x, y, octaves=octaves, freq=freq, amplitude=amplitude, shift_octaves=shift_octaves,
                          shift_freq=shift_freq, shift_amplitude=shift_amplitude, seed_shift=seed_shift)
    if noise_type == 'rigged':
        return rigged.get(x, y, octaves=octaves, freq=freq, seed_shift=seed_shift)
