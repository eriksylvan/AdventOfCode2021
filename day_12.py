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

caveGrapf = {}



def readMap(mp):
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

def findCavePath():
    pathList = ['start']
    visitedSmall = []   
    
    def followPath(nextCave, path):
        # Check all path return True if path eads to end
        
        #Addnext cave to path stack
        path.append(nextCave)
        
        # If next cave is a small one then add to visited small
        
        # Iterate over all ways out from cave
            # if next cave = 'end' tehn add path to avlid path
            # if next cave is small and already visited. then this path is not valid, remove current cave from bath and return
            # annars folowPath(nextCave, path) 

        
       
       
       
       
       
       
       
       
       
       '''
        if nextCave=='end': 
            return True # end found
        for cave in caveGrapf[nextCave]:
            if cave in visitedSmall:
                #This small cave already visited, skip path
                
                return False
            if cave.islower():
                visitedSmall.append(cave)
            if followPath(cave,path):
                # end found
                # save this path
                pathList.append(path)
        return False
    '''
    
    p = []
    followPath('start', p)
    return 0
            
    
                
def day12PartOne():
    input = file2List(inputFile)
    caveMap = readMap(input)
    output = "WIP" 
               
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