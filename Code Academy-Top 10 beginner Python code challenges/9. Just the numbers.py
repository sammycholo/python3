'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 9 : Just the numbers

'''
def just_num(lst):
    lst1 = []
    for e in lst:
        if type(e) == int and e >= 0:
            lst1.append(e)
    return lst1
    
new = just_num([10,"a","abc",9,"hello world",13,11,10,"k"])
print(new)
