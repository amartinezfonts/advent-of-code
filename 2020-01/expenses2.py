print("Here's my expense report:")

# open the expense report file for reading
expense_report = open("input.txt", "r")

# read each line of the file into an array
expArray = expense_report.readlines()

# iterate over the array to strip the newline chars and convert to int
for i, val in enumerate(expArray):
    expArray[i] = int(expArray[i].strip())

# iterate over the array with two vars until the sum is 2020
for num1 in expArray:
    for num2 in expArray:
        for num3 in expArray:
            sum = num1 + num2 + num3
            if sum == 2020:
                print(num1, " + ", num2," + ", num3, " = ", sum)
                print(num1, " * ", num2," * ", num3, " = ", num1*num2*num3)
                break
        if sum == 2020:
            break
    if sum == 2020:
        break
