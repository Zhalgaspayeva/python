import re
string = "this_is_an_example_string"
match = re.findall("[a-z]+(?:_[a-z]+)+", string)
print(match)