# We need a function that can transform a number (integer) into a string.

def number_to_string(num):
    return f"{num}"

#I used an fnum to pass the num as a variable in the string
#You can also use str(num)

print(number_to_string(67))     # 67
print(number_to_string(79585))  # 79585
print(number_to_string(-79585)) # -79585
print(number_to_string(1+2))    # 3
print(number_to_string(1-2))    # -1
print(number_to_string(0))      # 0