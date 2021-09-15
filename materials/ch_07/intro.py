# Function

# Type: No Input, No Output

def showlines():
    chr = '#'
    n = 90
    print(chr * n)
    print('CALLING --> showlines')

# --------------------------------------------

# Type: One Input, One output
'''
            |----|
INPUT -->   | F  |   --> OUTPUT
            |----|

'''

def square_num(x):
    z = x * x
    return z

# --------------------------------------------

# Type: One Input, No Output

def square_table(x):
    for k in range(1, x):
        print('k = ', k, '--> k^2 = ', square_num(k))

# --------------------------------------------

# Type: Multiple Inputs, One Output

def rectangle_area(width, heigth):
    area = width * heigth
    return area

# --------------------------------------------

# Type: One Input, Multiple Outputs

def cal_circle(radius):
    pi = 3.1415
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return (area, circumference)




# Main Program
print('Hello World!')

# showlines()
# showlines()
# print(square_num(4))
# print(square_num(25.5))
# square_table(100)
# print(rectangle_area(4, 5))

x, y = cal_circle(10)
print(x)
print(y)
