def uniq(numbers):
    u = []
    for item in numbers :
        if item not in u:
            u.append(item)
    return u

print(uniq([3,3,3,4,1,3,7,8,1,9,3,3,4,5,0,4,10]))

# уникальные элементы 