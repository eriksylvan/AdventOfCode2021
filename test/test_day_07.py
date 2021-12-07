import pytest
import day_07
    
    
crabs = [16,1,2,0,4,2,7,1,2,14]


def test_optimalHeigt():
    output = day_07.optimalHeigt(crabs)
    assert output == 2
    


def test_fuel():
    output = day_07.fuel(crabs, 2)
    assert output == 37


def test_optimalHeigt2():
    output = day_07.optimalHeigt2(crabs)
    assert output == 5
    
@pytest.mark.parametrize("i, o", [(5,168), (2,206)])
def test_fuel2(i, o):
    output = day_07.fuel2(crabs, i)
    assert output == o

# Run tests from terminal:
# $ pytest test/test_day_07.py 