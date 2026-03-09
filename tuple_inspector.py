'''
"The Tuple Inspector"
Write a function called tuple_inspector that takes a tuple of numbers and returns a formatted summary.

The highest number in the tuple
The lowest number in the tuple
How many items are in the tuple
Whether the tuple has more than 3 items — if yes add "Extended tuple", if no add "Short tuple"

Examples:
tuple_inspector((5, 3, 8, 1, 9, 2))    
→ "High: 9, Low: 1, Count: 6 — Extended tuple"

tuple_inspector((10, 20, 30))           
→ "High: 30, Low: 10, Count: 3 — Short tuple"

tuple_inspector((7, 2))                 
→ "High: 7, Low: 2, Count: 2 — Short tuple"

tuple_inspector((1, 5, 3, 9, 4, 2, 8)) 
→ "High: 9, Low: 1, Count: 7 — Extended tuple"
Constraints:

Use max() and min() — built in Python functions that work on both lists and tuples
Use len()
The input is a tuple not a list — treat it accordingly
'''

def tuple_inspector(x):
    highest = max(x)
    lowest = min(x)
    total_items = len(x)
    
    if total_items > 3:
        return f'High: {highest}, Low: {lowest}, Count: {total_items} — Extended tuple'
    return f'High: {highest}, Low: {lowest}, Count: {total_items} — Short tuple'

print(tuple_inspector((5, 3, 8, 1, 9, 2)))
print(tuple_inspector((1, 2, 3)))
print(tuple_inspector((10, 20, 30, 40)))
print(tuple_inspector((5,)))
print(tuple_inspector((7, 3, 9, 1)))
print(tuple_inspector((100, 50)))
print(tuple_inspector((8, 6, 7, 5, 3, 0)))
print(tuple_inspector((42, 42, 42)))
print(tuple_inspector((9, 8, 7, 6)))
print(tuple_inspector((15, 25, 35)))
print(tuple_inspector((2, 4, 6, 8, 10)))
print(tuple_inspector((999, 1, 500, 250)))
print(tuple_inspector((3, 3, 3, 3)))
print(tuple_inspector((12, 5, 18, 7, 20)))
print(tuple_inspector((1000,)))
print(tuple_inspector((4, 2)))
print(tuple_inspector((11, 22, 33, 44, 55, 66)))
print(tuple_inspector((0, -5, 10, 15)))
print(tuple_inspector((-10, -20, -5)))
print(tuple_inspector((1, 100, 50, 25, 75)))
print(tuple_inspector((6, 2, 9)))