#!/usr/bin/env python3

def sled(tree_array, move_right, move_down):
    # count trees
    trees_hit = 0

    # iterate over each line in the tree_array
    for index, line in enumerate(tree_array):
        # set starting column and row
        if index == 0:
            current_row = 0
            current_column = 0

        # count if you hit a tree
        if line[current_column] == "#": trees_hit += 1

        # keep on sleddin'
        current_column = current_column + move_right
        current_row = current_row + move_down

        # if you hit the edge of the map (end of the line), wrap around to the beginning
        if current_column >= line_length:
            current_column = current_column - line_length

    return trees_hit


# open the input file and convert to an array
with open ('input.txt', 'r') as tree_file:
    tree_array = [line for line in tree_file.readlines()]

# strip the newline chars
for i, val in enumerate(tree_array):
    tree_array[i] = tree_array[i].strip()

# figure out how long each line is (assume they're all the same)
line_length = len(tree_array[0])


sled1 = sled(tree_array, 1, 1)
print("1 right, 1 down = " + str(sled1) + " hit trees")

sled2 = sled(tree_array, 3, 1)
print("3 right, 1 down = " + str(sled2) + " hit trees")

sled3 = sled(tree_array, 5, 1)
print("5 right, 1 down = " + str(sled3) + " hit trees")

sled4 = sled(tree_array, 7, 1)
print("7 right, 1 down = " + str(sled4) + " hit trees")

sled5 = sled(tree_array, 1, 2)
print("1 right, 2 down = " + str(sled5) + " hit trees")

tree_product = sled1 * sled2 * sled3 * sled4 * sled5
print("Product of all 5 sledding trips: " + str(tree_product))
