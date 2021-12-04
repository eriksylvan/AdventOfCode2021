import pytest
import day_02
    
testInput = [['forward', '5'],['down', '5'],['forward', '8'],['up', '3'],['down', '8'],['forward', '2']]

def test_runSubTryOne():
    assert day_02.runSubTryOne(testInput) == 150

def test_runSubTryTwo():
    assert day_02.runSubTryTwo(testInput) == 900



# Run tests from terminal:
# $ pytest test/test_day_02.py 