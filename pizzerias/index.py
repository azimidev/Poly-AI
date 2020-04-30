import numpy


def load(file_name):
    lines = open(file_name).read().split('\n')

    first_line = lines[0].split()

    grid_size = int(first_line[0])

    num_inputs = int(first_line[1])

    information = []
    for i in range(1, num_inputs + 1):
        line = [int(l) for l in lines[i].split()]
        information.append(line)

    return grid_size, num_inputs, information


class Block:
    def __init__(self, dimension, location, capacity, debug=True):
        if (capacity < 1) | (capacity > 100):
            raise Exception('Range must be between 1 to 100')

        if (location[0] < 1) | (location[1] > dimension):
            raise Exception(f"Location must be within {dimension} x {dimension}.")

        if (dimension < 1) | (dimension > 1000):
            raise Exception('Dimensions is not valid!')

        self.debug = debug
        self.dimension = dimension
        self.location = location
        self.capacity = capacity
        self.block = numpy.zeros((dimension, dimension))

    def build(self):
        x = self.location[0] - 1
        y = self.location[1] - 1

        for i in range(self.capacity + 1):
            if (x + i) < dimension:
                self.block[x + i][y] = 1
            if (x - i) >= 0:
                self.block[x - i][y] = 1
            if (y + i) < dimension:
                self.block[x][y + i] = 1
            if (y - i) >= 0:
                self.block[x][y - i] = 1

        for i in range(1, self.capacity):
            if (x + i < dimension) & (y + i < dimension):
                self.block[x + i][y + i] = 1
            if (x - i >= 0) & (y - i >= 0):
                self.block[x - i][y - i] = 1
            if (x + i < dimension) & (y - i >= 0):
                self.block[x + i][y - i] = 1
            if (x - i >= 0) & (y + i < dimension):
                self.block[x - i][y + i] = 1

        self.block = numpy.flipud(self.block)

        if self.debug:
            print(self.block)

        return self.block


if __name__ == '__main__':
    file_name = 'input.txt'

    dimension, num_pizzerias, pizzerias = load(file_name)

    sum_range = numpy.zeros((dimension, dimension))
    for pizzeria in pizzerias:
        block = Block(dimension, pizzeria[0:-1], pizzeria[-1], debug=False)
        pizza_range = block.build()
        sum_range += pizza_range

    print(int(numpy.max(sum_range)))
