import os
from datetime import datetime


MATRIX_SIZE = 25
SIGNIFICANT_DIGITS = 2  # precision of all calculations
PRECISION = 0.01  # when two cells heights are considered equal
WATER_TOLERANCE = PRECISION * MATRIX_SIZE * 2
WATER_PER_LEVEL = 12
AMOUNT_OF_RAIN = 5
WATER_SHADES = [
    (176, 224, 230),
    (135, 206, 250),
    (135, 206, 235),
    (0, 191, 255),
    (30, 144, 255),
    (70, 130, 180),
    (65, 105, 225),
    (0, 0, 255),
    (0, 0, 205),
    (0, 0, 128)]
TERRAIN_PER_LEVEL = 21
DEFAULT_TERRAIN_LEVEL = 100
TERRAIN_SHADES = [
    (255, 248, 220),
    (255, 228, 196),
    (255, 222, 173),
    (222, 184, 135),
    (210, 180, 140),
    (244, 164, 96),
    (218, 165, 32),
    (205, 133, 63),
    (160, 82,  45),
    (139, 69,  19)]
IMAGE_LEN = 1000  # size of image in pixels
WATER_COLOR = (0, 0, 255)

DIRECTORY_NAME = os.path.join("images", str(datetime.now()))
if not os.path.exists(DIRECTORY_NAME):
    os.makedirs(DIRECTORY_NAME)

