from cell import Cell

def read_data_from_file(filepath):
    matrix = []
    with open(filepath, "r") as filee:
        for index, raw in enumerate(filee.readlines()):
            matrix.append([])
            entries = raw.split("    ")
            for entry in entries:
                cell = Cell(*(entry.split("  ")))
                matrix[index].append(cell)
    return matrix

def print_matrix(matr):
    for i in xrange(len(matr)):
        for j in xrange(len(matr[i])):
            print matr[i][j],
        print ""

lol = read_data_from_file("/home/mykhalch/uni/input.txt")
print_matrix(lol)