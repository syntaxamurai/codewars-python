'''
Is the string uppercase?
Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.
'''

def is_uppercase(inp):
    if inp == inp.upper():
        return True
    return False

print(is_uppercase("A"))
print(is_uppercase("a"))
print(is_uppercase("HELLO"))
print(is_uppercase("hello"))
print(is_uppercase("Hello"))
print(is_uppercase("hELLO"))
print(is_uppercase("HELLO WORLD"))
print(is_uppercase("HELLO World"))
print(is_uppercase("HELLO123"))
print(is_uppercase("HELLO123WORLD"))
print(is_uppercase("HELLO123world"))
print(is_uppercase("123"))
print(is_uppercase("123ABC"))
print(is_uppercase("123abc"))
print(is_uppercase("!!!"))
print(is_uppercase("@#$%^&*"))
print(is_uppercase("HELLO!"))
print(is_uppercase("HELLO!world"))
print(is_uppercase(""))
print(is_uppercase(" "))
print(is_uppercase("   "))
print(is_uppercase("HELLO_WORLD"))
print(is_uppercase("HELLO_world"))
print(is_uppercase("UPPERCASE"))
print(is_uppercase("UPPERCASElower"))
print(is_uppercase("ALL CAPS SENTENCE"))
print(is_uppercase("ALL Caps SENTENCE"))
print(is_uppercase("CAPS-WITH-DASH"))
print(is_uppercase("CAPS-WITH-dash"))