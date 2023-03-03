import re
string = "HelloWorldHowAreYou"
split_string = re.findall('[A-Z][^A-Z]*', string)
print(split_string)