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

def test_powerConsumption():
    assert day_03.calcge(testInput) == 198


def test_lifeSupportRating():
    assert day_03.calcLife(testInput) == 230


# Run tests from terminal:
# $ pytest test/test_day_03.py 