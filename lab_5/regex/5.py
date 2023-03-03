import re
string = "asfdljb"
match = re.findall(r"^a.+b$", string)
print(match)