def camel_to_snake(string):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in string]).lstrip('_')

string = "helloWorldHowAreYou"
snake_string = camel_to_snake(string)
print(snake_string)