def filter(ls):
    l = []
    for x in range(0,len(ls)):
        for i in range(2,int(ls[x]/2)):
            if ls[x]%i==0:
                t = False
                break
        else:
            l.append(ls[x])
    return l


ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
t = filter(ls)
print(t)