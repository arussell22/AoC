import numpy as np
def readAndSum(newFile):
        lines = newFile.readlines()
        lines = [line.strip() for line in lines]
        arr = [ element[0] + element[-1] if len(element) > 1 else element[0]  for element in  [filter(lambda x: x.isdigit(), line.split()) for line in lines]]
        # arr = np.array(lines)
        # result = np.where(arr == '')

        # split = np.split(arr, result[0])
        # arrs = [sum([int(newEl) for newEl in el if newEl]) for el in split]
        # # sorted = arrs.sort()
        # arrs.sort()
        return sum(arr)


def read(newFile):
        lines = newFile.readlines()
