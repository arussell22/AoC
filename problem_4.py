def read_in_boards(filename):
    with open(filename) as in_file:
        parsed = [[{'number': int(var), 'marked': False} for var in line.rstrip().split()] for line in in_file.readlines() if len(line.rstrip()) > 0]
        boards = {}
        for i in range(int(len(parsed)/5)):
            index = i * 5
            board_array = []
            for j in range(index, index+5):
                board_array.append(parsed[j])
            boards[i]=board_array
        return boards 

def mark_boards(boards, number):
    for key, value in boards.items():
        for line in value:
            for card_number in line:
                if card_number['number'] == number:
                    card_number['marked'] = True
    return boards


def parse_numbers(filename):
    with open(filename) as in_file:
        line = in_file.readline().rstrip().split(",")
        parsed = [int(var) for var in line]
        return parsed

def check_bingo(boards):
    toPop = []
    for key, board in boards.items():
        if (check_rows(board)):
            toPop.append(key)
        if check_cols(board):
            toPop.append(key)
    return {'NO_BINGO': boards, 'BINGO': toPop}

def check_rows(board):
    for line in board:
        checked_row = [number for number in line if number["marked"] == True]
        if(len(checked_row) == 5):
            return True
    return False

def check_cols(board):
    for i in range(len(board)):
            checked_col = [line[i] for line in board if line[i]["marked"] == True]
            if(len(checked_col) == 5):
                return True
    return False

def get_sum_of_board(board):
    sum = 0
    for line in board:
        for number in line:
            if (number['marked'] == False):
                sum += number['number']
    return sum

def run_bingo():
    values = parse_numbers('Inputs/p4_input.txt')
    boards = read_in_boards('Inputs/p4_boards.txt')

    for i in range(len(values)):
        value = values[i]
        boards = mark_boards(boards, value)
        if (i >= 4):
            checked_boards = check_bingo(boards)
            is_Bingo = len(checked_boards['BINGO']) > 0
            if(is_Bingo):
                sum = get_sum_of_board(boards[checked_boards['BINGO'][0]])
                print(sum * value)
                return


def run_bingo_last_to_win():
    values = parse_numbers('Inputs/p4_input.txt')
    boards = read_in_boards('Inputs/p4_boards.txt')
    # values = parse_numbers('Inputs/p4_example_inputs.txt')
    # boards = read_in_boards('Inputs/p4_example_boards.txt')

    for i in range(len(values)):
        value = values[i]
        boards = mark_boards(boards, value)
        if (i >= 4):
            checked_boards = check_bingo(boards)
            is_Bingo = len(checked_boards['BINGO']) > 0
            if(is_Bingo and (len(boards.items()) == 1)):
                sum = get_sum_of_board(boards[checked_boards['BINGO'][0]])
                print(sum * value)
                return
            elif(is_Bingo):
                for key in checked_boards['BINGO']:
                    boards.pop(key, None)
                

run_bingo()
run_bingo_last_to_win()


