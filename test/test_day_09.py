import pytest
import day_09
    
    
heatmap = ["2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678"]


def test_riskLevel():
    output = day_09.riskLevel(heatmap)
    assert output == 15
    


# Run tests from terminal:
# $ pytest test/test_day_08.py 