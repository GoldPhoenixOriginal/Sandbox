from game.draw.view_functions import worldmap
from game.draw.view_functions.debug import info, hitboxes, grid
from game.parameters import parameters
from game.world import character


def draw():
    parameters.screen.fill(parameters.bg)
    if parameters.display_mode == 'worldmap': worldmap.draw()
    if parameters.debug:
        # hitboxes.block_hitboxes()
        # grid.block_grid()
        # grid.chunk_grid()
        # hitboxes.character_hitbox()
        info.info()
    # character.draw()
