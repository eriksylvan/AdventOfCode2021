# https://adventofcode.com/2021/day/10



inputFile = 'input/10_input'
score = {'ok': 0,
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4}

def file2List(file):
    '''Reads file, returs list of lines
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list = []
    with open(file) as input:
        for line in input:
            list.append(line.strip())
    return list

def stackThe(inp):
    opn = {'(':0,'[':1,'{':2,'<':3}
    clo = {')':0,']':1,'}':2,'>':3}

    stack = []
    cnt = 0


    while cnt < len(inp):
        ch = inp[cnt]
        if ch in opn.keys():
            stack.append(ch) 
        elif ch in clo.keys():
            if opn[stack.pop()] == clo[ch]:
                #ok
                
                pass
            else:
                return (ch, stack)
        else:
            assert False
        cnt+=1
    # Everython OK
    return ('ok', stack)

def checkers(chunks):
    points = 0
    for chunk in chunks:
        (ch, stack) = stackThe(chunk)
        points += score[ch]
    
    return points

    
        
def leftovers(chunks):
    scores = []
    for chunk in chunks:
        (ch, stack) = stackThe(chunk)    
        if ch == 'ok':
            sc = 0
            for s in stack[::-1]:
               sc = sc * 5 + score[s]  
            scores.append(sc)
    scores.sort()
    ll= len(scores)-1/2
    return scores[int(len(scores)/2)]
        
            
    
                
def day10PartOne():
    input = file2List(inputFile)
    output = checkers(input)
           
    print(f'# Solution Day 10, Part one:\n# Answer: {output} \n\n')


def day10PartTwo():
    input = file2List(inputFile)
    output = leftovers(input)
    
    print(f'# Solution Day 10, Part two:\n# Answer: {output} \n\n')



if __name__ == "__main__":
    day10PartOne()
    day10PartTwo()

# Solution Day 10, Part one:
# Answer: 167379 


# Solution Day 10, Part two:
# Answer: 2776842859 

# Run from terminal:
# $ python day_10.py