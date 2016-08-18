def gcd(num1,num2):
    if(not num1):
        return num2
    return gcd(num2%num1,num1)

def reduce(num1,num2):
    mod = 0
    for x in num2:
        mod = (mod*10 + int(x))%num1
    return mod

def gcdLarge(num1,num2):
    num = reduce(num1,num2)
    return gcd(num1,num)

num1 = 1221
num2 = "1234567891011121314151617181920212223242526272829"
print(gcdLarge(num1,num2))

