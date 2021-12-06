class Lanternfish:
    def __init__(self, counter):
        self.counter = counter
    
    def iterate(self):
        if self.counter == 0:
            self.counter = 6
            return True
        self.counter -= 1
        return False

    def __str__(self):
        return str(self.counter)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.counter == other.counter
    
def parse_file(filename):
    array = []
    with open(filename) as in_file:
        line = in_file.readline().rstrip()
        split = line.split(',')
        print(split)
        ints = [int(number) for number in split]
        fishes = [Lanternfish(3)]
        print(fishes)
        return fishes

def iterate(fishes, days):
    counter = 0
    new_fishes = fishes
    while (counter != days):
        for fish in fishes:
            spawn = fish.iterate
            print(spawn)
            if (spawn):
                new_fishes.append(Lanternfish(8))
        counter += 1
        print('After', counter, 'days:', fishes)
    print(len(fishes))

fishes = parse_file('Inputs/p6_example_input.txt')
iterate(fishes, 2)
