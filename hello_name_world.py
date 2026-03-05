def hello(name=""):
    # name = name.capitalize()
    if name == "":
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"

'''
This code uses the if...else conditional
It first checks if the name is empty, then returns Hello, World!
If the name is not empty, it returns an f-string
It also capitalizes the first letter and the other letters are lowercased
'''

print(hello("John"))
print(hello("aLIce"))
print(hello(""))