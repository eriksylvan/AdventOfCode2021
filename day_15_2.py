# https://adventofcode.com/2021/day/15

# https://www.youtube.com/watch?v=Rb0xjNAk5qI

import heapq
from collections import defaultdict



inputFile = 'input/15_input'



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

def lessRiskyPath(caveGraph, fr, dest):
    dist = { fr: 0 }
    h = []
  
    heapq.heappush(h,(0,fr))

    while len(h)!=0:
        risk, pos = heapq.heappop(h)
        if risk <= dist[pos]:
            if pos == dest:
                # destination found :-)
                print(f"Path exist Risk:{risk}")
                break
            for nextPos, nextRisk in caveGraph[pos]:
                alt = risk + nextRisk
                if nextPos not in dist or alt < dist[pos]:
                    dist[nextPos] = alt
                    heapq.heappush(h,(risk + nextRisk, nextPos))
    #Leaving bye
    return risk    
    
    
def findMyWay(caveMap):
    mxi = len(caveMap)-1
    mxj = len(caveMap[0])-1
    graph = defaultdict(list)
    for i, row in enumerate(caveMap):
        for j, r in enumerate(row):
            risk = int(r)
            #Todo: add border chriteria
            #north
            if i!=0:
                graph[(i-1,j)].append([(i,j),risk])
            #south
            if i!=mxi:graph[(i+1,j)].append([(i,j),risk])
            #west
            if j!=0:graph[(i,j-1)].append([(i,j),risk])
            #east
            if j!=mxj:graph[(i,j+1)].append([(i,j),risk])
    
    start = (0,0)
    dest = (mxi,mxj)
    return lessRiskyPath(graph, start, dest)
    
'''               
def bigCave(cave):
    h = len(cave)
    w = len(cave[0])
    Q = []
    for r in range(h):
        for c in range(w):
            for ri in range(5):
                for ci in range(5):
                    x = (cave[r][c]+ci+ri) 
                    Q[(r+height*ri,c+width*ci)] = x if x<10 else x-9
    return Q
'''

def day15PartOne():
    inp = file2List(inputFile)
    output = findMyWay(inp)
    #output = "WIP"
    print(f'# Solution Day 15, Part one:\n# Answer: {output} \n\n')


def day15PartTwo():
    inp = file2List(inputFile)
    output = findMyWay(inp)
    output = "WIP"
    
    print(f'# Solution Day 15, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day15PartOne()
    day15PartTwo()

# Solution Day 15, Part one:
# Answer: 707 


# Solution Day 15, Part two:
# Answer: WIP


# Run from terminal:
# $ python day_15.py