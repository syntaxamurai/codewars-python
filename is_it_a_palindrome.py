'''
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
'''

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("Madam"))
print(is_palindrome("RaceCar"))
print(is_palindrome("a"))
print(is_palindrome("aa"))
print(is_palindrome("ab"))
print(is_palindrome(""))
print(is_palindrome("12321"))
print(is_palindrome("12345"))
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("Step on no pets"))
print(is_palindrome("madam im adam"))
print(is_palindrome("Was it a rat I saw"))
print(is_palindrome("noon"))
print(is_palindrome("civic"))
print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("!@##@!"))
print(is_palindrome("!@#"))