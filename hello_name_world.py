def hello(name=""):
    name = name.capitalize()
    if name == "":
        return "Hello, World!"
    else:
        return f"Hello, {name}!"


print(hello("John"))
print(hello("aLIce"))
print(hello(""))