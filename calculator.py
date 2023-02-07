print('Enter function.')
f = input()
if f == '*':
    print('Enter variable 1')
    a = int(input())
    print('Enter variable 2')
    b = int(input())
    print(a * b)
elif f == '+':
    print('Enter variable 1')
    a = int(input())
    print('Enter variable 2')
    b = int(input())
    print(a + b)
elif f == '/':
    print('Enter variable 1')
    a = int(input())
    print('Enter variable 2')
    b = int(input())
    print(a/b)
elif f == '-':
    print('Enter variable 1')
    a = int(input())
    print('Enter variable 2')
    b = int(input())
    print(a+b)
else:
    print( f'Is not a function')