
def part_1(filename, count):
    with open(filename) as newFile:
        arr = [ el for el in newFile.readlines()[0] ]

        for i in range(0, len(arr) - (count - 1)):
            if len(set(arr[i:i+count])) == count:
                return i + count

# print(part_1("inputs/problem_6.txt", 4))

print(part_1("inputs/problem_6.txt", 14))