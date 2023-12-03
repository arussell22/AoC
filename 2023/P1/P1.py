import re
numbers = ['\d', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reg = r"(?=("+'|'.join(numbers)+r"))"

def convert_to_num(line):
  
     found_nums = re.findall(reg, line)
     ints = [ str(int(el)) if el.isdigit() else str(numbers.index(el) + 1) for el in [ found_nums[0], found_nums[-1] ] ]
     num = ints[0] + ints[1]
     return int(num)
    

def readAndSum(newFile):
        lines = newFile.readlines()
        strings = [line.strip() for line in lines]
        charArrs =  [ list(strArr) for strArr in strings]

        resArr = []
        for charArr in charArrs:
              intArr = []
              for i in charArr:
                    if i.isdigit():
                        intArr.append(int(i)) 
              resArr.append(int(str(intArr[0]) + str(intArr[-1])))


with open ("part_1.txt") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        total += convert_to_num(line)

    print(total)