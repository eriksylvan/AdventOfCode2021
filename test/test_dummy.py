import pytest
import dummy_day
    
def test_dummy_01():
    assert dummy_day.dummy(1) == 2
        
def test_dummy_02():
    assert dummy_day.summy([1,2,3]) == 6

@pytest.mark.parametrize("test_input, expected_result", [([10,10,10],30), ([10,20,30],60), ([10,-10,10],10), ([1,1,1,1,1,1,-8],-2)])
def test_dummy_03(test_input, expected_result):
    assert dummy_day.summy(test_input) == expected_result
    

# Run tests from terminal:
# $ pytest test/test_dummy.py 