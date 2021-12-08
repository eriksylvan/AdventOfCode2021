# https://adventofcode.com/2021/day/8
import parse


inputFile = 'input/08_input'


def file2List(file):
    '''Reads file with vectors on format ex '8,0 -> 0,8' returs list of lines
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

def readVect(inp):
    '''Reads list with vectors on format ex '8,0 -> 0,8' returs list with lists [8,0,0,8]
    '''
    vectList = []
    inputList = []
    outputList = []
     
    for v in inp:
        tv = v.split('|')
        inputList.append(tv[0].strip().split())
        outputList.append(tv[1].strip().split())
    return inputList, outputList

def countEasy(l):
    count = 0;
    for r in l:
        for i in r:
            if len(i) in (2,3,4,7):
                count +=1
    return count
    
                
def day08PartOne():
    input = file2List(inputFile)
    i,o = readVect(input)
    output = countEasy(o)
    print(f'# Solution Day 08, Part one:\n# Answer: {output} \n\n')


def day08PartTwo():
    input = file2List(inputFile)
    
    output = "WIP"
    print(f'# Solution Day 08, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day08PartOne()
    #day08PartTwo()


# Run from terminal:
# $ python day_08.py