'''
** The Shopping Basket **
Write a function called basket_summary that takes a list of item prices and a customer name and returns a formatted summary.

Count how many items are in the basket
Calculate the total price
Calculate the average price per item rounded to 2 decimal places
If the total is above 500, add "Qualifies for free delivery!" on the end

Examples:
basket_summary("John", [120, 250, 80, 45])        
→ "John: 4 items, Total: 495.00, Avg: 123.75"

basket_summary("Mary", [300, 250, 100])            
→ "Mary: 3 items, Total: 650.00, Avg: 216.67. Qualifies for free delivery!"

basket_summary("Brian", [50, 30, 20, 10, 15])     
→ "Brian: 5 items, Total: 125.00, Avg: 25.00"

basket_summary("Alice", [500, 100])                
→ "Alice: 2 items, Total: 600.00, Avg: 300.00. Qualifies for free delivery!"
Constraints:

Use len() on the list
Use sum() — a built-in Python function that adds all items in a list
No loops needed
'''

def basket_summary(name, items):
    total_items = len(items)
    total_price = sum(items)
    avg_price = total_price / total_items
    summary = f'{name}: {total_items} items, Total: {total_price:.2f}, Avg: {avg_price:.2f}'

    if total_price > 500:
        return f'{summary}. Qualifies for free delivery!' 
    return f'{summary}'

print(basket_summary("John", [120, 250, 80, 45]))
print(basket_summary("Mary", [300, 250, 100]))
print(basket_summary("Brian", [50, 30, 20, 10, 15]))
print(basket_summary("Alice", [500, 100]))
print(basket_summary("Tom", [100]))
print(basket_summary("Sarah", [250, 249]))
print(basket_summary("Daniel", [499]))
print(basket_summary("Grace", [200, 200, 200]))
print(basket_summary("Kevin", [125, 125, 125, 125]))
print(basket_summary("Lucy", [10, 20, 30, 40, 50, 60]))
print(basket_summary("Mark", [300, 199.99]))
print(basket_summary("Sophia", [100.5, 200.75, 50.25]))
print(basket_summary("James", [500]))
print(basket_summary("Olivia", [499.99]))
print(basket_summary("Noah", [250, 250]))
print(basket_summary("Emma", [80, 90, 100, 110, 120]))
print(basket_summary("Liam", [5, 10, 15, 20, 25, 30, 35]))
print(basket_summary("Mia", [400, 50, 25, 10]))
print(basket_summary("Ethan", [60, 70, 80, 90, 100]))
print(basket_summary("Ava", [150.25, 349.75]))
print(basket_summary("Logan", [20, 20, 20, 20, 20, 20, 20, 20]))
print(basket_summary("Isabella", [333.33, 166.67]))
print(basket_summary("Lucas", [100, 150, 200, 75]))
print(basket_summary("Chloe", [250.5, 249.5]))