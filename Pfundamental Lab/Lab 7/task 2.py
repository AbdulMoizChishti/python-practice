def max(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)   
a=int(input("first number="))
b=int(input("second number="))
c=int(input("third number="))
max(a, b, c)
print("is the maximum of three integers")