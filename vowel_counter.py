'''
"The Vowel Counter"
Write a function called count_vowels that takes a sentence as input and returns a formatted summary string.

Count how many vowels are in the sentence (a, e, i, o, u — both upper and lowercase)
Count how many words are in the sentence
Return the result as a formatted string

Examples:
count_vowels("Hello World")         
→ "2 words, 3 vowels"

count_vowels("I love Nairobi")      
→ "3 words, 7 vowels"

count_vowels("Python is amazing")   
→ "3 words, 6 vowels"

count_vowels("  Hello   World  ")   
→ "2 words, 3 vowels"
Constraints:

No loops
Only string methods
Extra spaces between words or at the edges should not affect the word count or vowel count
'''

def count_vowels(word):
    #word count
    words = word.strip().split()
    wordcount = len(words)

    #vowelcount
    vowel_lower = word.lower()
    a = vowel_lower.count("a")
    e = vowel_lower.count("e")
    i = vowel_lower.count("i")
    o = vowel_lower.count("o")
    u = vowel_lower.count("u")
    vowel_count = a + e + i + o + u

    return f"{vowel_count} vowels, {wordcount} words"



print(count_vowels("This is the word"))      # Expected: Vowels: 4, Words: 4
print(count_vowels("Hello world"))           # Expected: Vowels: 3, Words: 2
print(count_vowels("Apple Is Orange"))       # Expected: Vowels: 7, Words: 3
print(count_vowels("Education"))             # Expected: Vowels: 5, Words: 1
print(count_vowels("Rhythms myths"))         # Expected: Vowels: 0, Words: 2
print(count_vowels("Hello, how are you?"))   # Expected: Vowels: 7, Words: 4
print(count_vowels("I have 2 apples"))       # Expected: Vowels: 5, Words: 4
print(count_vowels(""))                      # Expected: Vowels: 0, Words: 0
print(count_vowels("   This   is   spaced   ")) # Expected: Vowels: 4, Words: 3
print(count_vowels("aeiou AEIOU"))           # Expected: Vowels: 10, Words: 2