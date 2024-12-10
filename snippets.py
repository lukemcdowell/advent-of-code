from itertools import product


# reading in a file line by line
def get_data(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


# creating grid from a file
grid = [list(line) for line in get_data()]

# generate a list of all possible orders
combos = list(product("abc", repeat=4))
