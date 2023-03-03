import re
string = "ababbabbbabbbb"
match = re.findall("ab*", string)
print(match)