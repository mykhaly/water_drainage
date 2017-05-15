def make_rain(matrix, water_amount):
    size = len(matrix[0])
    for i in range(size):
        for j in range(size):
            matrix[i][j].water += water_amount
    return matrix


def make_water_drainage(matrix, era):
    smt_changed = True  # track whether water drainage occured for at least one cell in the @matrix
    iterations_count = 0  # number of iterations, used only for logging
    while smt_changed:
        smt_changed = False
        iterations_count += 1
        print "Calculating {} era, iteration: {}...".format(era, iterations_count)
        for row in matrix:
            for cell in row:
                water_drained = cell.drain_water(matrix)
                smt_changed = smt_changed or water_drained  # track whether drainage occured
