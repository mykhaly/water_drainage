from random import randint
from utils import *
MATRIX = []
MATRIX_SIZE = 10
# for i in range(MATRIX_SIZE):
#     MATRIX.append([])
#     for j in range(MATRIX_SIZE):
#         terrain = randint(0, 10)
#         water = randint(0, 10)
#         MATRIX[i].append(Cell(i, j, terrain, water))

# there is bug in config contained in file
MATRIX = read_data_from_file("input.txt")

matrix = MATRIX




def main():
    print_matrix(MATRIX)
    smth_changed = True
    iterations_count = 0
    while smth_changed:
        smth_changed = False
        iterations_count += 1
        print "Still calculating, iteration: ", iterations_count
        for row in MATRIX:
            for cell in row:
                water_drained = cell.drain_water(MATRIX)
                smth_changed = smth_changed or water_drained
    print_matrix(MATRIX)
if __name__ == "__main__":
    main()