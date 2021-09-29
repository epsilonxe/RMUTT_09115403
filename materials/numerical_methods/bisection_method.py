
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
    if abs(val) > 10 ** (-precision):
        result = True
    else:
        result = False
    return result

print('root finding: bisection method'.upper())
print('f(x) = x ** 5 + x ** 3 + x ** 2 - 1')
ls = float(input('Enter a left side value: '))
rs = float(input('Enter a right side value: '))
precision = int(input('Enter a precision for absolute error: '))
# print(f'f({ls}) = {f(ls)}, f({rs}) = {f(rs)}')
printline()

if f(ls)*f(rs) < 0:
    print('Correct inputs')
    mid = (ls + rs) / 2
    print(f'mid = {mid} => f({mid}) = {f(mid)}')
    printline()
    n_round = 0
    print(f'r={n_round:3} -> {ls:14.{precision}f} {rs:14.{precision}f} {mid:14.{precision}f} {f(mid):20.{precision}f}')
    
    while zero_abs_error(f(mid), precision) :
        n_round = n_round + 1
        if f(ls) * f(mid) > 0:
            ls = mid
        elif f(rs) * f(mid) > 0:
            rs = mid
        else:
            print('Fetal Error')
            break
        mid = (ls + rs) / 2 
        print(f'r={n_round:3} -> {ls:14.{precision}f} {rs:14.{precision}f} {mid:14.{precision}f} {f(mid):20.{precision}f}')
    
    solution = mid
    printline()
    print(f'Root of f(x) is {solution:.{precision}f} => f({solution:.{precision}f}) = {f(solution):.{precision}f}' )

else:
    print('Incorrect inputs')
    print('Please choose left side/right side again')