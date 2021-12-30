# https://adventofcode.com/2521/day/25


inputFile = 'input/25_input'


def file2List(file):
    '''Reads file, returs list of string
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    seaCucumber = []
    
    with open(file) as input:
        for line in input:
            seaCucumber.append(list(line.strip()))

    return seaCucumber



def seaCucumber(pic):
    for y, row in enumerate(pic):
        for x, p in  enumerate(row):
            if p in('v','>'):
                print(x,y,p)
            
    return 35

def moveCumber(cumberMap):
    sizeX = len(cumberMap[0])
    sizeY = len(cumberMap)


    newCumberMap =  [['.' for i in range(sizeX)] for i in range(sizeY)]
    newCumberMap2 =  [['.' for i in range(sizeX)] for i in range(sizeY)]
    
    # move all cumbers facing East 
    for y , row in enumerate(cumberMap):
        for x, p in  enumerate(row):
            if p in('>'):
                if row[(x+1)%sizeX] in ('.'):
                    # free pos to the right, move
                    newCumberMap[y][(x+1)%sizeX] = '>'
                    newCumberMap[y][x] = '.'
                else:
                    # pblocked spot, stay
                    newCumberMap[y][x] = '>'
            elif p in ('v'):
                newCumberMap[y][x] = 'v'

    # move all cumbers facing South
    for y , row in enumerate(newCumberMap):
        for x, p in  enumerate(row):
            if p in('v'):
                if newCumberMap[(y+1)%sizeY][x] in ('.'):
                    # free pos beneath, move
                    newCumberMap2[(y+1)%sizeY][x] = 'v'
                    newCumberMap2[y][x] = '.'
                else:
                    # pblocked spot, stay
                    newCumberMap2[y][x] = 'v'
            elif p in('>'):
                newCumberMap2[y][x] = '>'


            
    return newCumberMap2.copy()


def day25PartOne():
    nextSeaC = file2List(inputFile)
    inp_test = ["v...>>.vv>",
    ".vv>>.vv..",
    ">>.>v>...v",
    ">>v>>.>.v.",
    "v>v.vv.v..",
    ">.>>..v...",
    ".vv..>.>v.",
    "v.v..>>v.v",
    "....v..v.>"]
    
    #nextSeaC = []
    #for line in inp_test:
    #        nextSeaC.append(list(line.strip()))
    
    
    stepCount = 0
    seaC = []
    while seaC != nextSeaC:
        seaC = nextSeaC.copy()
        nextSeaC = moveCumber(seaC)
        stepCount += 1

    output = stepCount
    print(f'# Solution Day 25, Part one:\n# Answer: {output} \n\n')


    


if __name__ == "__main__":
    day25PartOne()
    
# Solution Day 25, Part one:
# Answer: 426 


# Run from terminal:
# $ python day_25.py