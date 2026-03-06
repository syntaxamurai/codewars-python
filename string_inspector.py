'''
"The String Inspector"
Write a function called inspect_string that takes a sentence and a letter as inputs and returns a formatted summary.

Total number of characters in the sentence (including spaces)
Total number of words
How many times the given letter appears (case insensitive)

Examples:
inspect_string("Hello World", "l")  
→ "11 characters, 2 words, 3 occurrences of l"

inspect_string("I love Nairobi", "o")  
→ "14 characters, 3 words, 2 occurrences of o"

inspect_string("Python is AMAZING", "a")  
→ "17 characters, 3 words, 2 occurrences of a"
Constraints:

Use both len() and .count() — both must appear in your solution
Case insensitive letter search
'''

def inspect_string(sentence, letter):
    #Total number of words
    words = sentence.split()
    words_total = len(words)

    #How many times the given letter appears
    case = sentence.lower()
    num_letters = case.count(letter)

    #Total number of characters in the sentence
    characters_total = len(sentence)

    return f"{characters_total} characters, {words_total} words, {num_letters} occurrences of {letter}"

print(inspect_string("Hello World", "l"))
print(inspect_string("I love Nairobi", "o"))
print(inspect_string("Python is AMAZING", "a"))
print(inspect_string("The quick brown fox", "o"))
print(inspect_string("Nairobi is beautiful", "i"))
print(inspect_string("Kenya is my home", "e"))
print(inspect_string("I am learning Python", "n"))
print(inspect_string("Backend developer", "e"))
print(inspect_string("Hello", "h"))
print(inspect_string("UPPER CASE SENTENCE", "e"))
print(inspect_string("mixed CASE letters", "e"))
print(inspect_string("No vowels here", "z"))
print(inspect_string("One", "o"))
print(inspect_string("Codewars is fun", "s"))
print(inspect_string("Thirty days of code", "t"))