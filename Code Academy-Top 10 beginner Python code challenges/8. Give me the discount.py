'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 8 : Give me the discount

'''
def give_discount(price, dis):
    discount = (price/100)*dis
    return price-discount
new = give_discount(100,10)
print(new)
new1 = give_discount(133,31)
print(new1)
