import const
import numpy as np


def isclose(a, b, rel_tol, abs_tol=const.PRECISION):
    # return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return abs(a - b) <= abs_tol


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
        precision = pow(10, - (const.SIGNIFICANT_DIGITS + 1))
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
            max_input = (self.height - min_neighb[0].height) / (len(min_neighb) + 1)
        for minimal_neighbour in min_neighb:
            shared_neighbours = set(minimal_neighbour.get_neighbours(matrix)).intersection(
                set(neighbours))
            for shared_neighbour in shared_neighbours:
                diff = shared_neighbour.height - minimal_neighbour.height

                max_input = diff if (diff != 0 and diff < max_input) else max_input
        return max_input

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
