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
    day_12.findCavePath()
    assert output == 6
  
def test_buildGraph2():
    gr = day_12.readMap(map2)
    output = len(gr)
    g = day_12.findCavePath()
    assert output == 7

# Run tests from terminal:
# $ pytest test/test_day_12.py 