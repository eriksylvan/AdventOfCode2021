import pytest
import day_13

inp=["6,10",
"0,14",
"9,10",
"0,3",
"10,4",
"4,11",
"6,0",
"6,12",
"4,1",
"0,13",
"10,12",
"3,4",
"3,0",
"8,4",
"1,10",
"2,14",
"8,10",
"9,0",
"",
"fold along y=7",
"fold along x=5"]

m=[[1,0,0],[1,0,1],[0,0,1]]


def test_PaperLayout():
    paper = day_13.getPaperLayout(inp)
    assert len(paper) == 15
    assert len(paper[0]) == 11

def test_FoldingInstructions():
    folding = day_13.getFoldingInstructions(inp)
    assert len(folding) == 2
    assert len(folding[0]) == 2

def test_fold():
    paper = day_13.getPaperLayout(inp)
    folded = day_13.fold(paper, 7, 'y')
    assert sum(sum(folded)) == 17
    folded = day_13.fold(folded, 5, 'x')
    assert sum(sum(folded)) == 16

# Run tests from terminal:
# $ pytest test/test_day_13.py 