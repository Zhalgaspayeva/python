def filter_prime(x):
    y = []
    for i in range(0,len(x)):
        for j in range(2,int(x[i]/2)):
            if(x[i]%j==0):
                u = False
                break
        else:
            y.insert(0,x[i])
    return y
    
        
x = [1,2,3,4,5,6,7,8,9,10,11]
y = filter_prime(x)
y.reverse()
print(y)
