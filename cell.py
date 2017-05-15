import const


class Cell:
    def __init__(self, x, y, terrain, water):
        self.x = int(x)
        self.y = int(y)
        self._terrain = float(terrain)
        self._water = float(water)

    def __repr__(self):
        return "{terrain:.{precision}f}\t{water:.{precision}f}\t{height:.{precision}f}\t\t".format(
            terrain=self.terrain, water=self.water, height=self.height,
            precision=const.SIGNIFICANT_DIGITS)

    @property
    def height(self):
        return self.terrain + self.water

    @property
    def terrain(self):
        return self._terrain

    @property
    def water(self):
        return self._water

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
            if col != last:
                neighbours.append(matrix[row - 1][col + 1])
        if col != last:
            neighbours.append(matrix[row][col + 1])
            if row != last:
                neighbours.append(matrix[row + 1][col + 1])
        if row != last:
            neighbours.append(matrix[row + 1][col])
            if col != 0:
                neighbours.append(matrix[row + 1][col - 1])
        if col != 0:
            neighbours.append(matrix[row][col - 1])
            if row != 0:
                neighbours.append(matrix[row - 1][col - 1])
        return neighbours

    def get_minimal_neighbours(self, matrix, neighbours):
        heights = {neighbour.height for neighbour in neighbours}
        heights.add(self.height)
        min_height = min(heights)
        minimal_neighbours = []
        if abs(min_height - self.height) <= const.PRECISION:
            return minimal_neighbours
        for neighbour in neighbours:
            if neighbour.height == min_height:
                minimal_neighbours.append(neighbour)
        return minimal_neighbours

    def possible_input(self, matrix, neighbours, min_neighb):
        max_input = float('inf')
        len_plus_one = len(min_neighb) + 1
        min_neighb_height = min_neighb[0].height
        if self.terrain < min_neighb_height + self.water / len_plus_one:
            max_input = (self.height - min_neighb_height) / len_plus_one

        neighbours = set(neighbours)
        for minimal_neighbour in min_neighb:
            shared_neighbours = set(minimal_neighbour.get_neighbours(matrix)).intersection(
                neighbours)
            for shared_neighbour in shared_neighbours:
                diff = shared_neighbour.height - minimal_neighbour.height
                max_input = diff if (diff != 0 and diff < max_input) else max_input
        return max_input

    def drain_water(self, matrix):
        drainage_occured = False
        while True:
            if self.water < const.WATER_TOLERANCE:
                break
            neighbours = self.get_neighbours(matrix)
            minimal_neighbours = self.get_minimal_neighbours(matrix, neighbours)
            if not minimal_neighbours:
                break
            water_could_be_drained = self.possible_input(matrix, neighbours, minimal_neighbours)
            if water_could_be_drained * len(minimal_neighbours) > self.water:
                water_could_be_drained = self.water / len(minimal_neighbours)
            drainage_occured = True
            for minimal_neighbour in minimal_neighbours:
                minimal_neighbour.water += water_could_be_drained
                self.water -= water_could_be_drained
        return drainage_occured
