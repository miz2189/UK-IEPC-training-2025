dict = {"B":2,"A":1,"D":1,"O":1,"P":1,"Q":1,"R":1}

colour1 = input()
colour2 = input()
len1 = len(colour1)
len2 = len(colour2)

picture = []
for i in range (5):
    array = []
    for i in range (len1*len2 + len1 -1):
        array.append(".")
    picture.append(array)



for i in range (len1):
    letter = colour1[i]
    holes = dict.get(letter,0)
    leftx = (len2+1)*i

    if holes == 2:

        for x in picture:
            x[leftx] = "X"
            x[leftx+len2-1] = "X"
        
        for y in range (leftx,leftx+len2-1):
            picture[0][y] = "X"
            picture[2][y] = "X"
    
    if holes == 1:
        for q in picture:
            q[leftx] = "X"
            q[leftx+len2-1] = "X"
        
        for y in range (leftx,leftx+len2-1):
            picture[0][y] = "X"
    
    if holes == 0:
        for x in picture:
            x[leftx] = "X"

count=0
for i in range (len1*len2 + len1 -1):
    if (i%(len2+1)) != len2:
        picture[4][i] = colour2[count%len2]
        count = count +1




line1= ""
line2 =""
line3=""
line4=""
line5=""

for a in picture[0]:
    line1 += a
for a in picture[1]:
    line2 += a
for a in picture[2]:
    line3 += a
for a in picture[3]:
    line4 += a
for a in picture[4]:
    line5 += a


print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
