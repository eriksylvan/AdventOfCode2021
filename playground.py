s1="AC"
s2="ac"
s3="Ac"
s4="cc"
print(s1.isupper())
print(s2.isupper())
print(s3.isupper())
print(s4.isupper())
print(s4.islower())





# i=range(9)
# print([t<5 for t in i])
# print(sum(t<5 for t in i))

inp = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

output0 = [0,0,0,0,0]
output1 = [0,0,0,0,0]

#print([r[4]=='1' for r in inp])

for r in inp:
    for i, ch in zip(range(5), r):
        output0[i]+=int(ch)
        
        
l = len(inp)
o1 = ['1' if i>=6 else '0' for i in output0]
o0 = ['0' if i>=6 else '1' for i in output0]
b1=''.join(map(str,o1))
b0=''.join(map(str,o0))
r1 = int(b1,2)
r2 = int(b0,2)
print(r1*r2)

print(sum([True,True,True]))
print(sum([True,True,False]))

print('101010',int('101010',2))

import parse
string = "shiny gold bags contain 2 dark red bags."
pattern = "{outer_color} bags contain {num:d} {inner_color} bags."
match = parse.search(pattern, string)
print(match)