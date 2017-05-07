from utils import *
MATRIX_SIZE = 15

# there is bug in config contained in file
# matrix = read_data_without_indices("input3.txt")

matrix = init_matrix(MATRIX_SIZE)


def main():
    print_matrix(matrix)
    make_water_drainage(matrix)
    print_matrix(matrix)
    img = make_image(matrix)
    img.show()


if __name__ == "__main__":
    main()
