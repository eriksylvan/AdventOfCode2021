# https://adventofcode.com/2021/day/8
import itertools


inputFile = 'input/08_input'


def file2List(file):
    '''Reads file, returs list of lines
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

def readDigitData(inp):
    '''Reads list data abour 7 segments digitis, splits it and return two lists, output and input 
    '''
    inputList = []
    outputList = []
     
    for v in inp:
        tv = v.split('|')
        inputList.append(tv[0].strip().split())
        outputList.append(tv[1].strip().split())
    return inputList, outputList

def countEasy(l):
    '''
    Counts the digits that are easy to rekognize (Part1)
    '''
    count = 0;
    for r in l:
        for i in r:
            if len(i) in (2,3,4,7):
                count +=1
    return count


def findWieringPattern(digits):
    '''
    This method finfd the wiering by trying out all possible wiering. 
    When first correct wiering is found it stops and returns the wiering pattern as a tuple.
    Position of the letter in the wiering pattern corresponds to one segment on the 7 segment display as follow:
    
     6666
    5    1
    5    1
     ffff
    4    2
    4    2
     3333
    
    For example: the wiering below is represented as: ('d', 'a', 'b', 'c', 'g', 'e', 'f')
    
     dddd
    e    a
    e    a
     ffff
    g    b
    g    b
     cccc
    '''
    segments = 'abcdefg'
    per = list(itertools.permutations(segments))
    
    
    for pattern in per:
        allOK = True
        for dig in digits:
            d = getDigit(dig,pattern)
            if d == -1:
                allOK = False
                break
        if allOK:
            #correct wiering found
            return pattern
    return False

        
def getDigit(dig,pattern):
    '''
    Return the digit represented by the segments in the input with given the wiering pattern
    Parameters:
    dig: the activated wires giving the digit as string (a-f)
    pattern: wiering pattern as a tuple ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    Returns:
    digit: number on display as int, -1 if unvalid number
    '''
    digList = set(dig)
    if digList == {pattern[0], pattern[1], pattern[2], pattern[3], pattern[4], pattern[5]}:
        return 0
    elif digList == {pattern[1], pattern[2]}:
        return 1
    elif digList == {pattern[0], pattern[1], pattern[3], pattern[4], pattern[6]}:
        return 2
    elif digList == {pattern[0], pattern[1], pattern[2], pattern[3], pattern[6]}:
        return 3
    elif digList == {pattern[1], pattern[2], pattern[5], pattern[6]}:
        return 4
    elif digList == {pattern[0], pattern[2], pattern[3], pattern[5], pattern[6]}:
        return 5
    elif digList == {pattern[0], pattern[2], pattern[3], pattern[4], pattern[5], pattern[6]}:
        return 6
    elif digList == {pattern[0], pattern[1], pattern[2]}:
        return 7
    elif digList == {pattern[0], pattern[1], pattern[2], pattern[3], pattern[4], pattern[5], pattern[6]}:
        return 8
    elif digList == {pattern[0], pattern[1], pattern[2], pattern[3], pattern[5], pattern[6]}:
        return 9
    else: 
        return -1
    

def decodeOutputValue(inp, out):
    '''
    Finds the wiering pattern, decodes and return the output value 
    '''
    p = findWieringPattern(inp)
    o1 = getDigit(out[0], p)    
    o2 = getDigit(out[1], p)
    o3 = getDigit(out[2], p)
    o4 = getDigit(out[3], p)        
    return (o1*1000+o2*100+o3*10+o4)
    

                
def day08PartOne():
    input = file2List(inputFile)
    i,o = readDigitData(input)
    output = countEasy(o)
    print(f'# Solution Day 08, Part one:\n# Answer: {output} \n\n')


def day08PartTwo():
    input = file2List(inputFile)
    inp,out = readDigitData(input)
    values = []
    for i in range(len(input)):
        values.append(decodeOutputValue(inp[i],out[i]))
    output = sum(values)
    print(f'# Solution Day 08, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day08PartOne()
    day08PartTwo()

# Solution Day 08, Part one:
# Answer: 237 


# Solution Day 08, Part two:
# Answer: 1009098 

# Run from terminal:
# $ python day_08.py