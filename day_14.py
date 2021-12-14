# https://adventofcode.com/2021/day/14


inputFile = 'input/14_input.txt'


class Polymer():
    def __init__(self,letter, prev = None, nxt = None):
        self.letter = letter
        self.previous = prev
        self.next = nxt

def file2List(file):
    '''Reads file, returs list of string
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

def initPolymer(template):
    prev = None
    nxt = None
    poly = None
    for ch in template:
        p = Polymer(ch,prev,nxt)
        if poly is None:
            poly = p
        if prev is not None:
            prev.next = p
        prev = p
    return poly    


def pairInsertion(pol, step, pairInsertions):
    
    startPol = pol  
    for s in range(step):
        print(f"Step: {s}")
        pol = startPol
        while pol.next is not None:
            pair = pol.letter + pol.next.letter
            ins = pairInsertions[pair]
            newP = Polymer(ins, pol, pol.next)
            #polyList.append(newP)
            pol.next = newP
            newP.next.previous = newP
            pol = newP.next
    return startPol         

def countLetters(startPol):
    pol = startPol
    count = {}
    end = False
    while not end:
        if pol.letter in count:
            count[pol.letter] += 1
        else:
            count[pol.letter] = 1
        if pol.next is not None:
            pol = pol.next
        else:
            end = True
    return count
            
def readInstructions(instr):
    template = instr[0]
    pairInsertions = {}
    for p in instr[2:]:
        sp = p.split(" -> ")
        pairInsertions[sp[0]]=sp[1]
    return template, pairInsertions
        
########################################
#  Part 2
########################################    
'''
Fisrt attempt took to long time
Second solution works better 

Every letter pair will result in two new letter pair, ex NN -> [NC, CN] after each step
buildPolyPair creates a dictionary that gives thw two new pairs

for every step
    for every letter pair in the polymer
        generate new letter pairs and count the new single letters


'''


def buildPolyPair(pairInsertions):
    polyPair = {}
    for pi in pairInsertions:
        a = pi[0]
        b = pairInsertions[pi]
        c = pi[1]
        
        polyPair[pi] = [a+b, b+c]
        
    return polyPair

def step(template, s, pairInsertions):
    pair_counter = {}
    pp = buildPolyPair(pairInsertions)
    chCount= {}
    for ch in template:
        if ch in chCount:
            chCount[ch]+=1
        else:
            chCount[ch]=1
    
    for i in range(len(template)-1):
        ch1 = template[i]
        ch2 = template[i+1]
        if ch1+ch2 in pair_counter:
            pair_counter[ch1+ch2] +=1
        else:
            pair_counter[ch1+ch2] =1
        
    
    for s in range(s):
        nextStep = {}
        for pair in pair_counter:
            noOfPair = pair_counter[pair]
            if pairInsertions[pair] in chCount:
                chCount[pairInsertions[pair]] += noOfPair
            else:
                chCount[pairInsertions[pair]] = noOfPair
            p0 = pp[pair][0]
            p1 = pp[pair][1]
            if p0 in nextStep:
                nextStep[p0] += noOfPair
            else:
                nextStep[p0] = noOfPair
            if p1 in nextStep:                
                nextStep[p1] += noOfPair
            else:
                nextStep[p1] = noOfPair
        pair_counter = nextStep.copy()
    
    return chCount



def polyCount(template, pairs, pair_counter, steps = 1):
    '''Return number of polymer
    '''
    # Only keep track of the number of pairs in each steps
    
    
    for i in range(len(template)-1):
        ch1 = template[i]
        ch2 = template[i+1]
        if ch1+ch2 in pair_counter:
            pair_counter[ch1+ch2] +=1
        else:
            pair_counter[ch1+ch2] =1
    return pair_counter



def buildDict(template, pairInsertions):
    for i in range(len(template)):
        ch1 = template[i]
        ch2 = template[i+1]
        pol = initPolymer(ch1+ch2)
        firstPoly = pairInsertion(firstPoly, 20, pairInsertions)

                
def day14PartOne():
    inp = file2List(inputFile)
    template, pairInsertions = readInstructions(inp)
    firstPoly = initPolymer(template)
    firstPoly = pairInsertion(firstPoly, 10, pairInsertions)
    c = countLetters(firstPoly)
    maximum = max(c, key=c.get) 
    minimum = min(c, key=c.get) 
    output = c[maximum] - c[minimum]
    print(f'# Solution Day 14, Part one:\n# Answer: {output} \n\n')


def day14PartTwo():
    inp = file2List(inputFile)
    t, p = readInstructions(inp)
    c = step(t, 40, p)
    maximum = max(c, key=c.get) 
    minimum = min(c, key=c.get) 
    output = c[maximum] - c[minimum]
    
    print(f'# Solution Day 14, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day14PartOne()
    day14PartTwo()




# Run from terminal:
# $ python day_12.py