'''
"The Price Formatter"
Write a function called format_price that takes a person's name, an item they bought, and a price as inputs and returns a neatly formatted receipt line.

The name should be in title case
The item should be in uppercase
The price should show exactly 2 decimal places
If the price is above 1000, add the word "(Premium)" at the end
'''


def format_price(name, item, price):
    name = name.title()
    item = item.upper()

    if price < 1000:
        return f"{name} bought {item} for {price:.2f}"
    else:
        return f"{name} bought {item} for {price:.2f} (Premium)"

'''
I solved this by first converting the name to title case,
then the item to upper
I then used an if statement to find the prices that are below 1000
and an else statement to add the Premium tag for prices that exceed 1000
I used an f-string to convert the price to exactly two decimal places and return a neatly formatted receipt line
'''

print(format_price("john doe", "laptop", 1500))
print(format_price("JANE smith", "book", 25.5))
print(format_price("brian", "phone", 1000.1))
print(format_price("mary", "pen", 10))