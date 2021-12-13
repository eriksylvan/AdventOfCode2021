# https://adventofcode.com/2021/day/13

import numpy as np


inputFile = 'input/13_input'

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

def getPaperLayout(inp):
    paper = []
    
    for row in inp:
        if len(row) == 0: 
            break
        s = row.strip().split(",")
        paper.append([int(s[0]),int(s[1])])
    
    mx = np.max(paper, axis=0)
    
    fullPaper = np.zeros([mx[1]+1, mx[0]+1], dtype = int)
    for p in paper:
        fullPaper[p[1],p[0]] = 1
    
    return fullPaper

def getFoldingInstructions(inp):
    folding = []
    for row in inp:
        if len(row)>0: 
            if row[0] == "f": 
                s = row.strip().split("=")
                folding.append([s[0],int(s[1])])
    return folding

def fold(m, f, axis):
    
    if axis == 'x':
        m = np.rot90(m,-1)
    z = np.zeros(np.shape(m),dtype=int)
    a = m[:f,:]
    az = z.copy()
    az[az.shape[0]-a.shape[0]:,az.shape[1]-a.shape[1]:] = a 
    b = m[f+1:,:]        
    bz = z.copy()
    bz[:b.shape[0],:b.shape[1]] = b
    bz = np.flipud(bz)
        
    folded = az | bz
    
    if a.shape[0] > b.shape[0]:
        folded = folded[folded.shape[0]-a.shape[0]:,folded.shape[1]-a.shape[1]:]
    else: 
        folded = folded[folded.shape[0]-b.shape[0]:,folded.shape[1]-b.shape[1]:]
    
    if axis == 'x':
        folded = np.rot90(folded,1)
    
        
    return folded
                
def day13PartOne():
    inp = file2List(inputFile)
    paper = getPaperLayout(inp)
    foInstr = getFoldingInstructions(inp)
    fPos = foInstr[0][1]
    fAx = foInstr[0][0][-1]
    folded = fold(paper, fPos, fAx)
    output =  sum(sum(folded)) 
    
    
    
               
    print(f'# Solution Day 13, Part one:\n# Answer: {output} \n\n')


def day13PartTwo():
    input = file2List(inputFile)
    output = "WIP"
    
    print(f'# Solution Day 13, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day13PartOne()
    day13PartTwo()




# Run from terminal:
# $ python day_12.py