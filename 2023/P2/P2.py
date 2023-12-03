import re
def convert_to_game(line):
     game_num = re.findall("\d+", line)[0]
     game = re.split('; |:', line.strip())[1:]
     good_game = True
     for round in game:
        for color in round.strip().split(","):
            if ('red' in color):
                if int(re.findall("\d+", color)[0]) > 12:
                    good_game = False
                    break
            if ('green' in color):
                if int(re.findall("\d+", color)[0]) > 13:
                    good_game = False
                    break
            if ('blue' in color):
                if int(re.findall("\d+", color)[0]) > 14:
                    good_game = False
                    break                
     return int(game_num) if good_game else 0

def get_lowest_cubes(line):
     game = re.split('; |:|,', line.strip())[1:]

     lowest_red = max([ int(re.findall("\d+", x)[0]) for x in game if "red" in x])
     lowest_green = max([ int(re.findall("\d+", x)[0]) for x in game if "green" in x])
     lowest_blue = max([ int(re.findall("\d+", x)[0]) for x in game if "blue" in x])

     return lowest_green * lowest_red * lowest_blue
        

with open ("part_2.txt") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        total += get_lowest_cubes(line)

    print(total)