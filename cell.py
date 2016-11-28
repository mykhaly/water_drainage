PRECISION = 3

class Cell:
    def __init__(self, x, y, terrain, water):
        self.x = x
        self.y = y
        self._terrain = terrain
        self._water = water

    def __repr__(self):
        return "\n{}\t{}\t{}\t{}".format(
            self.x,
            self.y,
            self.terrain,
            self.water)

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
        y = self.y
        x = self.x
        if y != 0:
            neighbours.append(matrix[y - 1][x])
        if y != 0 and x != last:
            neighbours.append(matrix[y - 1][x + 1])
        if x != last:
            neighbours.append(matrix[y][x + 1])
        if y != last and x != last:
            neighbours.append(matrix[y + 1][x + 1])
        if y != last:
            neighbours.append(matrix[y + 1][x])
        if y != last and x != 0:
            neighbours.append(matrix[y + 1][x - 1])
        if x != 0:
            neighbours.append(matrix[y][x - 1])
        if y != 0 and x != 0:
            neighbours.append(matrix[y - 1][x - 1])
        return neighbours

    def get_minimal_neighbours(self, matrix):
        neighbours = self.get_neighbours(matrix)
        heights = [neighbour.height for neighbour in neighbours]
        min_height = min(heights + [self.height])
        minimal_neighbours = []
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
            max_input = (self.water - min_neighb[0].height) / (len(min_neighb) + 1)
        for minimal_neighbour in min_neighb:
            shared_neighbours = set(minimal_neighbour.get_neighbours(matrix)).intersection(
                set(neighbours))
            for shared_neighbour in shared_neighbours:
                diff = shared_neighbour.height - minimal_neighbour.height
                max_input = diff if (diff != 0 and diff < max_input) else max_input
        return max_input if max_input >= 1.0 / (pow(10, PRECISION)) else 0

    def drain_water(self, matrix):
        sth_changed = True
        while sth_changed:
            minimal_neighbours = self.get_minimal_neighbours(matrix)
            if not minimal_neighbours:
                return
            water_could_be_drained = self.possible_input(matrix, minimal_neighbours)
            for minimal_neighbour in minimal_neighbours:
                minimal_neighbour.water += water_could_be_drained
                self.water -= water_could_be_drained
            sth_changed = water_could_be_drained not in (float('inf'), 0)
