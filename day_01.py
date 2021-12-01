# https://adventofcode.com/2021/day/1



inputFile = 'input/01_input'
   
def depthIncreaseCounter(sw):
    '''Returns the number of times a depth measurement increases
    '''
    pd = sw[0]
    dc = 0
    for d in sw:
        if d>pd:
            dc += 1
        pd = d
    return dc

def depthIncreaseCounterSlidingWindow(sw):
    '''Returns the number of times a depth measurement increases in the 3 value sliding window
    '''
    mx = len(sw)
    pdw = sum(sw[0:3])
    dc = 0
    
    for p in range(1, mx-2):
        dw = sum(sw[p:p+3])
        if dw>pdw:
            dc+=1
        pdw = dw

    

    return dc


def file2intList(file):
    '''Reads file return list with the items in file as int
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            for item in line.strip().split(' '):
                list.append(int(item))
    return list
        

def day01PartOne():
    input = file2intList(inputFile)
    output = depthIncreaseCounter(input)

    print(
        f'# Solution Day 01, Part one:\n# Answer: {output} \n\n')


def day01PartTwo():
    # input = [199,200,208,210,200,207,240,269,260,263]
    input = file2intList(inputFile)
    output = depthIncreaseCounterSlidingWindow(input)

    print(
        f'# Solution Day 01, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day01PartOne()
    day01PartTwo()


# Solution Day 01, Part one:
# Answer: 1390 


# Solution Day 01, Part two:
# Answer: 1457 


# Run from terminal:
# $ python day_01.py