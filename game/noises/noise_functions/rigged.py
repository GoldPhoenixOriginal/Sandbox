from game.parameters import parameters
from pynoise.noisemodule import RidgedMulti


def get(x, y, octaves=parameters.noise_octaves, freq=parameters.noise_frequnce, seed_shift=0):
    noise = RidgedMulti(
        octaves=octaves
    ).get_value(
        x / freq,
        y / freq,
        0,
    )
    return noise
