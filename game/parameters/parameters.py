import pygame
import noise
from random import randint
import time

# World settings
noise = noise
free_fall_time = 0
free_fall_speed = 0.2

seed = randint(-(2 ** 16), 2 ** 16)
# seed = 0
limit_height = 512
noise_frequnce = 1024
noise_octaves = 5
shift_amplitude = 25
shift_frequence = 250
shift_octaves = 5

# File system settings
current_save = f'seed_{seed}'

# Display settings
size = width, height = 1920, 1080  # Window size
zoom = 1  # Zoom in/out
scroll = 6 * zoom
texture_size = 7  # px
character_size = character_width, character_height = 21, 40  # px
block_size = int(texture_size * 3 // zoom)
blocks_x = width // block_size
blocks_y = height // block_size
display_mode = 'worldmap'  # worldmap
debug = True
bg = 64, 0, 48

# Start screen position
x = 0
y = 0
# move_x = -150 * block_size  # 0
# move_y = 412 * block_size  # limit_height // 2
move_x = -28 * block_size  # 0
move_y = 472 * block_size  # limit_height // 2
# move_x = 0  # 0
# move_y = 0  # limit_height // 2
loaded_chunks = {}

# Window settings
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sandbox')
pygame.display.set_icon(pygame.image.load('images/icon.png'))
frame_start_time = time.time()

# Default values
block_id = 'unset'
