'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 6 : Are the Xs equal to the Os?

'''
def equal_xo(mystr:str)->bool:
    if len(mystr) == 0:
        return True
    else:
        x = 0
        o = 0
        for e in mystr:
            if e == "X":
                x+=1
            elif e == "O":
                o+=1
        if x == o:
            return True
        else:
            return False
    
new = equal_xo("OOOXXX")
print(new)
new1 = equal_xo("XOXXO")
print(new1)
new2 = equal_xo("abc")
print(new2)
new3 = equal_xo("")
print(new3)
new4 = equal_xo("XOXXOXOO")
print(new4)
