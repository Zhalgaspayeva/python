import math

def parallelogram_area(base, height):
    return base * height


area_parallelogram = parallelogram_area(
    int(input("Length of base: ")), int(input("Height of parallelogram: ")))

print(f"Expected Output: {area_parallelogram}")

# площадь параллелограмма