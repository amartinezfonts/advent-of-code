#!/usr/bin/env python3
import re

# setup tasks
print("Here's a summary of the password compliance (v2):")
valid = 0
invalid = 0

#define the regex
line_regex = re.compile('(\d*)-(\d*)\s(\w):\s(\w*)')

# open the input file and convert to an array
with open ('input.txt', 'r') as pwdFile:
    pwdArray = [line for line in pwdFile.readlines()]

# iterate over each line in the password list
for line in pwdArray:
    # parse each line into needed variables
    pos1, pos2, target_letter, password = line_regex.findall(line)[0]
    pos1 = int(pos1)
    pos2 = int(pos2)
    pos1_match = False
    pos2_match = False

    # test for matches
    if password[pos1-1] == target_letter: pos1_match = True
    if password[pos2-1] == target_letter: pos2_match = True

    # check with XOR
    if pos1_match ^ pos2_match:
        valid += 1
    else:
        invalid += 1

print("Valid: " + str(valid))
print("Invalid: " + str(invalid))
