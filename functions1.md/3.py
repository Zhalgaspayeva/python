def func(x,y):
    if(y/4==x):
        return y
    for i in range(0,y):
        x -= 1
        y -= 2
        if(y/4 == x):
            return x

x = int(input())
y = int(input())
h = func(x,y)
l = x-func(x,y)
print(h)
print(l)

# h - numheads, l - numlegs