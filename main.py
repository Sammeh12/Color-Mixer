print('Enter the colors that you want to mix.')

# Input two colors
c1 = (input('Enter first color: '))
c2 = (input('Enter second color: '))

# Primary Colors
p1 = 'red'
p2 = 'yellow'
p3 = 'blue'

# Secondary Colors
s1 = 'orange'
s2 = 'green'
s3 = 'violet'

if (c1.casefold() == p1 and c2.casefold() == p2) or (c1.casefold() == p2 and c2.casefold() == p1):
    print(c1.lower() + ' + ' + c2.lower() + ' = ' + s1)
elif (c1.casefold() == p2 and c2.casefold() == p3) or (c1.casefold() == p3 and c2.casefold() == p2):
    print(c1.lower() + ' + ' + c2.lower() + ' = ' + s2)
elif (c1.casefold() == p3 and c2.casefold() == p1) or (c1.casefold() == p1 and c2.casefold() == p3):
    print(c1.lower() + ' + ' + c2.lower() + ' = ' + s3)
else:
    print('Invalid Input!')
