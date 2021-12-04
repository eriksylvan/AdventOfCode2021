import pytest
import day_03
    
testInput = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

def test_runSubTryOne():
    assert day_03.calcge(testInput) == 198





# Run tests from terminal:
# $ pytest test/test_day_02.py 