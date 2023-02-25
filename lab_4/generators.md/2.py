def even_numbers(n):
    for i in range(1, n + 1):
        if (i % 2 == 0):
            yield i


second_num = int(input())
for i in even_numbers(second_num):
    print(i, end=" ")
