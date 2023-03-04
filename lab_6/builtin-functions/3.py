s = input()
t = s[::-1] # реверс строки
if hash(s) == hash(t):
    print('polidrom') 
else :
    print('not polidrom')