import pytest
import day_05
    
testInput = ['0,9 -> 5,9',
'8,0 -> 0,8',
'9,4 -> 3,4',
'2,2 -> 2,1',
'7,0 -> 7,4',
'6,4 -> 2,0',
'0,9 -> 2,9',
'3,4 -> 1,4',
'0,0 -> 8,8',
'5,5 -> 8,2']

def test_readVect():
    output = day_05.readVect(testInput)
    assert output[9]==[5,5,8,2]

def test_plotVectOverlaps():
    v = day_05.readVect(testInput)
    o = day_05.plotVect(v)
    assert len(o) == 21
    assert day_05.findOverlaps(o) == 5
    
def test_plotVectOverlapsVithDiagonals():
    v = day_05.readVect(testInput)
    o = day_05.plotVect(v,diag=True)
    assert len(o) == 39
    assert day_05.findOverlaps(o) == 12
    


# Run tests from terminal:
# $ pytest test/test_day_05.py 