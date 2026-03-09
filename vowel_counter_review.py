'''
count_vowels("Hello World")       → "2 words, 3 vowels"
count_vowels("I love Nairobi")    → "3 words, 7 vowels"
count_vowels("  Hello   World  ") → "2 words, 3 vowels"
'''

def count_vowels(sentence):
    #words
    word = len(sentence.split())

    #vowels
    vowel = sentence.lower()
    a = vowel.count("a")
    e = vowel.count("e")
    i = vowel.count("i")
    o = vowel.count("o")
    u = vowel.count("u")
    
    vowel_count = a + e + i + o + u

    return f'{word} words, {vowel_count} vowels'


print(count_vowels("Hello World"))        # "2 words, 3 vowels"
print(count_vowels("I love Nairobi"))     # "3 words, 7 vowels"
print(count_vowels("  Hello   World  "))  # "2 words, 3 vowels"
print(count_vowels("Python is fun"))      # "3 words, 4 vowels"
print(count_vowels("AEIOU aeiou"))        # "2 words, 10 vowels"
print(count_vowels("OpenAI ChatGPT"))     # "2 words, 5 vowels"
print(count_vowels("  Multiple   spaces "))# "2 words, 6 vowels"
print(count_vowels("sky"))                # "1 words, 0 vowels"
print(count_vowels("I am learning Python"))# "4 words, 7 vowels"
print(count_vowels(""))                    # "0 words, 0 vowels"