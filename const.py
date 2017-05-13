import random
import os


SIGNIFICANT_DIGITS = 2  # precision of all calculations
WATER_PER_LEVEL = 12
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

DIRECTORY_NAME = os.path.join("images/", "FIX{}".format(random.randint(1000, 10000)))
if not os.path.exists(DIRECTORY_NAME):
    os.makedirs(DIRECTORY_NAME)
print "Output: " + DIRECTORY_NAME

#
# def get_color_bands(color, bands):
#     color_bands = []
#     red, green, blue = color
#     step = 1.0 / bands
#     fraction = 0
#     for band in range(bands):
#         new_red = max(0, red - fraction * 255)
#         new_green = max(0, green - fraction * 255)
#         new_blue = max(0, blue - fraction * 255)
#         color_bands.append((new_red, new_green, new_blue))
#         fraction += step
#     return color_bands
#
# l = get_color_bands((0, 200, 100), 100)
# print l