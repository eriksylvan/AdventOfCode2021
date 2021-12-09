# https://adventofcode.com/2021/day/9


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

def riskLevel(heatmap):
    return 0
    
                
def day09PartOne():
    input = file2List(inputFile)
    output = "WIP"
    print(f'# Solution Day 09, Part one:\n# Answer: {output} \n\n')


def day09PartTwo():
    input = file2List(inputFile)
    output = "WIP"
    print(f'# Solution Day 09, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day09PartOne()
    day09PartTwo()


# Run from terminal:
# $ python day_09.py