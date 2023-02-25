'''
Оператор with работает с функцией open() для открытия файла.

Таким образом, вы можете переписать код, который мы использовали в примере с функцией open(), следующим образом:
'''
with open("hello.txt") as my_file:
    print(my_file.read())

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file

# гитхаб занимается рендером
# ехксель может не распазнать

# rainbow делает цветное раделение
# ETL про разработку