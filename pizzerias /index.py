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
    def __init__(self, dim, location, capacity, debug=True):
        if (capacity < 1) | (capacity > 100):
            raise Exception('Range must be between 1 to 100')

        if (location[0] < 1) | (location[1] > dim):
            raise Exception('Location must be within {} x {}'.format(dim, dim))

        if (dim < 1) | (dim > 1000):
            raise Exception('Dimensions is not valid!')

        self.debug = debug
        self.dim = dim
        self.location = location
        self.capacity = capacity
        self.block = numpy.zeros((dim, dim))

    def build(self):
        x = self.location[0] - 1
        y = self.location[1] - 1

        for i in range(self.capacity + 1):
            if (x + i) < dim:
                self.block[x + i][y] = 1
            if (x - i) >= 0:
                self.block[x - i][y] = 1
            if (y + i) < dim:
                self.block[x][y + i] = 1
            if (y - i) >= 0:
                self.block[x][y - i] = 1

        for i in range(1, self.capacity):
            if (x + i < dim) & (y + i < dim):
                self.block[x + i][y + i] = 1
            if (x - i >= 0) & (y - i >= 0):
                self.block[x - i][y - i] = 1
            if (x + i < dim) & (y - i >= 0):
                self.block[x + i][y - i] = 1
            if (x - i >= 0) & (y + i < dim):
                self.block[x - i][y + i] = 1

        self.block = numpy.flipud(self.block)

        if self.debug:
            print(self.block)

        return self.block


if __name__ == '__main__':
    file_name = 'input.txt'

    dim, num_pizzerias, pizzerias = load(file_name)

    sum_range = numpy.zeros((dim, dim))
    for pizzeria in pizzerias:
        block = Block(dim, pizzeria[0:-1], pizzeria[-1], debug=False)
        pizza_range = block.build()
        sum_range += pizza_range

    print(int(numpy.max(sum_range)))
