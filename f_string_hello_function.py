'''
hello("john")    → "Hello, John!"
hello("aliCE")   → "Hello, Alice!"
hello("")        → "Hello, World!"
'''

def hello(x):
    if x == "":
        return 'Hello, World!'
    return f'Hello, {x.capitalize()}!'

print(hello("john"))      # "Hello, John!"
print(hello("aliCE"))     # "Hello, Alice!"
print(hello(""))          # "Hello, World!"
print(hello("MARY"))      # "Hello, Mary!"
print(hello("peter"))     # "Hello, Peter!"
print(hello("sArAh"))     # "Hello, Sarah!"
print(hello("ALex"))      # "Hello, Alex!"
print(hello("david"))     # "Hello, David!"
print(hello(""))          # "Hello, World!" (testing empty again)
print(hello("joHNny"))    # "Hello, Johnny!"