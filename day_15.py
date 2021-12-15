# https://adventofcode.com/2021/day/15


inputFile = 'input/15_input'


class Polymer():
    def __init__(self,letter, prev = None, nxt = None):
        self.letter = letter
        self.previous = prev
        self.next = nxt

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


                
def day15PartOne():
    inp = file2List(inputFile)
    output = "WIP"
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