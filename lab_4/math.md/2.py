import math

def area(height, base1, base2):
    return (height * base1 + height * base2) / 2


a = area(int(input("Height: ")), int(input("Base, first value: ")),
         int(input("Base, second value: ")))
print(f"Expected Output: {a}")

# плащадь трапеции