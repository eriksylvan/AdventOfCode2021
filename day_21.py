# https://adventofcode.com/2021/day/21
import random
import itertools


# Part 1
# linked list: Not nesesary... I thought I was smart and prepared for part 2. Liked list is not helping in part 2.
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



# Part 2

# inspired by https://github.com/Fadi88/AoC/blob/master/2021/day21/code.py

# Possible sum of 3 dises with 3 sides: 3, 4, 5, 6, 7, 8, 9
# e.g (1+1+1), (1,1,2), (1,1,3), (1,2,1) ...
# all combinations of [1,2,3] times 3 is given by iteritem.product([1, 2, 3], repeat=3)
# the series can look like this
# 3,4,5,4,5,6,5,6,7,4,5,6,5,6,7,6,7,8,5,6,7,6,7,8,7,8,9
# 

def playPart2(pos1, pos2, score1=0, score2=0, playerturn=0, knownResults={}):
    '''
    Returns number of wins for [player1, player 2] for the given positions scora, and playerturn
    '''

    # knownResults is a case holding all results for a known input
    # player = 0 => first player
    # player = 1 => second player

    if (pos1, pos2, score1, score2, playerturn) in knownResults:
        return knownResults[(pos1, pos2, score1, score2, playerturn)]

    wins = [0, 0] # countiung all wins for player1 and player2
    rolls = [r1 + r2 + r3 for r1, r2, r3 in itertools.product([1, 2, 3], repeat=3)] #returning all pussible outcome of three dises rolling

    for r in rolls:
        pos = [pos1, pos2]
        score = [score1, score2]

        pos[playerturn] = (pos[playerturn] + r - 1) % 10 + 1    # New position for player after moving acorfing to dice roll
        score[playerturn] += pos[playerturn]                    # New score for player after moving acorfing to dice roll

        if score[playerturn] >= 21:     # we have a winner!!!
            wins[playerturn] += 1
        else:
            # no winner, continue play with next player (deeper in the paralell universe... recursively)
            w1, w2 = playPart2(pos[0], pos[1], score[0], score[1], 1 if playerturn == 0 else 0, knownResults)
            wins[0] += w1
            wins[1] += w2

    # Save nober of wins in cache and return wins
    knownResults[(pos1, pos2, score1, score2, playerturn)] = wins
    
    return wins 



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
    player1 = 8
    player2 = 5
    wins = playPart2(player1, player2)
    # Pussle answer is maximum number of wins
    output = max(wins)
    
        
    print(f'# Solution Day 21, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day21PartOne()
    day21PartTwo()





# Run from terminal:
# $ python day_21.py