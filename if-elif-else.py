a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')
