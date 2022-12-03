import numpy as np
def readAndSum(newFile):
        lines = newFile.readlines()
        lines = [line.strip() for line in lines]
        arr = np.array(lines)
        result = np.where(arr == '')

        split = np.split(arr, result[0])
        arrs = [sum([int(newEl) for newEl in el if newEl]) for el in split]
        # sorted = arrs.sort()
        arrs.sort()
        return arrs

def part_1(filename):
    with open(filename) as newFile:
        arr = readAndSum(newFile)
        return arr[len(arr) - 1]

def part_2(filename):
        with open(filename) as newFile:
            arr = readAndSum(newFile)
            return sum([arr[len(arr) - 1], arr[len(arr) - 2], arr[len(arr) - 3]])

print(part_1('inputs/problem_1.txt'))

print(part_2('inputs/problem_1.txt'))



# print(eval(''))