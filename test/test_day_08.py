import pytest
import day_08
    
    
inputFile = "input/test_08_input"


def test_input_file():
    l = day_08.file2List(inputFile)
    inputList, outputList = day_08.readVect(l)
    assert len(inputList) == 10
    assert inputList[0][0] == 'be'
    assert outputList[9][3] == 'bagce'

def test_countEasy():
    l = day_08.file2List(inputFile)
    inputList, outputList = day_08.readVect(l)
    assert day_08.countEasy(outputList) == 26
    

# Run tests from terminal:
# $ pytest test/test_day_08.py 