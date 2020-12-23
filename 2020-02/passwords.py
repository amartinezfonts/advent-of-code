#!/usr/bin/env python3
import re

# setup tasks
print("Here's a summary of the password compliance:")
valid = 0
invalid = 0

#define the regex
line_regex = re.compile('(\d*)-(\d*)\s(\w):\s(\w*)')

# open the input file and convert to an array
with open ('input.txt', 'r') as pwdFile:
    pwdArray = [line for line in pwdFile.readlines()]

# iterate over each line in the password list
for line in pwdArray:
    # find all matching groups for each line
    min_count, max_count, target_letter, password = line_regex.findall(line)[0]

    # count the number of target letters in the password
    char_count = password.count(target_letter)

    # check to see if the target letter is between min and max requirements
    if char_count >= int(min_count) and char_count <= int(max_count):
        valid += 1
    else:
        invalid += 1

print("Valid: " + str(valid))
print("Invalid: " + str(invalid))
