def reverse(n):
    i = n
    while i != -1:
        yield i
        i -= 1


reverse_num = int(input())
for i in reverse(reverse_num):
    print(i, end=" ")