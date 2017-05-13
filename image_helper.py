from PIL import Image


from colour import Color
import numpy as np
import os
import const


# def get_color_bands(color, bands, darken=True):
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
#     # color_bands = color_bands if darken else list(reversed(color_bands))
#     return color_bands
#
#
# terrain_colours = get_color_bands((153, 102, 0), const.TERRAIN_SHADES, darken=False)
# water_colours = get_color_bands((0, 0, 255), const.WATER_SHADES)


def get_water_shade(water_level):
    shade_idx = int(water_level) / const.WATER_PER_LEVEL \
        if water_level < const.WATER_PER_LEVEL * len(const.WATER_SHADES) \
        else len(const.WATER_SHADES) - 1
    return list(const.WATER_SHADES[shade_idx])


def get_terrain_shade(terrain_level):
    shade_idx = int(terrain_level) / const.TERRAIN_PER_LEVEL \
        if terrain_level < const.TERRAIN_PER_LEVEL * len(const.TERRAIN_SHADES) \
        else len(const.TERRAIN_SHADES) - 1
    return list(const.TERRAIN_SHADES[shade_idx])


def make_image(matrix, era=0, iteration=0):
    size_of_matrix = len(matrix[0])
    pixels_per_square = const.IMAGE_LEN / size_of_matrix
    data = np.zeros((const.IMAGE_LEN, const.IMAGE_LEN, 3), dtype=np.uint8)
    for i in xrange(size_of_matrix):
        for j in xrange(size_of_matrix):
            water_level = matrix[i][j].water
            if water_level > pow(10, -const.SIGNIFICANT_DIGITS):
                colour = get_water_shade(water_level)
            else:
                # colour = [255, 255, 255]
                colour = get_terrain_shade(matrix[i][j].height)
            for k in range(pixels_per_square * i, pixels_per_square * (i + 1)):
                for l in range(pixels_per_square * j, pixels_per_square * (j + 1)):
                    data[k, l] = colour

    img = Image.fromarray(data, 'RGB')
    iteration += 1000
    img_name = '{era:>5}.{iteration:>5}.png'.format(era=era, iteration=iteration)
    img_path = os.path.join(const.DIRECTORY_NAME, img_name)
    img.save(img_path)
    return img
