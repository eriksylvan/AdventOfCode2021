# https://adventofcode.com/2021/day/15


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

def initCave(template):
    return None    

def enterCave(cMap):
    
    def move(cavemap, path, risk, minRisk, minPath, pos, visited):
        if not pos in visited:
            r = int(cavemap[pos[1]][pos[0]])
            if pos!=(0,0):
                risk += r
            visited.append(pos)
            # If risk at this point is greater than the lowest risk found then skip this path
            if risk <= minRisk:
                if pos[0] == mapSize[0]-1 and pos[1] == mapSize[1]-1 :
                    # Cave exit reached
                    print(f"exit: {risk},  MinRisk: {minRisk}, Path:{''.join(path)}")
                    if risk < minRisk: 
                        minRisk = risk
                        minPath = path.copy()
                else:    
                
                    if pos[1] < mapSize[1]-1:
                        path.append('s')
                        risk, path, minRisk, minPath, visited = move(cavemap, path, risk, minRisk, minPath, (pos[0], pos[1]+1), visited) #move south
                        path.pop()
                    if pos[0] < mapSize[0]-1:
                        path.append('e')
                        risk, path,minRisk, minPath, visited = move(cavemap, path, risk, minRisk, minPath, (pos[0]+1, pos[1]), visited) #move east
                        path.pop()
                    if pos[1] > 0:
                        path.append('n')
                        risk, path, minRisk, minPath, visited = move(cavemap, path, risk, minRisk, minPath, (pos[0], pos[1]-1), visited) #move north
                        path.pop()
                    if pos[0] > 0:
                        path.append('w')
                        risk, path, minRisk, minPath, visited = move(cavemap, path, risk, minRisk, minPath, (pos[0]-1, pos[1]), visited) #move west
                        path.pop()
            else:
                pass
                #print(f"Skip this route: {risk}. MinRisk: {minRisk}, {len(path)}, Path:{''.join(path)}")    
            
            #move back, reduce risk
            risk -=r    
            if visited!=[]: visited.pop()
        return risk, path, minRisk, minPath, visited

    # init
    path = []
    minPath = []
    risk = 0
    visited = []
    position = (0,0) # x,y
    minRisk = 999999999
    mapSize = len(cMap[0]),len(cMap)
    # start moving
    
    risk, path,minRisk, minPath, visited = move(cMap, path, risk, minRisk, minPath, (0,0), visited)
        
    return minRisk, minPath
    
    
    
    
    
    
    
                
def day15PartOne():
    inp = file2List(inputFile)
    risk, path = enterCave(inp)
    output = risk
    print(f'# Solution Day 15, Part one:\n# Answer: {output} \n\n')


def day15PartTwo():
    inp = file2List(inputFile)
    output = "WIP"
    
    print(f'# Solution Day 15, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day15PartOne()
    day15PartTwo()




# Run from terminal:
# $ python day_15.py