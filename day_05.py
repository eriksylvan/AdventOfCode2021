# https://adventofcode.com/2021/day/5
import parse


inputFile = 'input/05_input'
   

def file2List(file):
    '''Reads file with vectors on format ex '8,0 -> 0,8' returs list [8,0,0,8]
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
    for v in inp:
        pattern = "{x1:d},{y1:d} -> {x2:d},{y2:d}"
        match = parse.search(pattern, v)
        vectList.append([match.named.get('x1'), match.named.get('y1'), match.named.get('x2'), match.named.get('y2')])
    return vectList


def plotVect(vect, diag=False):
    '''Return a dictionalt rith all coordinates that the vector list covers
    '''
    count = {}
    for v in vect:
        dx = abs(v[2]-v[0])
        dy = abs(v[3]-v[1])
        
        if v[0]>v[2]: xStep = -1 
        else: xStep = 1
        if v[1]>v[3]: yStep = -1
        else: yStep = 1
        
        if dx == 0:
            for i in range(v[1],v[3]+yStep, yStep):
                if not (v[0],i) in count: count[(v[0],i)] = 0
                count[(v[0],i)]=count.get((v[0],i))+1
        if dy == 0:
            for i in range(v[0],v[2]+xStep, xStep):
                if not (i, v[1]) in count: count[(i, v[1])] = 0
                count[(i, v[1])]=count.get((i, v[1]))+1
 
        if dx!= 0 and dy!=0:
            if diag:
                if v[0]>v[2]: xStep = -1 
                else: xStep = 1
                if v[1]>v[3]: yStep = -1
                else: yStep = 1
                
                for i,j in zip(range(v[0],v[2]+xStep, xStep), range(v[1],v[3]+yStep,yStep) ):
                    if not (i, j) in count: count[(i, j)] = 0
                    count[(i, j)]=count.get((i, j))+1    
    return count    

def findOverlaps(d):
    c=0
    for k in (d):
        if d[k] > 1:
            c+=1
    return c


                
def day05PartOne():
    input = file2List(inputFile)
    v = readVect(input)
    o = plotVect(v)
    output = findOverlaps(o)
    
    print(f'# Solution Day 05, Part one:\n# Answer: {output} \n\n')


def day05PartTwo():
    input = file2List(inputFile)
    v = readVect(input)
    o = plotVect(v,diag=True)
    output = findOverlaps(o)
    print(
        f'# Solution Day 05, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day05PartOne()
    day05PartTwo()

# Solution Day 05, Part one:
# Answer: 5835 


# Solution Day 05, Part two:
# Answer: 17013 



# Run from terminal:
# $ python day_05.py