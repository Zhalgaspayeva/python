import random

x = True
name = input("Hello what is your name?")

print(f"Well, {name}, I am thinking of a number between 1 and 20.")

print("Take a guess.")

y = random.randint(1,20)
cnt = 0
while x:
    num = int(input())
    cnt += 1
    if(num > y):
        print("Your guess is to big")
        print("Take a guess")
    elif(num < y):
        print("Your guess is to low")
        print("Take a guess")
    else:
        print(f"Good job, KBTU! You guessed my number in {cnt} guesses!")
        x = False