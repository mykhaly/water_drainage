from utils import *
from image_helper import *
from matrix_helper import *
import const


def main():
    filepath = os.path.join(const.DIRECTORY_NAME, "input.txt")
    init_matrix_to_file(filepath, const.MATRIX_SIZE)
    matrix = read_matrix(filepath)
    make_image(matrix, era="0", iteration=8000)
    for era in range(1, 10):
        make_rain(matrix, 5)
        make_water_drainage(matrix, era)
        print_matrix(matrix)
        make_image(matrix, era=era, iteration=8000)
    print "Output: " + const.DIRECTORY_NAME


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print const.DIRECTORY_NAME
        raise

# vovk.v.d@gmail.com
