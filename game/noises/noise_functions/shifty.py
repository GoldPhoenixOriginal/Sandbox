from game.parameters import parameters


def get(x, y, octaves=parameters.noise_octaves, freq=parameters.noise_frequnce, amplitude=parameters.limit_height,
        shift_octaves=parameters.shift_octaves, shift_freq=parameters.shift_frequence,
        shift_amplitude=parameters.shift_amplitude, seed_shift=0):
    noise = parameters.noise.snoise2(
        (x + (parameters.noise.snoise2(
            0,
            (y * 2) / shift_freq,
            octaves=shift_octaves,
            repeatx=amplitude,
            repeaty=amplitude,
            base=(parameters.seed + seed_shift))
        ) * shift_amplitude) / freq,
        0,
        octaves=octaves,
        repeatx=amplitude,
        repeaty=amplitude,
        base=(parameters.seed + seed_shift))
    return noise
