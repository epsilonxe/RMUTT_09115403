
# f(x) = x^3 - x - 2
# def f(x):
#     y = x ** 3 - x - 2
#     return y

def f(x):
    y = x ** 5 + x ** 3 + x ** 2 - 1
    return y

def printline():
    print('-' * 45)

def zero_abs_error(val, precision):
    if abs(val > 10 ** (-precision)):
        result = False
    else:
        result = True
    return result


def rel_error(val1, val2, precision):
    ea = abs( (val2 - val1) / val2 )
    if ea <= 10 ** (-precision):
        result = True
    else:
        result = False
    return result


ls = float(input('Enter a left side value: '))
rs = float(input('Enter a right side value: '))
print(f'f({ls}) = {f(ls)}, f({rs}) = {f(rs)}')
printline()

if f(ls)*f(rs) < 0:
    print('Correct inputs')
    mid = (ls + rs) / 2
    print(f'mid = {mid} => f({mid}) = {f(mid)}')
    printline()

    n_round = 0
    precision = 5

    while zero_abs_error(f(mid), precision) :
        n_round = n_round + 1
        mid = (ls + rs) / 2 
        print(f'r={n_round:3} -> {ls:14.{precision}f} {rs:14.{precision}f} {mid:14.{precision}f} {f(mid):20.{precision}f}')
        if f(ls) * f(mid) > 0:
            ls = mid
        elif f(rs) * f(mid) > 0:
            rs = mid
        else:
            print('Fetal Error')
            break

    printline()
    print(f'Root of f(x) is {mid:20.{precision}f} => f({mid:20.{precision}f}) = {f(mid):20.{precision}f}' )

else:
    print('Incorrect inputs')
    print('Please choose left side/right side again')