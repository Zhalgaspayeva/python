import re
string = "HelloWorld hELLOwORLD GoodMorning goodnight"
match = re.findall("[A-Z][a-z]+", string)
print(match)