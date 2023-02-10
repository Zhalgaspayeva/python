def palindrom(s):
    size = int(len(s)/2)
    for i in range(0,size):
        if(s[i]!=s[len(s)-i-1]):
            return False    
    return True

a = str(input())
print(palindrom(a))


# проверка на полидром (читается одиннаково с двух сторон)