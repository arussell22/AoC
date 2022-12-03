  def parse_file(filename):
    array = []
    with open(filename) as in_file:
        line = in_file.readline().rstrip()
        split = line.split(',')
        fishes = [int(number) for number in split]
        school = {}
        for fish in fishes:
            if fish not in school.keys():
                school[fish] = 1
            else:
                school[fish] += 1
        print(school)
        return school

def iterate(schools, days):
    counter = 0
    while (counter < days):
        new_schools = {}
        for key,value in schools.items():
            if (key == 0):
                if (6 not in new_schools.keys()):
                    new_schools[6] = value
                else:
                    new_schools[6] += value
                new_schools[8] = value
            else:
                if key-1 not in new_schools.keys():
                    new_schools[key-1] = value
                else:
                    new_schools[key-1] += value
        counter += 1
        schools = new_schools
    print(sum(schools.values()))
    
fishes = parse_file('Inputs/p6_input.txt')
iterate(fishes, 256)
