'''
format_price("john doe", "laptop", 1500)  → "John Doe bought LAPTOP for 1500.00 (Premium)"
format_price("JANE smith", "book", 25.5)  → "Jane Smith bought BOOK for 25.50"
format_price("mary", "pen", 10)           → "Mary bought PEN for 10.00"
'''

def format_price(name, item, price):
    new_name = name.lower().title()
    new_item = item.upper()

    if price > 1000:
        return f'{new_name} bought {new_item} for {price:.2f} (Premium)'
    return f'{new_name} bought {new_item} for {price:.2f}'

print(format_price("john doe", "laptop", 1500))    # "John Doe bought LAPTOP for 1500.00 (Premium)"
print(format_price("JANE smith", "book", 25.5))    # "Jane Smith bought BOOK for 25.50"
print(format_price("mary", "pen", 1000))             # "Mary bought PEN for 1000.00"
print(format_price("ALICE JOHNSON", "phone", 800)) # "Alice Johnson bought PHONE for 800.00"
print(format_price("robert", "notebook", 15))      # "Robert bought NOTEBOOK for 15.00"
print(format_price("EMILY davis", "tablet", 1200)) # "Emily Davis bought TABLET for 1200.00 (Premium)"
print(format_price("michael", "headphones", 60.75))# "Michael bought HEADPHONES for 60.75"
print(format_price("sarah lee", "bag", 45.5))      # "Sarah Lee bought BAG for 45.50"
print(format_price("CHRIS", "monitor", 350))       # "Chris bought MONITOR for 350.00"
print(format_price("anna", "keyboard", 75))        # "Anna bought KEYBOARD for 75.00"