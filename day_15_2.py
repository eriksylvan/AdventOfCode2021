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
    
    
def findMyWay(caveMap, dup=1):
    cmi = len(caveMap)
    cmj = len(caveMap[0])
    
    mxi = len(caveMap)*dup-1
    mxj = len(caveMap[0])*dup-1
    print(mxi, mxj)
    graph = defaultdict(list)
    for i, row in enumerate(caveMap):
        for j, r in enumerate(row):
            for f in range(dup):
                for g in range(dup):     
                    ii = i + cmi * f    
                    jj = j + cmj * g   
                    risk = int(r)+f+g
                    if risk>9:
                        risk=risk-9
                    #north
                    if ii!=0:
                        graph[(ii-1),jj].append([(ii, jj), risk])
            #south
                    if ii!=mxi:

                        graph[((ii+1),jj)].append([(ii,jj),risk])
            #west
                    if jj!=0:

                        graph[(ii,(jj-1)) ].append([(ii, jj),risk])
            #east
                    if jj!=mxj:

                        graph[(ii,(jj+1))].append([(ii,jj),risk])
    
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
    output = findMyWay(inp,1)
    #output = "WIP"
    print(f'# Solution Day 15, Part one:\n# Answer: {output} \n\n')


def day15PartTwo():
    inp = file2List(inputFile)
    output = findMyWay(inp,5)
    #output = "WIP"
    
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
