# os модуль
import os 

path = os.getcwd() # текущая папка
dirs = os.listdir(path)
for i in dirs:
    if os.path.isdir(i):
        print(f"Dir => {i}")
    elif os.path.isfile(i):
        print(f"File => {i}")