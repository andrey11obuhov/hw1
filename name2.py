s=input('Write your name ')
if len(s)<5:
    d=input('Write your surname ')
    s=s.upper()
    d=d.upper()
    print(d+s)
else:
    print(s.lower())