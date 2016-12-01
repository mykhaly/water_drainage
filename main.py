from random import randint
from utils import *
FIRST_ROW = [Cell(0, 0, 0, 1), Cell(0, 1, 0, 2), Cell(0, 2, 0, 1.5)]
SECOND_ROW = [Cell(1, 0, 2, 0), Cell(1, 1, 2, 0.9), Cell(1, 2, 2, 0)]
THIRD_ROW = [Cell(2, 0, 2, 0), Cell(2, 1, 2, 0), Cell(2, 2, 0, 1)]

# There is bug in this config
# 0  0  1.0  8.0    0  1  9.0  2.0    0  2  1.0  9.0
# 1  0  3.0  0.0    1  1  7.0  0.0    1  2  2.0  1.0
# 2  0  2.0  1.0    2  1  9.0  6.0    2  2  7.0  7.0

MATRIX2 = [FIRST_ROW, SECOND_ROW, THIRD_ROW]
# MATRIX = []
# for i in range(3):
#     MATRIX.append([])
#     for j in range(3):
#         terrain = randint(0, 10)
#         water = randint(0, 10)
#         MATRIX[i].append(Cell(i, j, terrain, water))

MATRIX = read_data_from_file("/home/mykhalch/uni/input.txt")

matrix = MATRIX




def main():
    print_matrix(MATRIX)
    print "\n\n\n"
    smth_changed = True
    iterations_count = 0
    while smth_changed:
        smth_changed = False
        iterations_count += 1
        print "ITERATION: ", iterations_count
        for row in MATRIX:
            for cell in row:
                print "WORKING WITH CELL: ", cell.x, cell.y
                water_drained = cell.drain_water(MATRIX)
                if water_drained:
                    print "WATER DRAINED FROM CELL: ", cell.x, cell.y
                    print_matrix(MATRIX)
                smth_changed = smth_changed or water_drained

    print_matrix(MATRIX)
if __name__ == "__main__":
    main()