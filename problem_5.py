class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x) +','+str(self.y)+')'

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def parse_file(filename):
    array = []
    with open(filename) as in_file:
        lines = in_file.readlines()
        for line in lines:
            no_whitespace = line.replace(" ", "").rstrip()
            split = no_whitespace.split("->")
            parsed = [val.split(",") for val in split]
            to_array = find_line(parsed)
            array += to_array
    print(len(list_duplicates(array)))

def list_duplicates(a):
    #from https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
    seen = {}
    dupes = []
    for x in a:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    return dupes

def find_line(array):
    if(len(array) == 2):
        main_array = []
        first = array[0]
        second =array[1]
        point_1 = Point(int(first[0]), int(first[1]))
        point_2 = Point(int(second[0]), int(second[1]))
        x1 = point_1.x
        x2 = point_2.x
        y1 = point_1.y
        y2 = point_2.y
        if(x1 == x2):
            if (y1 < y2):
                start = y1
                end = y2+1
            else:
                start = y2
                end = y1+1
            for i in range(start, end):
                main_array.append(Point(x1, i))
        elif(y1==y2):
            if (x1 < x2):
                start = x1
                end = x2+1
            else:
                start = x2
                end = x1+1
            for i in range(start, end):
                main_array.append(Point(i, y1))
        elif (abs(x1 - x2) == abs(y1-y2)): 
            for i in range(abs(x1-x2)+1):
                if (x1 - x2) < 0:
                    x = x1 + i
                else:
                    x = x1 - i
                if(y1 - y2) < 0:
                    y = y1 + i
                else:
                    y = y1 - i
                main_array.append(Point(x, y))
        return main_array

  
parse_file('Inputs/p5_input.txt')
