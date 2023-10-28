'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 2 : Sort a list
'''
def list_sort(lst, order):
    if order == "asc":
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                else:
                    j+=1
        return lst
    elif order == "dsc":
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                else:
                    j+=1
        return lst
    elif order == "none":
        return lst

new = list_sort([3,10,0,1,11,13,20,6], "asc")
new1 = list_sort([3,10,0,1,11,13,20,6], "dsc")
new2 = list_sort([3,10,0,1,11,13,20,6], "none")
print(new)
print(new1)
print(new2)
