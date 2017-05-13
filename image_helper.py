from PIL import Image

import numpy as np
import os
import const


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


def make_image(matrix, era=0, iteration=8000):
    size_of_matrix = len(matrix[0])
    pixels_per_square = const.IMAGE_LEN / size_of_matrix
    data = np.zeros((const.IMAGE_LEN, const.IMAGE_LEN, 3), dtype=np.uint8)
    for i in xrange(size_of_matrix):
        for j in xrange(size_of_matrix):
            water_level = matrix[i][j].water
            if water_level > const.WATER_TOLERANCE:
                colour = get_water_shade(water_level)
            else:
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
