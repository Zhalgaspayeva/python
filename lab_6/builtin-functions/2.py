s = input()
lower = [
    1 if str(i).islower() else 0
    for i in s
]
upper = [
    1 if str(i).isupper() else 0
    for i in s
]
print('lower',sum(lower))
print('upper',sum(upper))