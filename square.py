import math
s=input('write your figure ')
if s=='circle':
    r=int(input('write radius '))
    print(math.pi*r*r)
elif s=='triangle':
    a= int(input('write a '))
    b = int(input('write b '))
    c = int(input('write c '))
    p=(a+b+c)/2
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
elif s=='rectangle':
    a = int(input('write a '))
    b = int(input('write b '))
    print(a*b)