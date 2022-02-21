s=input('Write your first line ')
print(len(s))
a=s.find(' ',0, len(s) )
b=s.rfind(' ',0, len(s) )

print(s[0:a]+'; '+s[b:len(s)])