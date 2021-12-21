# https://adventofcode.com/2021/day/21
import random
import itertools

#inputFile = 'input/21_input.txt'


class Board():
    def __init__(self, size = 10):
        self.size = 10
        self.spaces = {}
        pr = None
        nx = None
        for i in range(1, size+1):
            self.spaces[i] = Space(i, prev=pr, nxt=nx)
            if pr is not None:
                self.spaces[i].previous.next = self.spaces[i]
            else:
                firstSpace = self.spaces[i]
            pr = self.spaces[i]
        firstSpace.previous = pr
        firstSpace.previous.next = firstSpace
    
    def jump(self, space, step):
        nx = space
        for i in range(step):
            nx = nx.next
        return nx




class Space():
    def __init__(self, nr, prev = None, nxt = None):
        self.nr = nr
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

def day21PartOne():
#    inp = file2List(inputFile)
    b = Board(size=10)
    dice = random.randint(1,100) +random.randint(1,100) +random.randint(1,100)
    l = list(range(1,101))
    dice100 = itertools.cycle(l)
    def rollDice():
        return dice100.__next__() + dice100.__next__() + dice100.__next__()
    

    # Player 1 starting position: 8
    # Player 2 starting position: 5
    player1 = b.spaces[8]
    p1c = 0
    player2 = b.spaces[5]
    p2c = 0
    rolled = 0

    while True:
        pd = rollDice()
        rolled += 3
        player1 = b.jump(player1, pd)
        p1c += player1.nr
        if p1c >= 1000: 
            output = rolled * p2c
            break

        pd = rollDice()
        rolled += 3
        player2 = b.jump(player2, pd)
        p2c += player2.nr
        if p2c >= 1000: 
            output = rolled * p1c
            break
    


    #output = "WIP"
    print(f'# Solution Day 21, Part one:\n# Answer: {output} \n\n')


def day21PartTwo():
    #inp = file2List(inputFile)
    output = "WIP"
    
    print(f'# Solution Day 21, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day21PartOne()
    day21PartTwo()





# Run from terminal:
# $ python day_21.py