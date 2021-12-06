import pytest
import day_06
    
testInput = [3,4,3,1,2]

def test_Reporduce():
    output = day_06.Reporduce(testInput,18)
    print(output)
    assert len(output) == 26
    


    


# Run tests from terminal:
# $ pytest test/test_day_05.py 