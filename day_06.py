# https://adventofcode.com/2021/day/6
import parse


inputFile = 'input/06_input'
   

def file2List(file):
    '''Reads file with vectors on format ex '1,2,3' returs list [1,2,3]
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            for item in line.strip().split(','):
                list.append(int(item))
    return list


def Reporduce(fish=[], days = 1):
    '''Return a List with the fish after a number of Days of reproduction
    '''
    nextGen = []
    for d in range(days):
        nextGen = fish.copy()
        for i in range(len(fish)):
            if fish[i] == 0:
                nextGen[i] = 6
                nextGen.append(8)
            else:
                nextGen[i]-=1
        fish = nextGen.copy()
    return fish


def Reporduce2(fish=[], days = 1):
    '''Return number of fish after a number of Days of reproduction
    Function gives same result as Reproduction()
    '''
    # Only keep track of the number of fishes in each age
    
    ages=[0]*9
    for i in fish:
        ages[i]+=1

    for d in range(days):
        a0=ages[0]
        ages[0] = ages[1]
        ages[1] = ages[2]
        ages[2] = ages[3]
        ages[3] = ages[4]
        ages[4] = ages[5]
        ages[5] = ages[6]
        ages[6] = a0 + ages[7]
        ages[7] = ages[8]
        ages[8] = a0
       
    return sum(ages)

               
def day06PartOne():
    input = file2List(inputFile)
    fish = Reporduce(input, 80)    
    output = len(fish)    
    print(f'# Solution Day 06, Part one:\n# Answer: {output} \n\n')


def day06PartTwo():
    input = file2List(inputFile)
    output = Reporduce2(input, 256)    
    print(f'# Solution Day 06, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day06PartOne()
    day06PartTwo()

# Solution Day 06, Part one:
# Answer: 380758 




# Run from terminal:
# $ python day_06.py