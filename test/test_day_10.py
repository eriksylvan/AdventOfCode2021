import pytest
import day_10
    
    
chunk = ["[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"]

@pytest.mark.parametrize("test_input, test_output",
                         [('[({(<(())[]>[[{[]{<()<>>','ok'), 
                         ('{([(<{}[<>[]}>{[]{[(<()>','}'), 
                         ('[{[{({}]{}}([{[{{{}}([]',']'), 
                         ('[<(<(<(<{}))><([]([]()',')'), 
                         ('<{([([[(<>()){}]>(<<{{','>')]
                         )
def test_chunk(test_input, test_output):
    (o, stack) = day_10.stackThe(test_input) 
    assert o == test_output
    
def test_subsystem():
    assert day_10.checkers(chunk)  == 26397
     

def test_leftovers():
    assert day_10.leftovers(chunk)  == 288957

    
# Run tests from terminal:
# $ pytest test/test_day_10.py 