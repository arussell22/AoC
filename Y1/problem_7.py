import numpy
from math import floor, ceil

def parse_file(filename):
    array = []
    with open(filename) as in_file:
        line = in_file.readline().rstrip()
        split = line.split(',')
        crabs = [int(number) for number in split]
        # print(crabs)
        return crabs

def crab_median_dist(crabs):
    median = int(numpy.median(crabs))
    crabs_distance = [abs(int(crab-median)) for crab in crabs]
    return crabs_distance

def crab_increased_dist(crabs):
    mean = round(numpy.mean(crabs))
    # print(crabs)
    crabs_distance = [round(summation(crab, mean)) for crab in crabs]
    return crabs_distance

def summation(crab, mean):
    distance = abs(crab - mean)
    # return .5 * (distance * (distance - 1) + distance)
    return distance*(distance+1)/2

def sum_n(n):
    if n <= 1:
        return n
    else:
        return n + sum_n(n-1)

def t(v):
    return v*(v+1)/2

def test(c):
    m = float(sum(c)) / len(c)
    v = min([sum([t(abs(v - i)) for v in c]) for i in [int(floor(m)), int(ceil(m))]])
    print(v)

crabs = parse_file('Inputs/p7_input.txt')
mean = numpy.mean(crabs)
print(sum(crab_median_dist(crabs)))

print(test(crabs))
