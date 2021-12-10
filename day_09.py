# https://adventofcode.com/2021/day/9

import math


inputFile = 'input/09_input'


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

def findLocalMin(heatmap):
    mx= len(heatmap[0])
    my= len(heatmap)
    localMin = {}
    extendedHeatmap = extendHeatmap(heatmap)
    
    for y in range(1,my+1):
        for  x in range(1,mx+1):
            n = int(extendedHeatmap[y-1][x])
            s = int(extendedHeatmap[y+1][x])
            w = int(extendedHeatmap[y][x-1])
            e = int(extendedHeatmap[y][x+1])
            c = int(extendedHeatmap[y][x])
            if (c<n)and(c<s)and(c<w)and(c<e):
                # local min found
                localMin[(x-1,y-1)] = c
    return localMin

def extendHeatmap(heatmap):
    extendedHeatmap = ['9'*(len(heatmap[0])+2)]
    for row in heatmap:
        extendedHeatmap.append('9'+row+'9')
    extendedHeatmap.append('9'*(len(heatmap[0])+2))
    return extendedHeatmap

def find3LargestBasinSize(heatmap):
    extendedHeatmap = extendHeatmap(heatmap)
    
    localMin = findLocalMin(heatmap)
    sizes = []
    for x,y in localMin.keys():
        visited = []
        sizes.append(basinSize(x+1,y+1,0,visited,extendedHeatmap))

    sizes.sort(reverse=True)
    return sizes[0:3]


def basinSize(x,y, size,visited,heatmap):
    if (x,y) in visited: 
        return 0     
    visited.append((x,y))
    if heatmap[y][x]=='9':
        return 0
    else:
        size=1
    # N
    size += basinSize(x,y-1, size, visited,heatmap)
    # E
    size += basinSize(x+1,y, size, visited,heatmap)
    # S
    size += basinSize(x,y+1, size, visited,heatmap)
    # W
    size += basinSize(x-1,y, size, visited,heatmap)
    return size
                
def day09PartOne():
    input = file2List(inputFile)
    localMin = findLocalMin(input)
    output = sum(localMin.values()) + len(localMin)
           
    print(f'# Solution Day 09, Part one:\n# Answer: {output} \n\n')


def day09PartTwo():
    input = file2List(inputFile)
    localMin = findLocalMin(input)
    o3 = find3LargestBasinSize(input)
    output = math.prod(o3)
    print(f'# Solution Day 09, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day09PartOne()
    day09PartTwo()

# Solution Day 09, Part one:
# Answer: 518 


# Solution Day 09, Part two:
# Answer: 949905 

# Run from terminal:
# $ python day_09.py