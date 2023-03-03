def snake_to_camel(string):
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

string = "hello_world_how_are_you"
camel_string = snake_to_camel(string)
print(camel_string)