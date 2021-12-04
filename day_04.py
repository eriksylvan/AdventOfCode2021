# https://adventofcode.com/2021/day/4



inputFile = 'input/04_input'

class Bingo(object):
    def __init__(self, b):
        self.board = b
        self.marked = [[False]*5 for n in range(5)]
        
    def play(self, num):
        r=0
        c=0
        for row in self.board:
            c=0
            for n in row:
                if n == num:
                    self.marked[r][c]=True
                    break 
                c+=1
            r+=1
    
    def score(self, num):
        sum=0
        for r in range(5):
            for c in range(5):
                if not self.marked[r][c]:
                    sum += self.board[r][c]   
        return sum * num 
                
            
    def check(self):
        # Check for bingo in rows:
        for r in range(5):
            if sum(self.marked[r])==5:
                return True
        # Check for bingo in columns:
        for c in range(5):
            if sum([self.marked[0][c],self.marked[1][c],self.marked[2][c],self.marked[3][c],self.marked[4][c]])==5:
                return True
        # Check for bingo in diagonals:
        # if sum([self.marked[0][0],self.marked[1][1],self.marked[2][2],self.marked[3][3],self.marked[4][4]])==5:
        #     return True
        # if sum([self.marked[0][4],self.marked[1][3],self.marked[2][2],self.marked[3][1],self.marked[4][0]])==5:
        #     return True
        
        #Bingo not found, return False
        return False       
        

def readBingoFile(file):
    '''
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    bingoNumbers = []
    bingoBords = []
    with open(file) as input:
        numrow = input.readline()
        bingoNumbers = [int(a) for a in numrow.strip().split(',')]
        for line in input:
            if line == "\n":
                board = []
                bingoBords.append(board)
            else:
                board.append([int(a) for a in line.strip().split()])
    return (bingoNumbers,bingoBords )

def playBingo(bingonumbers, boards):
    bingo = False
    for n in bingonumbers:
        if bingo: break
        for b in boards:
            if bingo: break
            b.play(n)
            if b.check():
                score = b.score(n)
                bingo = True
    return score  

def playBingoLastScore(bingonumbers, bb):

    boards=[]
    for b in bb:
        boards.append([b,True])  #[0] = the board [1]=still in play
    
    for n in bingonumbers:
        for b in boards:
            if b[1]: # if still in play
                b[0].play(n)
                if b[0].check():
                    score = b[0].score(n)
                    b[1]= False # set the bord not in play
    return score  

def day04PartOne():
    bingonumbers, bingoBoardsInt = readBingoFile(inputFile)
    boards=[]
    for b in bingoBoardsInt:
        boards.append(Bingo(b)) 
    
    output = playBingo(bingonumbers, boards)

    print(f'# Solution Day 02, Part one:\n# Answer: {output} \n\n')


def day04PartTwo():
    bingonumbers, bingoBoardsInt = readBingoFile(inputFile)
    boards=[]
    for b in bingoBoardsInt:
        boards.append(Bingo(b))
                    
    output = playBingoLastScore(bingonumbers, boards)
    print(
        f'# Solution Day 02, Part two:\n# Answer: {output} \n\n')


if __name__ == "__main__":
    day04PartOne()
    day04PartTwo()


# Solution Day 02, Part one:
# Answer: 28082 


# Solution Day 02, Part two:
# Answer: 8224 

# Run from terminal:
# $ python day_04.py