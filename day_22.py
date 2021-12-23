inputFile = 'input/22_input'
import parse   
from collections import defaultdict

def file2List(file):

    list = []
    #on x=10..12,y=10..12,z=10..12                
    pattern = "{onoff:l} x={x1:d}..{x2:d},y={y1:d}..{y2:d},z={z1:d}..{z2:d}"
    with open(file) as input:
        for line in input:
                L=line.strip()
                match = parse.search(pattern, L)
                isOn = match.named.get('onoff')=='on' 
                list.append([isOn, match.named.get('x1'), match.named.get('x2'), match.named.get('y1'), match.named.get('y2'),  match.named.get('z1'), match.named.get('z2')])
                
              	
                

    return list

def fillPack(instr):
    uni = defaultdict(bool)
	
    for r,i in enumerate(instr):
        print(r)
        for x in range(i[1], i[2]+1):
            if -50 <= x <= 50:
                for y in range(i[3], i[4]+1):
                    if -50 <= y <= 50:
                        for z in range(i[5],i[6]+1):
                            if -50 <= z <= 50:
                                uni[(x,y,z)]=i[0]
            
    return uni

def countTrueIn50(uni):
    c=0
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                if uni[(x,y,z)]:
                    c+=1
    return c

               
def day22PartOne():
    input = file2List(inputFile)
    uni = fillPack(input)
    output =countTrueIn50(uni)    
    # output = "wip"
    print(f'# Solution Day 22, Part one:\n# Answer: {output} \n\n')


def day22PartTwo():
    input = file2List(inputFile)
    output = "wip"
    print(f'# Solution Day 22, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day22PartOne()
    day22PartTwo()




# Run from terminal:
# $ python day_22.py
