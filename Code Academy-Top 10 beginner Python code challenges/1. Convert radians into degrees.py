'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 1 : Convert radians into degrees
'''
def convert_radians(rad:int)->float:
    degree = rad*(180/3.1415)
    return degree

new = convert_radians(2)
print(new)
