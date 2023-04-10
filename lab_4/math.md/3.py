# площадь правильного многоугольника
import math

side = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))


def polygon_area(sides, length):
    perimeter = sides * length
    length /= 2
    degree_polygon = 360 / (sides * 2)
    a = math.cos(degree_polygon) * length / math.sin(degree_polygon) # апофема
    area = (a * length) / 2
    return sides * area


if (side == 4):
    print(f"The area of the polygon is: {length ** 2}")
else:
    print(f"The area of the polygon is: {polygon_area(side, length)}")