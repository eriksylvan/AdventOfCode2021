# https://adventofcode.com/2021/day/17



inputFile = 'input/17_input'
   
def depthIncreaseCounter(sw):
    '''Returns the number of times a depth measurement increases
    '''
    # list comprehension solution inspired by https://www.reddit.com/user/smokebath/
    return sum((sw[i+1] > sw[i] for i in range(len(sw)-1))) 
            
    # pd = sw[0]
    # dc = 0
    # for d in sw:
    #     if d>pd:
    #         dc += 1
    #     pd = d
    # return dc

def depthIncreaseCounterSlidingWindow(sw):
    '''Returns the number of times a depth measurement increases in the 3 value sliding window
    '''
    mx = len(sw)
    pdw = sum(sw[0:3])
    dc = 0
    
    for p in range(1, mx-2):
        dw = sum(sw[p:p+3])
        if dw>pdw:
            dc+=1
        pdw = dw

    return dc


def file2intList(file):
    '''Reads file return list with the items in file as int
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            for item in line.strip().split(' '):
                list.append(int(item))
    return list
    
    
    
def inTargetArea(x,y , tx1, tx2, ty1, ty2):
    return tx1 <= x<= tx2 and ty1 <= y <= ty2

def launchProbe(vx, vy, tx1, tx2, ty1, ty2):
    px = 0
    py = 0
    hMax = 0 
    while px <= tx2 and py >= ty1:
        if vy == 0: 
            hMax = py
        if inTargetArea(px,py , tx1, tx2, ty1, ty2): 
             return True, hMax
        px = px + vx 
        if vx != 0: 
            vx -= 1
        py += vy
        vy -=1     
    return False, 0    

def day17PartOne():
    
    hMax  = 0
    xMax = -100
    yMax = -100
    hitcount = 0
    for x in range(1000):
        for y in range(-1000,1000,1):
            hit, h = launchProbe(x, y, 244, 303, -91, -54)
            #hit, h = launchProbe(x, y, 20, 30, -10, -5)
            if hit: 
                hitcount+=1
                print(hitcount, x, y, h)
                # print(hitcount, x, y, h)
                if h > hMax:
                    hMax = h
                    xMax = x
                    yMax = y
                    
                    print(f"New Max:{hMax}")
                
    
    output = hMax


    print(
        f'# Solution Day 17, Part one:\n# Answer: {output} \n\n')
    print(
        f'# Solution Day 17, Part two:\n# Answer: {hitcount} \n\n')

def day17PartTwo():
    #input = file2intList(inputFile)
    output = "WIP"

   
    pass


if __name__ == "__main__":
    day17PartOne()
    #day17PartTwo()

# Solution Day 17, Part one:
# Answer: 4095 


# Solution Day 17, Part two:
# Answer: 3773 


# Run from terminal:
# $ python day_17.py