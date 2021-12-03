
def part_1(filename):
    with open(filename) as newFile:
        horizontal = 0
        depth = 0
        aim = 0
        forwardCount = 0
        downCount = 0
        upCount = 0
        for line in newFile:
            splitLine = line.split()
            direction = splitLine[0]
            value = splitLine[1]
            if (direction == 'forward'):
                horizontal += int(value)
                depth += (aim * int(value))
                forwardCount += 1
            elif(direction == 'down'):
                # depth += int(value)
                aim += int(value)
                downCount += 1
            if (direction == 'up'):
                # depth -= int(value)
                aim -= int(value)
                upCount += 1 

        print(horizontal * depth, forwardCount, downCount, upCount)

part_1('Inputs/problem_2.txt')            