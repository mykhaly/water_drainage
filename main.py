from utils import *
from image_helper import *
from matrix_helper import *


def main():
    matrix = read_matrix("input3.txt")
    # matrix = random_matrix(10, 15, 150)
    make_image(matrix, era="0", iteration=8000)
    for era in range(1, 7):
        make_rain(matrix)
        make_water_drainage(matrix, era)
        print_matrix(matrix)
        make_image(matrix, era=era, iteration=8000)
    print "Output: " + const.DIRECTORY_NAME


if __name__ == "__main__":
    main()

# vovk.v.d@gmail.com
