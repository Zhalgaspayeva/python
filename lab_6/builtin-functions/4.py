from time import sleep

num = int(input())
miliseconds = int(input())
sleep(miliseconds / 1000)
print(f'Square root of {num} after {miliseconds} miliseconds is {num ** 0.5}')