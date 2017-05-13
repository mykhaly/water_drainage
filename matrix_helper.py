from random import randint
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
    def make_ellipsoid(matrix, width, length):
        width, length = float(width), float(length)
        rows, cols = matrix.shape
        for i in range(rows):
            center_x = i - (rows / 2)
            for j in range(cols):
                center_y = j - (cols / 2)
                if abs((center_x / length) ** 2) + abs((center_y / width) ** 2) >= 1:
                    matrix[i, j] += (abs(center_x) + abs(center_y)) * 10
        return matrix

    data = np.matrix(np.zeros((size, size), int))
    make_ellipsoid(data, 4, 3)
    with open(filepath, "w") as f:
        for i in range(size):
            row = ""
            for j in range(size):
                row += str(data[i, j]) + " "
            row += "\n"
            f.write(row)