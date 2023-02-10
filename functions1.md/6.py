def  reverse(a):
    b = (a).split()
    s = ""
    for i  in range(0,len(b)):
        s += b[len(b)-i-1]
        s += " "

    return s

a = "We are ready"
b = reverse(a)
print(b)

# разделить предложение на слова через split и реверснуть