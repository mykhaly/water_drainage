from random import randint
from cell import Cell
from PIL import Image
import numpy as np


def read_data_from_file(filepath):
    matrix = []
    with open(filepath, "r") as filee:
        for index, raw in enumerate(filee.readlines()):
            matrix.append([])
            entries = raw.split("\t  ")
            for entry in entries:
                cell = Cell(*entry.split()[:-1])
                matrix[index].append(cell)
    return matrix


def read_data_without_indices(filepath):
    matrix = []
    with open(filepath, "r") as filee:
        content = filee.readlines()
        for i, raw in enumerate(content):
            matrix.append([])
            entries = raw.split("\t  ")
            for j, entry in enumerate(entries):
                # skip height if present
                data = entry.split()
                terrain = data[0]
                water = 1.0
                cell = Cell(i, j, terrain, water)
                matrix[i].append(cell)
    return matrix


def init_matrix(matrix_size):
    matrix = []
    for i in range(matrix_size):
        matrix.append([])
        for j in range(matrix_size):
            terrain = randint(0, 1000)
            water = randint(0, 100)
            matrix[i].append(Cell(i, j, terrain, water))
    return matrix


def print_matrix(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            print matrix[i][j],
        print ""


def get_water_ranges(matrix):
    max = 0.
    min = float('inf')
    for i in matrix:
        for el in i:
            if el.water > max:
                max = el.water
            if el.water < min and el.water != 0:
                min = el.water
    return min, max



def make_image(matrix):
    min_water, max_water = get_water_ranges(matrix)
    water_colours = [[0, 192, 192],
                     [32, 128, 192],
                     [32, 64, 192],
                     [62, 32, 128]]

    def get_water_shade(water_level):
        if water_level == 0:
            return [255, 255, 255]
        water_shade_idx = int(float(water_level - min_water) / (max_water - min_water)) * 3
        return water_colours[water_shade_idx]

    coefficient = 50
    size = len(matrix[0]) * coefficient
    data = np.zeros((size, size, 3), dtype=np.uint8)
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            colour = get_water_shade(matrix[i][j].water)
            for k in range(coefficient * i, coefficient * (i + 1)):
                for l in range(coefficient * j, coefficient * (j + 1)):
                    data[k][l] = colour

    img = Image.fromarray(data, 'RGB')
    img.save('my.png')
    return img
    # img.show()


def print_matrix_diff(matrix1, matrix2):
    for i, row in enumerate(matrix1):
        for j, element in enumerate(row):
            if element != matrix2[i][j]:
                print "first: {}, {}: {}\t".format(i, j, element),
                print "second: {}, {}: {}".format(i, j, matrix2[i][j])
        print ""


def make_water_drainage(matrix):
    smt_changed = True
    iterations_count = 0
    while smt_changed:
        smt_changed = False
        iterations_count += 1
        print "Calculating, iteration: {}...".format(iterations_count)
        for row in matrix:
            for cell in row:
                water_drained = cell.drain_water(matrix)
                smt_changed = smt_changed or water_drained
