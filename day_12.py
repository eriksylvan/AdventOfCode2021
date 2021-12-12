# https://adventofcode.com/2021/day/12



inputFile = 'input/12_input'

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





def readMap(mp):
    caveGrapf = {}
    for row in mp:
        rowSplit = row.split('-')
        name = rowSplit[0]
        dest = rowSplit[1]
        if name in caveGrapf.keys():
            # already exist, add new dest
            if not dest in caveGrapf[name]:
                caveGrapf[name].append(dest)             
        else:
            # New Cave, add name and dest
            caveGrapf[name] = [dest]

        if dest in caveGrapf.keys():
            if not name in caveGrapf[dest]:
                caveGrapf[dest].append(name)
        else: 
                caveGrapf[dest] = [name]
            
    return caveGrapf

def findCavePath(caveGrapf):
    pathList = []
    #visitedSmall = []   
    
    def followPath(cave, path):
        # Check all path return True if path eads to end
        
        #Addnext cave to path stack
        path.append(cave)
        if cave=='end':
            pathList.append(path.copy())
            path.pop()
            return path
        # If next cave is a small one then add to visited small
        #if cave.islower(): visitedSmall.append(cave)

        # Iterate over all ways out from cave
        for nextCave in caveGrapf[cave]:
            # if next cave is small and already visited. then this path is not valid, remove current cave from bath and return
            if nextCave.islower() and nextCave in path:
                #Dead end
                pass
            else:
                path = followPath(nextCave, path)
        path.pop()
        return path

                 
    path = []
    path = followPath('start', path)
    return pathList 

            
    
                
def day12PartOne():
    input = file2List(inputFile)
    caveMap = readMap(input)
    numberOfPath = findCavePath(caveMap)
    output = len(numberOfPath)
               
    print(f'# Solution Day 12, Part one:\n# Answer: {output} \n\n')


def day12PartTwo():
    input = file2List(inputFile)
    output = "WIP" 
    
    print(f'# Solution Day 12, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day12PartOne()
    day12PartTwo()




# Run from terminal:
# $ python day_12.py