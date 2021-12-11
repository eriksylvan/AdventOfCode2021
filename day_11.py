# https://adventofcode.com/2021/day/11



inputFile = 'input/11_input'

def file2List(file):
    '''Reads file, returs list of string
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

def octopusMatrix(octList):
    '''
    Reads ist of str, returs matrix of int (Dumbo Octopuses)
    '''
    matrix = []
    for line in octList:
        matrix.append([int(ch) for ch in list(line)])
    return matrix

def flashCount(oct, steps, findsync = False):
    '''
    This method can solve both part one and two, this makes it a bit messy...
    returns flashcount and number of steps
    '''
    xmax = len(oct[0])-1 # max posiitions to prevent from Index out of range
    ymax = len(oct)-1
    
    def doFlash(xx,yy):
        yf = yy-1
        yt = yy+1
        xf = xx-1
        xt = xx+1
        if yf < 0: yf = 0
        if yt > ymax: yt = ymax
        if xf < 0: xf = 0
        if xt > xmax: xt = xmax
        
        for yi in range(yf,yt+1):
            for xi in range(xf,xt+1):
                oct[yi][xi] += 1
                if oct[yi][xi] == 10:
                    flashPositions.append((xi,yi))
                 
    flashCount = 0
    flashPositions = []
    
    #for s in range(1, steps+1,1):
    sync = False
    s=0
    
    while ((not sync)and findsync) or ((s<steps) and (not findsync)): 
        s+=1        
        #Increase energy level by 1 for all oct
        for y in range(ymax+1):
            for x in range(xmax+1):
                oct[y][x] += 1
                if oct[y][x] == 10:
                    flashPositions.append((x,y))


        while len(flashPositions) > 0:
            doFlash(flashPositions[0][0], flashPositions[0][1])
            del flashPositions[0]

        # Zero all flashes
        flashCountThisStep = 0
        for y in range(ymax+1):
            for x in range(xmax+1):
                if oct[y][x]>=10:
                    oct[y][x]=0
                    flashCountThisStep += 1                   
        flashCount += flashCountThisStep
        sync = flashCountThisStep == ((xmax+1) * (ymax+1))
        
    return flashCount, s
    
                
def day11PartOne():
    input = file2List(inputFile)
    octM = octopusMatrix(input)
    output, o2 = flashCount(octM,100) 
               
    print(f'# Solution Day 11, Part one:\n# Answer: {output} \n\n')


def day11PartTwo():
    input = file2List(inputFile)
    octM = octopusMatrix(input)
    o1, output = flashCount(octM,-1, findsync=True) 
    
    print(f'# Solution Day 11, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day11PartOne()
    day11PartTwo()

# Solution Day 11, Part one:
# Answer: 1644 


# Solution Day 11, Part two:
# Answer: 229 


# Run from terminal:
# $ python day_11.py