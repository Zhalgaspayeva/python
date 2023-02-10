def spy_game(nums):
    x = 2
    y = 1
    for i in range(0,len(nums)):
        if(nums[i]==0):
            x-=1
        if(nums[i]==7 and x<=0):
            y-=1
    if x!=2 and y!=1:
        return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# подряд стоящие 007