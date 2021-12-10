import pytest
import day_09
    
    
heatmap = ["2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678"]

extendedHeatmap = ["999999999999",
"921999432109",
"939878949219",
"998567898929",
"987678967899",
"998999656789",
"999999999999"]

def test_extendHeatMap():
    assert day_09.extendHeatmap(heatmap) == extendedHeatmap

def test_riskLevel():
    localMin = day_09.findLocalMin(heatmap)
    output = sum(localMin.values()) + len(localMin)
    assert output == 15

def test_findBasinSize():
    exhm = day_09.extendHeatmap(heatmap)
    visited=[]
    output = day_09.basinSize(2,1,0,visited,exhm)
    assert output == 3

def test_findBasinSize2():
    exhm = day_09.extendHeatmap(heatmap)
    visited=[]
    output = day_09.basinSize(10,1,0,visited,exhm)
    assert output == 9

def test_find3LargestBasinSize():
    localMin = day_09.findLocalMin(heatmap)
    output = day_09.find3LargestBasinSize(heatmap)
    assert output == [14, 9, 9]
    
# Run tests from terminal:
# $ pytest test/test_day_08.py 