from game.parameters import parameters


def get(x, y, octaves=parameters.noise_octaves, freq=parameters.noise_frequnce, seed_shift=0):
    noise = parameters.noise.snoise2(
        x / freq,
        y / freq,
        octaves=octaves,
        repeatx=parameters.limit_height,
        repeaty=parameters.limit_height,
        base=(parameters.seed + seed_shift))
    return noise
