import pytest
import day_11
    
    
octGrid = ["5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526"]

octGridSmall = ["11111",
"19991",
"19191",
"19991",
"11111"]

def test_octSmall():
    octM = day_11.octopusMatrix(octGridSmall)
    output, step = day_11.flashCount(octM,2) 
    
    assert output == 9
  
@pytest.mark.parametrize("i, o", [(10,204), (100,1656)]  )
def test_oct(i, o):
    octM = day_11.octopusMatrix(octGrid)
    count, step = day_11.flashCount(octM,i) 
    
    assert count == o
  
@pytest.mark.parametrize("i, o", [(-1,195)])
def test_oct_sync(i, o):
    octM = day_11.octopusMatrix(octGrid)
    count,step = day_11.flashCount(octM,-1, findsync=True) 
    
    assert step == step
  

    
# Run tests from terminal:
# $ pytest test/test_day_11.py 