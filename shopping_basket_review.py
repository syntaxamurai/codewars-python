'''
basket_summary("John", [120, 250, 80, 45])   → "John: 4 items, Total: 495.00, Avg: 123.75"
basket_summary("Mary", [300, 250, 100])       → "Mary: 3 items, Total: 650.00, Avg: 216.67. Qualifies for free delivery!"
'''

def basket_summary(name, items):
    num_items = len(items)
    total_price = sum(items)
    avg = total_price / num_items

    if total_price > 500:
        return f'{name}: {num_items} items, Total: {total_price:.2f}, Avg: {avg:.2f}. Qualifies for free delivery!'
    return f'{name}: {num_items} items, Total: {total_price:.2f}, Avg: {avg:.2f}'

print(basket_summary("John", [120, 250, 80, 45]))   # "John: 4 items, Total: 495.00, Avg: 123.75"
print(basket_summary("Mary", [300, 250, 100]))      # "Mary: 3 items, Total: 650.00, Avg: 216.67. Qualifies for free delivery!"
print(basket_summary("Brian", [50, 30, 20, 10, 15]))# "Brian: 5 items, Total: 125.00, Avg: 25.00"
print(basket_summary("Alice", [500, 100]))         # "Alice: 2 items, Total: 600.00, Avg: 300.00. Qualifies for free delivery!"
print(basket_summary("Tom", [100, 150, 200]))      # "Tom: 3 items, Total: 450.00, Avg: 150.00"
print(basket_summary("Emma", [50, 75, 25]))        # "Emma: 3 items, Total: 150.00, Avg: 50.00"
print(basket_summary("Liam", [600]))               # "Liam: 1 items, Total: 600.00, Avg: 600.00. Qualifies for free delivery!"
print(basket_summary("Sophia", [80, 90, 100, 110]))# "Sophia: 4 items, Total: 380.00, Avg: 95.00"
print(basket_summary("Noah", [499.99, 0.01]))      # "Noah: 2 items, Total: 500.00, Avg: 250.00"
print(basket_summary("Olivia", [200, 150, 100]))   # "Olivia: 3 items, Total: 450.00, Avg: 150.00"