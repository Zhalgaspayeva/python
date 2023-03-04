# all()
a = (
    i == 'True' for i in input().split()
)
x = all(a)
print(x)