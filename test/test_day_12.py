import pytest
import day_12
    
    
map1 = ["start-A",
"start-b",
"A-c",
"A-b",
"b-d",
"A-end",
"b-end"]

map2 = ["dc-end",
"HN-start",
"start-kj",
"dc-start",
"dc-HN",
"LN-dc",
"HN-end",
"kj-sa",
"kj-HN",
"kj-dc"]


def test_buildGraph():
    gr = day_12.readMap(map1)
    output = len(gr)
    assert output == 6


def test_findNumberOfPath1():
    gr = day_12.readMap(map1)
    numberOfPath = day_12.findCavePath(gr)
    assert  len(numberOfPath) == 10
  
def test_findNumberOfPath2():
    gr = day_12.readMap(map2)
    numberOfPath = day_12.findCavePath(gr)
    assert  len(numberOfPath) == 19

def test_findNumberOfPathTwiceSmall1():
    gr = day_12.readMap(map1)
    numberOfPath = day_12.findCavePath(gr, singleSmallCaveTwice=True)
    assert  len(numberOfPath) == 36
  
def test_findNumberOfPathTwiceSmall12():
    gr = day_12.readMap(map2)
    numberOfPath = day_12.findCavePath(gr, singleSmallCaveTwice=True)
    assert  len(numberOfPath) == 103

# Run tests from terminal:
# $ pytest test/test_day_12.py 