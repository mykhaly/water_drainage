def make_rain(matrix, water_amount):
    size = len(matrix[0])
    for i in range(size):
        for j in range(size):
            matrix[i][j].water += water_amount
    return matrix


def make_water_drainage(matrix, era):
    smt_changed = True
    iterations_count = 0
    while smt_changed:
        smt_changed = False
        iterations_count += 1
        print "Calculating {era} era, iteration: {iteration}...".format(
            era=era, iteration=iterations_count)
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                water_drained = cell.drain_water(matrix)
                smt_changed = smt_changed or water_drained
