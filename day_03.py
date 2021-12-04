# https://adventofcode.com/2021/day/3



inputFile = 'input/03_input'
   
def calcge(inp):
    '''Returns product of gamma and epsilon
    '''
    output0 = [0]*len(inp[0])
    l = len(output0)

    for r in inp:
        for i, ch in zip(range(l), r):
            output0[i]+=int(ch)
        
    l = len(inp)/2
    o1 = ['1' if i>=l else '0' for i in output0]
    o0 = ['0' if i>=l else '1' for i in output0]
    b1=''.join(map(str,o1))
    b0=''.join(map(str,o0))
    r1 = int(b1,2)
    r0 = int(b0,2)
    return r0*r1

def calcLife(inp):
    '''Returns product multiply the oxygen generator rating and the CO2 scrubber rating
    '''
    l = len(inp[0])
    
    def bitCriteria(keepMostCommon=True):
        inpList=[]
        for b in inp:
            inpList.append([b,True])  #[0] = the bitvalue [1]=keep
        kept=len(inp)
        for i in range(l):
            count1=0
            # First bit
            for r in inpList:
                if r[1]:
                    if r[0][i]=='1':
                        count1+=1
            
            if keepMostCommon:
                if count1>=kept/2: 
                    mcb='1'
                else: 
                    mcb='0'
            else:
                if count1>=kept/2: 
                    mcb='0'
                else: 
                    mcb='1'
            
            for r in inpList:
                if r[1]:#Kept
                    if r[0][i]==mcb:
                        r[1]=True
                    else:
                        r[1]=False
                        kept-=1
                if kept==1:break
            if kept==1:break 
            
        for i in inpList:
            if i[1]:
                ox=i[0]
                return int(ox,2)
    

    oxi= bitCriteria(True)
    co2= bitCriteria(False)
        
        
    return oxi * co2


def file2List(file):
    '''Reads file return list with the items in file as ['down', '6']
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
        

def day03PartOne():
    input = file2List(inputFile)
    output = calcge(input)
    print(f'# Solution Day 03, Part one:\n# Answer: {output} \n\n')


def day03PartTwo():
    input = file2List(inputFile)
    output = calcLife(input)
    print(
        f'# Solution Day 03, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day03PartOne()
    day03PartTwo()


# Solution Day 03, Part one:
# Answer: 3985686 


# Solution Day 03, Part two:
# Answer: 2555739 


# Run from terminal:
# $ python day_03.py