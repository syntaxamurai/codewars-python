'''
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: [-2.398]
Output: -2.398

Input: []
Output: 0

Assumptions
You can assume that you are given a (possibly empty) valid array containing only numbers.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.
'''

def sum_array(a):
    if a == []:
        return 0
    return sum(a)

'''
I solved it by first returning zero uf the array is empty
I then wrote an array method 'sum' that return the sum of the numbers in an array
'''

print(sum_array([1, 2, 3]))          # 6
print(sum_array([10, 20, 30]))       # 60
print(sum_array([5]))                # 5
print(sum_array([]))                 # 0
print(sum_array([7, 3, 9, 2]))       # 21
print(sum_array([15, 5, 10, 20]))    # 50
print(sum_array([4, 8, 12, 16]))     # 40
print(sum_array([-1, -2, -3]))       # -6
print(sum_array([10, -5, 3]))        # 8
print(sum_array([-10, 5, -2, 7]))    # 0
print(sum_array([1,2,3,4,5,6,7,8,9,10]))   # 55
print(sum_array([100,200,300,400]))        # 1000
print(sum_array([13, 27, 35, 49, 52]))     # 176
print(sum_array([0, 0, 0]))          # 0
print(sum_array([999999, 1]))        # 1000000
print(sum_array([-1000, 500, 500]))  # 0