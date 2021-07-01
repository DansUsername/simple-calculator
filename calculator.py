# simple calculator

op = input('''
Please pick one of the following operations:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
x = int(input('enter first number: '))
y = int(input('enter second number: '))

if op == '+':
    print('{} + {} = '.format(x,y))
    print(x + y)
elif op == '-':
    print('{} - {} = '.format(x,y))
    print(x - y)
elif op == '*':
    print('{} * {} = '.format(x,y))
    print(x * y)
elif op == '/':
    print('{} / {} = '.format(x,y))
    print(x / y)

else:
    print("unknown value")
