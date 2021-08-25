'''
2 * 1 = 2
2 * 2 = 4
...
2 * 12 = 24
'''

n = int(input('Enter an integer: '))
k = 1
while k <= 36:
    # print(f'{n} * {k} = {n*k}')
    print(n, '*', k, '=', 2*k)
    k = k + 1
