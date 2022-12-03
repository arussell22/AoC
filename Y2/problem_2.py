import numpy as np

def convert(a):
    if a in ['A', 'X']:
        return 1   
    elif a in ['B', 'Y']:
        return 2
    else:
        return 3


def compare(a, b):
    comparison = a - b
    if comparison == 0:
        result = 3
    elif comparison in [-1, 2]:
        result = 6
    else:
        result = 0
    return b + result

def readAndSum(newFile):
        lines = newFile.readlines()
        lines = [[convert(el) for el in line.strip() if el.strip()] for line in lines]
        
        arrLine = [compare(line[0], line[1]) for line in lines]
        # arr = np.array(lines)
        # result = np.where(arr == '')

        # split = np.split(arr, result[0])
        # arrs = [sum([int(newEl) for newEl in el if newEl]) for el in split]
        # # sorted = arrs.sort()
        # arrs.sort()
        return sum(arrLine)

def win(a):
    if a == 1:
        return 2
    elif a == 2:
        return 3
    else:
        return 1

def lose(a):
    if a == 1:
        return 3
    elif a == 2:
        return 1
    else:
        return 2

def getOwn(a, b):
    if b == 1:
        return lose(a)
    elif b == 2:
        return a
    else:
        return win(a) 

def getResult(a):
    if a == 1:
        return 0
    elif a == 2:
        return 3
    else:
        return 6
def part_1(filename):
    with open(filename) as newFile:
        arr = readAndSum(newFile)
        return arr

def part_2(filename):
        with open(filename) as newFile:
            lines = newFile.readlines()
            lines = [[convert(el) for el in line.strip() if el.strip()] for line in lines]
            arrLines = [getOwn(line[0], line[1]) + getResult(line[1]) for line in lines]
            return sum(arrLines)

        

# print(part_1('inputs/problem_2.txt'))

print(part_2('inputs/problem_2.txt'))