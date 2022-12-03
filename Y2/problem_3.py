def comparison(line):
    x = slice(0, len(line)//2)
    y = slice(len(line)//2, len(line))
    print(x, y)
    arr1 = line[x]
    arr2 = line[y]

    print(arr1, arr2)
    return [el for el in arr1 if arr2.count(el) >= 1]

def compute(el):
    # print(el)
    if el.islower():
        print("Lower", el)
        return ord(el) - 96
    else:
        print("Upper", el)
        return ord(el) - 38

def part_1(filename):
    with open(filename) as newFile:
        arr = [comparison(line) for line in newFile]
        print(arr)
        computedArr = [sum([compute(el) for el in set(i)]) for i in arr]
        return sum(computedArr)

def comparison2(line):
    arr = [x.strip() for x in line]
    # print(arr)
    one = arr[0]
    two = arr[1]
    three = arr[2]
    return [el for el in arr[0] if arr[1].count(el) >= 1 and arr[2].count(el) >= 1]

def part_2(filename):
     with open(filename) as newFile:
        file = newFile.readlines()
        arr = [file[i:i + 3] for i in range(0, len(file), 3)]
        cleaned = [set(comparison2(el)) for el in arr]
        return sum([sum([compute(el) for el in set(i)]) for i in cleaned])


# print(part_1('inputs/problem_3.txt'))

print(part_2('inputs/problem_3.txt'))