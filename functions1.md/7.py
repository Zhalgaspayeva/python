def num(a):
    for i in range(0,len(a)):
        if(a[i]==3):
            if(a[i+1]==3):
                return True
    return False

a = [1,3,3,1]
x = num(a)
print(x)

# a 3 next to a 3