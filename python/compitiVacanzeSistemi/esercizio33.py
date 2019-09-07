def printPlusAppend(i, numbers, increment):
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + increment

    print("Numbers now: ", numbers)
    print("At the bottom i is {}".format(i))
    return i

i = 0
numbers = []
number = 25

for i in range (0, number):
    i = printPlusAppend(i, numbers, 5)
