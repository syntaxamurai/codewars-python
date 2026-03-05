'''
Write a function called clean_string that takes a string as input and returns a new string where:

All leading and trailing whitespace is removed
The first letter of the string is capitalised
All other letters are lowercase
Any occurrence of the word "bad" is replaced with "good"

Examples:
clean_string("  hello WORLD  ")     → "Hello world"
clean_string("  BAD day today  ")   → "Good day today"
clean_string("  THIS IS BAD  ")     → "This is good"
clean_string("  bad BAD bad  ")     → "Good good good"
Constraints:

Do not use any loops
Only use string methods you have learned today
'''
def clean_string(string):
    return string.strip().lower().replace("bad", "good").capitalize()

'''
string.strip()            # removes leading/trailing whitespace
      .lower()            # makes everything lowercase first
      .replace("bad", "good")  # replaces "bad"
      .capitalize()       # capitalizes only the first letter, rest stays lowercase
'''

print(clean_string("  hello WORLD  "))
print(clean_string("  BAD day today  "))
print(clean_string("  THIS IS BAD  "))
print(clean_string("  bad BAD bad  "))