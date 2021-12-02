# https://adventofcode.com/2021/day/2



inputFile = 'input/02_input'
   
def runSubTryOne(sw):
    '''Returns the number of times a depth measurement increases
    '''
    depth = 0
    pos = 0         
    for d in sw:
        if d[0]=='forward':
            pos+=int(d[1])
        elif d[0]=='up':
            depth-=int(d[1])
        else: #down
            depth+=int(d[1])
    return depth * pos

def runSubTryTwo(sw):
    '''Returns the number of times a depth measurement increases
    '''
    depth = 0
    pos = 0    
    aim = 0     
    for d in sw:
        if d[0]=='forward':
            pos+=int(d[1])
            depth+=aim * int(d[1])
        elif d[0]=='up':
            aim-=int(d[1])
        else: #down
            aim+=int(d[1])
    return depth * pos


def file2List(file):
    '''Reads file return list with the items in file as ['down', '6']
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            list.append(line.strip().split(' '))
    return list
        

def day02PartOne():
    input = file2List(inputFile)
    output = runSubTryOne(input)
    print(
        f'# Solution Day 02, Part one:\n# Answer: {output} \n\n')


def day02PartTwo():
    input = file2List(inputFile)
    output = runSubTryTwo(input)
    print(
        f'# Solution Day 02, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day02PartOne()
    day02PartTwo()


# Solution Day 02, Part one:
# Answer: 2091984 


# Solution Day 02, Part two:
# Answer: xxx 


# Run from terminal:
# $ python day_01.py