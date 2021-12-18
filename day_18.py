# https://adventofcode.com/2021/day/18


inputFile = 'input/18_input'


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


def day18PartOne():
    inp = file2List(inputFile)
    output = "WIP"
    print(f'# Solution Day 18, Part one:\n# Answer: {output} \n\n')


def day18PartTwo():
    inp = file2List(inputFile)
    output = "WIP"
    
    print(f'# Solution Day 18, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day18PartOne()
    day18PartTwo()




# Run from terminal:
# $ python day_18.py