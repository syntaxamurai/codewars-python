'''
list_analyst("Scores", [88, 92, 75, 100, 63, 77])
→ "Scores — Count: 6, Sum: 495, High: 100, Low: 63, Range: 37, Avg: 82.50"

list_analyst("Prices", [120, 450, 80, 230, 95])
→ "Prices — Count: 5, Sum: 975, High: 450, Low: 80, Range: 370, Avg: 195.00"
'''

def list_analyst(name, arr):
    count_arr = len(arr)
    sum_arr = sum(arr)
    high = max(arr)
    low = min(arr)
    range_arr = high - low
    avg = sum_arr / count_arr

    return f'{name} — Count: {count_arr}, Sum: {sum_arr}, High: {high}, Low: {low}, Range: {range_arr}, Avg: {avg:.2f}'

print(list_analyst("Scores", [10, 20, 30, 40]))
print(list_analyst("Repeats", [5, 5, 5, 5, 5]))
print(list_analyst("Grades", [100, 50, 75]))
print(list_analyst("Numbers", [1, 2, 3, 4, 5, 6]))
print(list_analyst("Sales", [250, 500, 750]))
print(list_analyst("Decimals", [10.5, 20.75, 15.25]))
print(list_analyst("Single", [1]))
print(list_analyst("Zeros", [0, 0, 0]))
print(list_analyst("Mixed", [-10, 0, 10, 20]))
print(list_analyst("Multiples", [7, 14, 21, 28, 35]))
print(list_analyst("Large Numbers", [999, 1000, 1001]))
print(list_analyst("Uniform", [3, 3, 3, 3, 3]))
print(list_analyst("Random", [50, 25, 75, 100]))
print(list_analyst("Sequence", [12, 15, 18, 21, 24, 27]))
print(list_analyst("Negatives", [-5, -10, -15]))
print(list_analyst("Floats", [1.1, 2.2, 3.3, 4.4]))
print(list_analyst("Two Items", [5, 10]))
print(list_analyst("Decimals Small", [0.5, 0.25, 0.75]))
print(list_analyst("Big Range", [100, 200, 300, 400, 500]))
print(list_analyst("Random Mix", [8, 6, 7, 5, 3, 0]))