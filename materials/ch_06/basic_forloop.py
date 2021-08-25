# print('Hello', 1)
# ...
# print('Hello', 10)

for k in range(1, 11):
    print('Hello', k)

print('-' * 30)

for k in [1, 3, 5, 7, 9]:
    print('Hello', k)

print('-' * 30)

for s in 'HELLO WORLD':
    print(s, end='....')
print()

print('-' * 30)

for x,y in [(1,2), (3, 100), (5, 99)]:
    print('x = ', x)
    print('y = ', y)