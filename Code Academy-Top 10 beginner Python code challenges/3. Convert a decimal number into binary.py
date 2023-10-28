'''
10 Python Code Challenges for Beginners : https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
Solution By : Samuel Emmanuel
Problem 3 : Convert a decimal number into binary
'''
def dec_bin(num):
    bin = []
    bin_num = ""
    if num > 0:
        while num != 0:
            rem = num%2
            bin.insert(0,rem)
            num = num//2
    for e in bin:
        bin_num = bin_num+str(e)
    return bin_num
    
new = dec_bin(1024)
print(new)
print("Using Bin", bin(1024))
new1 = dec_bin(999)
print("Using Bin", bin(999))
print(new1)
