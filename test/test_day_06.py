import pytest
import day_06
    
fish = [3,4,3,1,2]

@pytest.mark.parametrize("test_input, expected_result", [(1,5), (18,26), (80,5934)])
def test_Reporduce(test_input, expected_result):
    output = day_06.Reporduce(fish,test_input)
    print(output)
    assert len(output) == expected_result
    

@pytest.mark.parametrize("test_input, expected_result", [(1,5), (18,26), (80,5934), (256, 26984457539)])
def test_Reporduce2(test_input, expected_result):
    output = day_06.Reporduce2(fish,test_input)
    print(output)
    assert output == expected_result


# Run tests from terminal:
# $ pytest test/test_day_05.py 