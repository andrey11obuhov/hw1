a=input('Is it raining? ')
a=a.lower()
if a=='yes':
    b=input('Is it windy' )
    b=b.lower()
    if b=='yes':
        print('It is too windy for an umbrella ')
    else:
        print('Take an umbrella ')
else:
    print('Enjoy your day ')
