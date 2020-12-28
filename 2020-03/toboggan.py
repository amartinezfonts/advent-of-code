#!/usr/bin/env python3

# open the input file and convert to an array
with open ('input.txt', 'r') as tree_file:
    tree_array = [line for line in tree_file.readlines()]

# set some constants
line_length = 31
move_right = 3
move_down = 1

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
    current_row = current_row + move_down
    current_column = current_column + move_right

    # if you hit the edge of the map (end of the line), wrap around to the beginning
    if current_column >= line_length:
        current_column = current_column - line_length

print("You hit this many trees: " + str(trees_hit))
