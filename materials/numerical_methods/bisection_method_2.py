
# f(x) = x^3 - x - 2
# def f(x):
#     y = x ** 3 - x - 2
#     return y

def f(x):
    y = x ** 5 + x ** 3 + x ** 2 - 1
    return y

def printline():
    print('-' * 45)


def rel_error(val1, val2, percent_error):
    ea = abs( (val2 - val1) / val2 )
    # print('REL_ERR->', val1, val2, ea)
    if ea >= percent_error:
        result = True
    else:
        result = False
    return result


print('root finding: bisection method'.upper())
print('f(x) = x ** 5 + x ** 3 + x ** 2 - 1')

ls = float(input('Enter a left side value: '))
rs = float(input('Enter a right side value: '))
err = float(input('Enter a relative error value: '))
# print(f'f({ls}) = {f(ls)}, f({rs}) = {f(rs)}')
printline()

if f(ls)*f(rs) < 0:
    print('Correct inputs')
    mid = (ls + rs) / 2
    # print(f'mid = {mid} => f({mid}) = {f(mid)}')
    printline()

    n_round = 0
    percent_error = err

    '''
    The first member of mid_list is a dummy value
    which is set to 999*mid.
    This guarantees a very high relative error in the first round.
    '''
    mid_list = [999*mid, mid]

    print(f"{'ROUND':16} {'LS':14} {'RS':14} {'MID':14} {'f(MID)':20}")
    print(f'r={n_round:3} -> {ls:14.5f} {rs:14.5f} {mid:14.5f} {f(mid):20.5f}')

    while rel_error(mid_list[-2], mid_list[-1], percent_error) :       
        n_round = n_round + 1
        if f(ls) * f(mid) > 0:
            ls = mid
        elif f(rs) * f(mid) > 0:
            rs = mid
        else:
            print('Fetal Error')
            break
        mid = (ls + rs) / 2
        mid_list.append(mid)
        print(f'r={n_round:3} -> {ls:14.5f} {rs:14.5f} {mid:14.5f} {f(mid):20.5f}')

    solution = mid_list[-1]
    printline()
    print(f'Root of f(x) is {solution:.5f} => f({solution:.5f}) = {f(solution):.5f}' )

else:
    print('Incorrect inputs')
    print('Please choose left side/right side again')