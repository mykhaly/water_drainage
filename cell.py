SIGNIFICANT_DIGITS = 8

def isclose(a, b, rel_tol, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Cell:
    def __init__(self, x, y, terrain, water):
        self.x = int(x)
        self.y = int(y)
        self._terrain = float(terrain)
        self._water = float(water)

    def __repr__(self):
        return "{}  {}  {:.8f}  {:.8f}  {:.8f}   ".format(
            self.x,
            self.y,
            self.terrain,
            self.water,
            self.height)
        # return "{} {}   ".format(self.terrain, self.water)

    @property
    def height(self):
        return round(self.terrain + self.water, SIGNIFICANT_DIGITS)

    @property
    def terrain(self):
        return round(self._terrain, SIGNIFICANT_DIGITS)

    @property
    def water(self):
        return round(self._water, SIGNIFICANT_DIGITS)

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
        min_height = min(heights)
        minimal_neighbours = []
        precision = pow(10, -SIGNIFICANT_DIGITS)
        if isclose(min_height, self.height, precision):
            return minimal_neighbours
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
            max_input = round((self.height - min_neighb[0].height) / (len(min_neighb) + 1),
                              SIGNIFICANT_DIGITS)
        for minimal_neighbour in min_neighb:
            shared_neighbours = set(minimal_neighbour.get_neighbours(matrix)).intersection(
                set(neighbours))
            for shared_neighbour in shared_neighbours:
                diff = round(shared_neighbour.height - minimal_neighbour.height, SIGNIFICANT_DIGITS)
                max_input = diff if (diff != 0 and diff < max_input) else max_input
        # return max_input if max_input >= 1.0 / (pow(10, PRECISION)) else 0
        return round(max_input, SIGNIFICANT_DIGITS)

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
