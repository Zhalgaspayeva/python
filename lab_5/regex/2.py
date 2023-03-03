import re
string = "abb abbb abbbb abbbbb"
match = re.findall("ab{2,3}", string)
print(match)