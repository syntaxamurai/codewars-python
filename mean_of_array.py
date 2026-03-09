'''
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
'''

def get_average(marks):
    return int(sum(marks) / len(marks))

'''
Used sum method to find the sum of all the items in the array
Used len to find the number of items in the array
Found the mean by dividing the sum over the number of arrays
Used int method to round down the number
'''

tests = [
    [2,2,2,2],
    [1,2,3,4,5],
    [10,20,30,40],
    [100,90,80],
    [5,6,7],
    [1,1,1,1,1],
    [50,60],
    [0,0,0,0],
    [3,5,7,9],
    [12,15,18]
]

for t in tests:
    print(get_average(t))

'''
Used a list tests to have all my tests together
Used a for loop to go through each item in my tests list
printed the output of each item
'''