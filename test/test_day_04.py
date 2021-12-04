import pytest
import day_04




def test_readFile():
    inputFile = 'input/test_04_input'
    out, out2 = (day_04.readBingoFile(inputFile))
    assert out == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    assert len(out2) == 3
    assert len(out2[0]) == 5
    assert len(out2[0][0]) == 5

def test_playBingo():
    inputFile = 'input/test_04_input'
    bingonumbers, bingoBoardsInt = day_04.readBingoFile(inputFile)
    boards=[]
    for b in bingoBoardsInt:
        boards.append(day_04.Bingo(b)) 

    output = day_04.playBingo(bingonumbers, boards)
    assert output == 4512

def test_playBingoLastScore():
    inputFile = 'input/test_04_input'
    bingonumbers, bingoBoardsInt = day_04.readBingoFile(inputFile)
    boards=[]
    for b in bingoBoardsInt:
        boards.append(day_04.Bingo(b)) 

    output = day_04.playBingoLastScore(bingonumbers, boards)
    assert output == 1924


# Run tests from terminal:
# $ pytest test/test_day_02.py 