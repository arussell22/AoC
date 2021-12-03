import collections
def find_bit(filename, least_common):
    with open(filename) as in_file:
        s_array = {}
        for line in in_file:
            number_array = list(line)
            for i in range(len(number_array)-1):
                number = int(number_array[i])
                significant_count= {"zero": 0, "one": 0}
                if len(s_array) <= i:
                    s_array[i] = {'zero': 0, 'one': 0}
                if number == 0:
                    s_array[i]['zero'] += 1
                elif number == 1:
                    s_array[i]['one'] += 1
        str1 = " "
        common_bits = []
        for i in range(len(s_array)):
            if least_common:
                to_append = 0 if s_array[i]['zero'] > s_array[i]['one'] else 1
                common_bits.append(to_append) 
            if not least_common:
                to_append = 1 if s_array[i]['zero'] > s_array[i]['one'] else 0
                common_bits.append(to_append) 
        return(' '.join([str(elem) for elem in common_bits]).replace(" ", ""))

def find_bit_2(filename, least_common):
    with open(filename) as in_file:
        lines = in_file.readlines()
        number_lines = [list(line)[:-1] for line in lines]
        print(number_lines)
        s_array = {}
        i = 0
        while(len(number_lines) > 1):
            for line in number_lines:
                print(line)
                number = int(line[i])
                if len(s_array) <= i:
                    s_array[i] = {'zero': 0, 'one': 0}
                if number == 0:
                    s_array[i]['zero'] += 1
                elif number == 1:
                    s_array[i]['one'] += 1
                
            str1 = " "
            common_bits = []
            if least_common:
                bit = 0 if s_array[i]['zero'] > s_array[i]['one'] else 1
                number_lines = [line[i] == str(bit) for line in number_lines ]
            if not least_common:
                bit = 1 if s_array[i]['zero'] > s_array[i]['one'] else 0
                number_lines = [line[i] == str(bit) for line in number_lines ]
            i += 1
        toReturn = ' '.join([str(elem) for elem in number_lines[0]]).replace(" ", "")
        print(toReturn)
        return()


find_bit_2('Inputs/problem_3.txt', True)
# gamma = find_bit('Inputs/problem_3.txt', True)
# epsilon = find_bit('Inputs/problem_3.txt', False)

# print(gamma)
# print(epsilon)
# print ('gamma:', int(gamma, 2), 'epsilon:', int(epsilon, 2), '=', int(gamma, 2)* int(epsilon, 2))
