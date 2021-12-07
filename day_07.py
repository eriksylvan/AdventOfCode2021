# https://adventofcode.com/2021/day/7
import statistics
import sys


inputFile = 'input/07_input'
   

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

def optimalHeigt(values):
    return round(statistics.median(values))

def optimalHeigt2(values):
    mx = max(values)
    mn = min(values)
    optH = 0
    optF = sys.maxsize
    
    for h in range(mn,mx,1):
        f = fuel2(values, h)
        if f < optF:
            optF = f
            optH = h
    return optH

def fuel(heights,optHeight):
    fuel = [abs(h-optHeight) for h in heights]
    return sum(fuel)

def fuel2(heights,optHeight):
    def fc(dist):
        return dist*(dist+1) / 2
    fuel = [fc(abs(h-optHeight)) for h in heights]
    return int(sum(fuel))

def day07PartOne():
    input = file2List(inputFile)

    oh = optimalHeigt(input)     
    output = fuel(input,oh)
    print(f'# Solution Day 07, Part one:\n# Answer: {output} \n\n')


def day07PartTwo():
    input = file2List(inputFile)
    oh = optimalHeigt2(input)     
    output = fuel2(input,oh)
    print(f'# Solution Day 07, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day07PartOne()
    day07PartTwo()


# Solution Day 07, Part one:
# Answer: 336040 


# Solution Day 07, Part two:
# Answer: 94813675 



# Run from terminal:
# $ python day_07.py