from random import randint

import const
from cell import Cell
import numpy as np


def read_matrix(filepath):
    with open(filepath, "r") as filee:
        content = filee.readlines()
        water = 0
        matrix = []

        for i, raw in enumerate(content):
            matrix.append([])
            entries = raw.split()
            for j, terrain in enumerate(entries):
                matrix[i].append(Cell(i, j, terrain, water))
    return matrix


def random_matrix(size, min_height=0, max_height=100):
    matrix = []
    water = 0
    for i in range(size):
        matrix.append([])
        for j in range(size):
            terrain = randint(min_height, max_height)
            matrix[i].append(Cell(i, j, terrain, water))
    return matrix


def print_matrix(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            print matrix[i][j],
        print ""


def print_matrix_diff(matrix1, matrix2):
    size = len(matrix1[0])
    for i in xrange(size):
        for j in xrange(size):
            if matrix1[i][j] != matrix2[i][j]:
                print "first: {}, {}: {}\t".format(i, j, matrix1[i][j]),
                print "second: {}, {}: {}".format(i, j, matrix2[i][j])
        print ""


def init_matrix_to_file(filepath, size):
    def make_ellipsoid(matrix, center_x, center_y, a, b, min_height):
        a, b = float(a), float(b)
        rows, cols = matrix.shape
        for i in range(rows):
            x = abs(i - center_x)
            for j in range(cols):
                y = abs(j - center_y)
                if (x / a) ** 2 + (y / b) ** 2 <= 1:
                    # matrix[i, j] *= min(((x / a) ** 2 + (y / b) ** 2) + min_height,
                    #                     const.DEFAULT_TERRAIN_LEVEL)
                    coefficient = (x / a) ** 2 + (y / b) ** 2
                    matrix[i, j] = min(coefficient * matrix[i, j] + min_height,
                                       const.DEFAULT_TERRAIN_LEVEL)
        return matrix

    matrix = np.matrix(np.ones((size, size), int) * const.DEFAULT_TERRAIN_LEVEL)
    matrix = make_ellipsoid(matrix=matrix,
                            center_x=20,
                            center_y=36,
                            a=25,
                            b=40,
                            min_height=20)

    matrix = make_ellipsoid(matrix=matrix,
                            center_x=50,
                            center_y=36,
                            a=25,
                            b=30,
                            min_height=5)

    # save height matrix to file
    with open(filepath, "w") as f:
        for i in range(size):
            row = ""
            for j in range(size):
                row += str(matrix[i, j]) + " "
            row += "\n"
            f.write(row)