from cell import Cell


def read_data_from_file(filepath):
    matrix = []
    with open(filepath, "r") as filee:
        for index, raw in enumerate(filee.readlines()):
            matrix.append([])
            entries = raw.split("\t  ")
            for entry in entries:
                # temp = entry.split(' ')
                # x, y, params = temp[0], temp[1], temp[2]
                # terrain, water, height = params.split('\t')
                # cell = Cell(x, y, terrain, water)
                temp = entry.split()
                cell = Cell(*entry.split())
                matrix[index].append(cell)
    return matrix


def print_matrix(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            print matrix[i][j],
        print ""
