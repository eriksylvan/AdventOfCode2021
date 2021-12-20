# https://adventofcode.com/2021/day/20


inputFile = 'input/20_input'


def file2List(file):
    '''Reads file, returs list of string
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list2 = []
    list = []
    
    with open(file) as input:
        for line in input:
            if line=='\n':
                break
            list.append(line.strip())
        for line in input:
            list2.append(line.strip())
    
    return list, list2



def readPicture(pic):
    o = 100 #offset
    pixels = {}
    yl = len(pic);  xl = len(pic[0])
    for y, row in enumerate(yl):
        for x, p in  enumerate(xl):
            pixels[(x,y)] = p
            
    return pixels

def extendPicture00(pic):
    extraRow = '.'*(len(pic[0])+4)
    ePic = [extraRow,extraRow]
    for row in pic:
        ePic.append('..' + row + '..')
    ePic.append(extraRow)
    ePic.append(extraRow)
    return ePic

def extendPicture11(pic):
    extraRow = '#'*(len(pic[0])+4)
    ePic = [extraRow,extraRow]
    for row in pic:
        ePic.append('##' + row + '##')
    ePic.append(extraRow)
    ePic.append(extraRow)
    return ePic


            
def printPicture(pic):
    for row in pic:
        print(row)

def enhancePicture2(pic, enh):
    for y, row in enumerate(pic[1:-1]):
        for x, pix in enumerate(row[1:-1]):
            if pix == '.':
                print(' ', end='')
            else: 
                print('#', end='')
        print()
   
        
def enhancePicture(pic, enh):
    enhPic = []
    #pic = extendPicture00(pic)
    for y, row in enumerate(pic[1:-1],1):
        enhRow = ''
        for x, pix in enumerate(row[1:-1],1):
            word = pic[y-1][x-1:x+2] + pic[y][x-1:x+2] + pic[y+1][x-1:x+2]
            idx = int(str(word).replace('.','0').replace('#','1'),2)
            enhRow = enhRow + enh[0][idx]
        enhPic.append(enhRow)
    return enhPic.copy()

def countPixels(pic):
    count = 0
    for row in pic:
        for pixel in row:
            if pixel =='#':
                count +=1
    return count
    

def day20PartOne():
    inp, pic = file2List(inputFile)
    
    print(len(inp[0]))
    printPicture(pic)
    print(f'\n\n')
    print(len(pic), len(pic[0]))
    print(f'\n\n')
    pic = extendPicture00(pic)
    enhPic = enhancePicture(pic, inp)
    printPicture(enhPic)
    print(f'\n\n')
    print(len(enhPic), len(enhPic[0]))
    print(f'\n\n')

    enhPic = extendPicture11(enhPic)
    enhPic2 = enhancePicture(enhPic, inp)
    output = countPixels(enhPic2)
    printPicture(enhPic2)
    print(f'\n\n')
    print(len(enhPic2), len(enhPic2[0]))
    print(f'\n\n')

    print(f'# Solution Day 20, Part one:\n# Answer: {output} \n\n')


def day20PartTwo():
    inp, pic= file2List(inputFile)
    
    for i in range(25):
        pic = extendPicture00(pic)
        pic = enhancePicture(pic, inp)
        pic = extendPicture11(pic)
        pic = enhancePicture(pic, inp)
    
    
    output = countPixels(pic)
    printPicture(pic)
    print(f'\n\n')
    print(len(pic), len(pic[0]))
    print(f'\n\n')
    
    print(f'# Solution Day 20, Part two:\n# Answer: {output} \n\n')
    


if __name__ == "__main__":
    day20PartOne()
    day20PartTwo()




# Run from terminal:
# $ python day_20.py