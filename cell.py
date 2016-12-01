PRECISION = 3


class Cell:
    def __init__(self, x, y, terrain, water):
        self.x = int(x)
        self.y = int(y)
        self._terrain = float(terrain)
        self._water = float(water)

    def __repr__(self):
        return "{}  {}  {}  {}   ".format(
            self.x,
            self.y,
            self.terrain,
            self.water)
        # return "{} {}   ".format(self.terrain, self.water)

    @property
    def height(self):
        return round(self.terrain + self.water, PRECISION)

    @property
    def terrain(self):
        return round(self._terrain, PRECISION)

    @property
    def water(self):
        return round(self._water, PRECISION)

    @water.setter
    def water(self, value):
        self._water = value

    def get_neighbours(self, matrix):
        last = len(matrix) - 1
        neighbours = []
        col = self.y
        row = self.x
        if row != 0:
            neighbours.append(matrix[row - 1][col])
        if row != 0 and col != last:
            neighbours.append(matrix[row - 1][col + 1])
        if col != last:
            neighbours.append(matrix[row][col + 1])
        if row != last and col != last:
            neighbours.append(matrix[row + 1][col + 1])
        if row != last:
            neighbours.append(matrix[row + 1][col])
        if row != last and col != 0:
            neighbours.append(matrix[row + 1][col - 1])
        if col != 0:
            neighbours.append(matrix[row][col - 1])
        if row != 0 and col != 0:
            neighbours.append(matrix[row - 1][col - 1])
        return neighbours

    def get_minimal_neighbours(self, matrix):
        neighbours = self.get_neighbours(matrix)
        heights = [neighbour.height for neighbour in neighbours]
        min_height = min(heights + [self.height])
        minimal_neighbours = []
        #
        if min_height == self.height:
            return minimal_neighbours
        #
        for index, height in enumerate(heights):
            if height == min_height:
                minimal_neighbours.append(neighbours[index])
        return minimal_neighbours

    def possible_input(self, matrix, min_neighb):
        neighbours = self.get_neighbours(matrix)
        max_input = float('inf')
        if self.terrain > min_neighb[0].height + self.water / (len(min_neighb) + 1):
            # all water could be drained
            pass
        else:
            # some water will not be drained
            # error for second iteration for first cell
            # self.water == 5.5 and min_neighb[0].height == 5.5
            max_input = round((self.water - min_neighb[0].height) / (len(min_neighb) + 1),
                              PRECISION)
        for minimal_neighbour in min_neighb:
            shared_neighbours = set(minimal_neighbour.get_neighbours(matrix)).intersection(
                set(neighbours))
            for shared_neighbour in shared_neighbours:
                diff = round(shared_neighbour.height - minimal_neighbour.height, PRECISION)
                max_input = diff if (diff != 0 and diff < max_input) else max_input
        # return max_input if max_input >= 1.0 / (pow(10, PRECISION)) else 0
        return round(max_input, PRECISION)

    def drain_water(self, matrix):
        smth_drained = False
        while True:
            minimal_neighbours = self.get_minimal_neighbours(matrix)
            if not minimal_neighbours:
                return smth_drained
            water_could_be_drained = self.possible_input(matrix, minimal_neighbours)
            if water_could_be_drained * len(minimal_neighbours) > self.water:
                water_could_be_drained = self.water / len(minimal_neighbours)
            if water_could_be_drained not in (float('inf'), 0):
                for minimal_neighbour in minimal_neighbours:
                    minimal_neighbour.water += water_could_be_drained
                    self.water -= water_could_be_drained
                smth_drained = True
            else:
                return smth_drained
