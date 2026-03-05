def solution(string):
    return string[::-1] 
''' 
This is a step function. 
By following the syntax [start:stop:step],
I left the start and stop empty because I want the whole string
Used a negative step because U want to walk through the string from n=backwards(reversing it)
'''
print(solution('world'))
print(solution('hello'))
print(solution(''))
print(solution('h'))