# https://adventofcode.com/2021/day/3



inputFile = 'input/03_input'
   
def calcge(inp):
    '''Returns product of gamma and epsilon
    '''
    output0 = [0]*len(inp[0])
    print(output0)
    l = len(output0)

    for r in inp:
        for i, ch in zip(range(l), r):
            output0[i]+=int(ch)
        
    l = len(inp)/2
    o1 = ['1' if i>=l else '0' for i in output0]
    o0 = ['0' if i>=l else '1' for i in output0]
    b1=''.join(map(str,o1))
    b0=''.join(map(str,o0))
    r1 = int(b1,2)
    r0 = int(b0,2)
    print(output0, o0,o1,b0,b1,r0,r1)
    return r0*r1

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
            list.append(line.strip())
    return list
        

def day03PartOne():
    input = file2List(inputFile)
    output = calcge(input)
    print(f'# Solution Day 02, Part one:\n# Answer: {output} \n\n')


def day03PartTwo():
    input = file2List(inputFile)
    output = runSubTryTwo(input)
    print(
        f'# Solution Day 02, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day03PartOne()
    #day02PartTwo()


# Solution Day 02, Part one:
# Answer: 2091984 


# Solution Day 02, Part two:
# Answer: xxx 


# Run from terminal:
# $ python day_01.py