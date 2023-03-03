import re
string = "ThisIsAStringWithWordsStartingWithCapitalLetters"
new_string = re.sub(r"(?<=\w)([A-Z])", r" \1", string).lower()
print(new_string)