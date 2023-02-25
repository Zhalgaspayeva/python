def square_power(n):
    for i in range(1, n + 1):
        yield i * i


nums = int(input())
a = square_power(nums)

for i in range(nums):
    print(next(a), end=" ")