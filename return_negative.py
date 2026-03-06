'''
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

'''

def make_negative( number ):
    if number < 1:
        return number
    else:
        return -number
    
'''
Used an if else condition to check if the number is negative and return the number as is, or if the number is greater than one, then negate it
'''
print(make_negative(1))   # -1
print(make_negative(-5))  # -5
print(make_negative(0))   # 0