#import pytest
import day_25

inp = ["v...>>.vv>",
".vv>>.vv..",
">>.>v>...v",
">>v>>.>.v.",
"v>v.vv.v..",
">.>>..v...",
".vv..>.>v.",
"v.v..>>v.v",
"....v..v.>"]


def test_seaCucumber():
    o = day_25.seaCucumber(inp)
    assert True



# Run tests from terminal:
# $ pytest test/test_day_25.py s