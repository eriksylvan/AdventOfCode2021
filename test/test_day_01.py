import pytest
import day_01
    
def test_depthCounter():
    assert day_01.depthIncreaseCounter([199,200,208,210,200,207,240,269,260,263]) == 7

def test_depthCounterSlidingWindow_1():
    assert day_01.depthIncreaseCounterSlidingWindow([199,200,208,210,200,207,240,269,260,263]) == 5

def test_depthCounterSlidingWindow_2():
    assert day_01.depthIncreaseCounterSlidingWindow([1,1,1,2,1,1,1]) == 1


# Run tests from terminal:
# $ pytest test/test_day_01.py 