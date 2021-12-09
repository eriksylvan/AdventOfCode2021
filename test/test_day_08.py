import pytest
import day_08
    
    
inputFile = "input/test_08_input"


def test_input_file():
    l = day_08.file2List(inputFile)
    inputList, outputList = day_08.readDigitData(l)
    assert len(inputList) == 10
    assert inputList[0][0] == 'be'
    assert outputList[9][3] == 'bagce'

def test_countEasy():
    l = day_08.file2List(inputFile)
    inputList, outputList = day_08.readDigitData(l)
    assert day_08.countEasy(outputList) == 26

def test_isDigit_3():
    d = day_08.getDigit('abcdg', ('a', 'b', 'c', 'd', 'e', 'f', 'g'))
    assert d == 3

@pytest.mark.parametrize("test_input, test_output", [('acedgfb',8), ('cdfbe',5), ('gcdfa',2), ('fbcad',3), ('dab',7), ('cefabd',9), ('cdfgeb',6), ('eafb',4), ('cagedb',0), ('ab',1)])
def test_getDigit(test_input, test_output):
    d = day_08.getDigit(test_input, ('d', 'a', 'b', 'c', 'g', 'e', 'f'))
    assert d == test_output

def test_getDigit_Unvalid():
    d = day_08.getDigit('adefg', ('a', 'b', 'c', 'd', 'e', 'f', 'g'))
    assert d == -1

def test_findWieringPattern():
    digits = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    d = day_08.findWieringPattern(digits)
    assert ''.join(d) == 'dabcgef'

def test_getSumFromExample():
    input = day_08.file2List(inputFile)
    inp,out = day_08.readDigitData(input)
    values = []
    for i in range(len(input)):
        values.append(day_08.decodeOutputValue(inp[i],out[i]))
    output = sum(values)
    assert output == 61229
    
# Run tests from terminal:
# $ pytest test/test_day_08.py 

