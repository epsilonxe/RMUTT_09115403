# Functions
# Type: No Input - No Output

def showlines():
    n = 80
    chr = '$'
    print(n * chr)
    print('THIS IS A FUNCTION CALLING')
    print(n * chr)


def square(x):
    z = x ** 2
    return z


def square_table(x):
    for i in range(1, x):
        print('i = ', i, '-> i^2 = ', square(i))



# Main Program
print('This is how we use functions in Python')

# showlines()
# print(square(2))
square_table(10)