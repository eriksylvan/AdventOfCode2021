# https://adventofcode.com/2021/day/10



inputFile = 'input/10_input'


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


                
def day10PartOne():
    input = file2List(inputFile)
    output = "WIP"
           
    print(f'# Solution Day 10, Part one:\n# Answer: {output} \n\n')


def day10PartTwo():
    input = file2List(inputFile)
    output = "WIP"
    
    print(f'# Solution Day 10, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day10PartOne()
    day10PartTwo()


# Run from terminal:
# $ python day_10.py