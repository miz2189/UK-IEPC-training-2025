import math
 
x = 0 
num = int(input())
 
while num >=  2**x:
    x += 1
 
 
num = math.ceil(math.log(x,2))
if 2**num == 1:
    print(2**num, "bit")
else:
    print(2**num, "bits")