'''
"The List Analyst"
Write a function called list_analyst that takes a list of numbers and a name for the list and returns a full analysis.

Total count of numbers
The sum of all numbers
The highest number
The lowest number
The range (highest minus lowest)
Average rounded to 2 decimal places

Examples:
list_analyst("Scores", [88, 92, 75, 100, 63, 77])
→ "Scores — Count: 6, Sum: 495, High: 100, Low: 63, Range: 37, Avg: 82.50"

list_analyst("Temps", [36, 37, 38, 36, 39, 37])
→ "Temps — Count: 6, Sum: 223, High: 39, Low: 36, Range: 3, Avg: 37.17"

list_analyst("Prices", [120, 450, 80, 230, 95])
→ "Prices — Count: 5, Sum: 975, High: 450, Low: 80, Range: 370, Avg: 195.00"
Constraints:

Use len(), sum(), max(), min() — all four must appear
Calculate range yourself using the values you already have
No loops
'''

def list_analyst(name, nums):
    count_nums = len(nums)
    sum_nums = sum(nums)
    highest = max(nums)
    lowest = min(nums)
    range_nums = highest - lowest
    avg = sum_nums / count_nums

    return f'{name} — Count: {count_nums}, Sum: {sum_nums}, High: {highest}, Low: {lowest}, Range: {range_nums}, Avg: {avg:.2f}'

# print(list_analyst("Starter", [88, 92, 75, 100, 63, 77]))
print(list_analyst([10, 20, 30, 40], "Scores"))
print(list_analyst([5, 5, 5, 5, 5], "Repeats"))
print(list_analyst([100, 50, 75], "Grades"))
print(list_analyst([1, 2, 3, 4, 5, 6], "Numbers"))
print(list_analyst([250, 500, 750], "Sales"))
print(list_analyst([10.5, 20.75, 15.25], "Decimals"))
print(list_analyst([1], "Single"))
print(list_analyst([0, 0, 0], "Zeros"))
print(list_analyst([-10, 0, 10, 20], "Mixed"))
print(list_analyst([7, 14, 21, 28, 35], "Multiples"))
print(list_analyst([999, 1000, 1001], "Large Numbers"))
print(list_analyst([3, 3, 3, 3, 3], "Uniform"))
print(list_analyst([50, 25, 75, 100], "Random"))
print(list_analyst([12, 15, 18, 21, 24, 27], "Sequence"))
print(list_analyst([-5, -10, -15], "Negatives"))
print(list_analyst([1.1, 2.2, 3.3, 4.4], "Floats"))
print(list_analyst([5, 10], "Two Items"))
print(list_analyst([0.5, 0.25, 0.75], "Decimals Small"))
print(list_analyst([100, 200, 300, 400, 500], "Big Range"))
print(list_analyst([8, 6, 7, 5, 3, 0], "Random Mix"))