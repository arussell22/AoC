import numpy

def parse_file(filename):
    array = []
    with open(filename) as in_file:
        line = in_file.readline().rstrip()
        split = line.split(',')
        crabs = [int(number) for number in split]
        print(crabs)
        return crabs

def crab_median_dist(crabs):
    median = int(numpy.median(crabs))
    crabs_distance = [abs(int(crab-mean)) for crab in crabs]
    return crabs_distance

def crab_increased_dist(crabs):
    mean = round(numpy.mean(crabs))
    print(crabs)
    crabs_distance = [round(summation(crab, mean)) for crab in crabs]
    return crabs_distance

def summation(crab, mean):
    distance = crab - mean
    return .5 * (distance * (distance - 1) + crab)
crabs = parse_file('Inputs/p7_example_input.txt')
mean = numpy.mean(crabs)
print(round(mean))

print((crab_increased_dist(crabs)))
