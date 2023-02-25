def three_four(n):
    for i in range(1, n+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i


for i in three_four(int(input())):
    print(i, end=" ")

# от 0 до N числа цифры которые делятся на 3 и 4