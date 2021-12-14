import pytest
from day_06 import day06PartTwo
import day_14

inp=["NNCB",
"",
"CH -> B",
"HH -> N",
"CB -> H",
"NH -> C",
"HB -> C",
"HC -> B",
"HN -> C",
"NN -> C",
"BH -> H",
"NC -> B",
"NB -> B",
"BN -> B",
"BB -> N",
"BC -> B",
"CC -> N",
"CN -> C"]



def test_readInstructions():
    t, p = day_14.readInstructions(inp)
    assert t == "NNCB"
    assert len(p) == 16
    assert p["CC"] == "N"


def test_initPolymer():
    t, p = day_14.readInstructions(inp)
    poly = day_14.initPolymer(t)
    assert poly.next.next.next.letter == "B"

def test_pairInsertion():
    t, p = day_14.readInstructions(inp)
    poly = day_14.initPolymer(t)
    firstPoly = day_14.pairInsertion(poly, 1, p)
    assert firstPoly.letter == "N"


def test_countLetters():
    t, p = day_14.readInstructions(inp)
    poly = day_14.initPolymer(t)
    firstPoly = day_14.pairInsertion(poly, 1, p)
    c = day_14.countLetters(firstPoly)
    assert sum(c.values()) == 7
    maximum = max(c, key=c.get) 
    assert maximum =='N'
    assert c[maximum] == 2
    
    
def test_countLetters_10steps():
    t, p = day_14.readInstructions(inp)
    poly = day_14.initPolymer(t)
    firstPoly = day_14.pairInsertion(poly, 10, p)
    c = day_14.countLetters(firstPoly)
    assert sum(c.values()) == 3073
    maximum = max(c, key=c.get) 
    assert maximum =='B'
    assert c[maximum] == 1749
    minimum = min(c, key=c.get) 
    assert minimum =='H'
    assert c[minimum] == 161
    

@pytest.mark.skip(reason="takes to long time")    
def test_countLetters_40steps():
    t, p = day_14.readInstructions(inp)
    poly = day_14.initPolymer(t)
    firstPoly = day_14.pairInsertion(poly, 40, p)
    c = day_14.countLetters(firstPoly)
    maximum = max(c, key=c.get) 
    assert maximum =='B'
    assert c[maximum] == 2192039569602
    minimum = min(c, key=c.get) 
    assert minimum =='H'
    assert c[minimum] == 3849876073    


def test_polyCount():
    t, p = day_14.readInstructions(inp)
    pairs = {}
    pair_counter = {}
    c = day_14.polyCount(t, pairs, pair_counter, 10)
    assert len(c) == 3

def test_buildPolyPair():
    t, p = day_14.readInstructions(inp)
    pp = day_14.buildPolyPair(p)
    assert len(pp) == 16

def test_step_1():
    t, p = day_14.readInstructions(inp)
    result = day_14.step(t, 1, p)
    assert result['N'] == 2
    assert result['C'] == 2
    assert result['B'] == 2
    assert result['H'] == 1

def test_step_2():
    t, p = day_14.readInstructions(inp)
    result = day_14.step(t, 2, p)
    assert result['N'] == 2
    assert result['C'] == 4
    assert result['B'] == 6
    assert result['H'] == 1

def test_step_40():
    t, p = day_14.readInstructions(inp)
    result = day_14.step(t, 40, p)
    assert result['B'] == 2192039569602
    assert result['H'] == 3849876073

# Run tests from terminal:
# $ pytest test/test_day_13.py 