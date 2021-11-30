# https://adventofcode.com/2021/day/1



inputFile = 'input/dummy_input'


def dummy(d):
    '''Dummy function for test Doubles the input
    Parameters:
    d (int): the input 
    Returns:
    int: the duble input
    '''
    return d*2
    
def summy(l):
    '''Resturns the sum of all int in a list
    Parameters:
    l [int]: the input list
    Returns:
    int: sum of all inputs
    '''
    return sum(l)
    
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
    input = 1
    output = dummy(input)

    print(
        f'Solution Day 01, Part one:\nAnswer: {output} \n\n')


def day01PartTwo():
    input = file2intList(inputFile)
    output = summy(input)

    print(
        f'Solution Day 01, Part two:\nAnswer: {output} \n\n')


if __name__ == "__main__":
    day01PartOne()
    day01PartTwo()


# Run from terminal:
# $ python day_01.py