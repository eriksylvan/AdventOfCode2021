# https://adventofcode.com/2021/day/6
import parse


inputFile = 'input/06_input'
   

def file2List(file):
    '''Reads file with vectors on format ex '1,2,3' returs list [1,2,3]
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            for item in line.strip().split(','):
                list.append(int(item))
    return list

def readVect(inp):
    '''Reads list with vectors on format ex '8,0 -> 0,8' returs list with lists [8,0,0,8]
    '''
    vectList = []
    for v in inp:
        pattern = "{x1:d},{y1:d} -> {x2:d},{y2:d}"
        match = parse.search(pattern, v)
        vectList.append([match.named.get('x1'), match.named.get('y1'), match.named.get('x2'), match.named.get('y2')])
    return vectList


def Reporduce(fish=[], days = 1):
    '''Return a List with the fich after a number of Days of reproduction
    '''
    nextGen = []
    for d in range(days):
        nextGen = fish.copy()
        for i in range(len(fish)):
            if fish[i] == 0:
                nextGen[i] = 6
                nextGen.append(8)
            else:
                nextGen[i]-=1
        fish = nextGen.copy()
    return fish

               
def day06PartOne():
    input = file2List(inputFile)
    fish = Reporduce(input, 80)    
    output = len(fish)    
    print(f'# Solution Day 06, Part one:\n# Answer: {output} \n\n')


def day06PartTwo():
    input = file2List(inputFile)
    output = "WIP"
    print(f'# Solution Day 06, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day06PartOne()
    #day06PartTwo()

# Solution Day 06, Part one:
# Answer: 380758 




# Run from terminal:
# $ python day_06.py