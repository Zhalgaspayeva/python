def square(a, b):
    for i in range(a, b + 1):
        yield i * i


first = int(input())
second = int(input())
for i in square(first, second):
    print(i, end=" ")