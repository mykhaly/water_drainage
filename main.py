from utils import *
from image_helper import *
from matrix_helper import *
import const
import sys
from logger import Logger


def main():
    filepath = os.path.join(const.DIRECTORY_NAME, "input.txt")
    init_matrix_to_file(filepath, const.MATRIX_SIZE)
    matrix = read_matrix(filepath)
    # matrix = read_matrix("input2.txt")
    make_image(matrix, era=0)
    for era in range(1, 5):
        make_rain(matrix, const.AMOUNT_OF_RAIN)
        make_water_drainage(matrix, era)
        print_matrix(matrix)
        make_image(matrix, era=era)
        print "\n"


if __name__ == "__main__":
    import cProfile, pstats, StringIO

    pr = cProfile.Profile()
    pr.enable()

    # ... do something ...
    logpath = os.path.join(const.DIRECTORY_NAME, "logfile.log")
    sys.stdout = Logger(logpath)
    print "Output: " + const.DIRECTORY_NAME
    main()
    print "Output: " + const.DIRECTORY_NAME

    pr.disable()
    s = StringIO.StringIO()
    sortby = 'time'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()

# vovk.v.d@gmail.com
