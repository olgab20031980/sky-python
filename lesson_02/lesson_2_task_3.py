import math


def multiplay(side):
    area = side * side
    return math.ceil(area)


square_side = float(input("Сторона квадрата = "))
area = multiplay(square_side)

print(f"Площадь квадрата = {area}")
