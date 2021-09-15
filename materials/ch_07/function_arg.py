def circle_area(radius, pi=3.14):
    area = pi * radius * radius
    return area


def rectangle_area(width, heigth=1):
    area = width * heigth
    return area


print(circle_area(10))
print(circle_area(10, pi=3.14151923))
print(circle_area(10, 3.14151923))

print(rectangle_area(4, 5))
print(rectangle_area(4))