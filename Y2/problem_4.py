def pairs(line):
    return [list(range(int(el.split('-')[0]), int(el.split('-')[1]) + 1)) for el in line.strip().split(',')]

def getAssignment(line):
    # 
    op = pairs(line)
    calc = set(op[0] + op[1])
    calcLen = len(calc)
    if calcLen == len(op[0]) or calcLen == len(op[1]):
        return calc
    else:
        return None

def getOverlap(line):
    op = pairs(line)
    calc = op[0] + op[1]
    beforeSet = len(calc)
    after = len(set(calc))
    return beforeSet if beforeSet != after else None

def part_1(filename):
    with open(filename) as newFile:
        arr = [el for el in [getAssignment(line) for line in newFile] if el]
        return len(arr)

def part_2(filename):
    with open(filename) as newFile:
        arr = [el for el in [getOverlap(line) for line in newFile] if el]
        return len(arr)

# print(part_1('inputs/problem_4.txt'))

print(part_2('inputs/problem_4.txt'))
