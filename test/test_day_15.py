import pytest
import day_15
import day_15_2

inp1=["1163751742",
"1381373672",
"2136511328",
"3694931569",
"7463417111",
"1319128137",
"1359912421",
"3125421639",
"1293138521",
"2311944581"]

inp2=["222",
"112",
"213"]
# risk =6
inp3=["19999",
"19121",
"19191",
"12291",
"99991"]

def test_findPath1():
    risk, path = day_15.enterCave(inp1)
    assert risk==40

def test_findPath2():
    risk, path = day_15.enterCave(inp2)
    assert risk==6
    

def test_findPath3():
    risk, path = day_15.enterCave(inp3)
    assert risk==15
    
    
def test_findMyWay():
    risk = day_15_2.findMyWay(inp2)
    assert risk ==6


def test_findMyWay2():
    risk = day_15_2.findMyWay(inp1)
    assert risk == 40
    
def test_findMyWay3():
    risk = day_15_2.findMyWay(inp3)
    assert risk == 15
    
    
def test_findMyWay4():
    inputFile = "input/test_15_input"
    inp = day_15_2.file2List(inputFile)
    risk = day_15_2.findMyWay(inp)
    assert risk == 315

# Run tests from terminal:
# $ pytest test/test_day_15.py s