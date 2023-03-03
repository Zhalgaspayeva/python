import re
string = "Hello, world. How are you?"
new_string = re.sub("[ ,.]", ":", string)
print(new_string)