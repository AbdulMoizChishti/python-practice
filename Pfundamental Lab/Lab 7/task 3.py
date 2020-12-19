def GCD(a,b):
    if a>b:
        c=a
    else:
        c=b
    for x in range(c,0,-1):
        if a%x==0 and b%x==0:
            return x

a=int(input("Enter any number:"))
b=int(input("Enter second number:"))
gcd=GCD(a,b)
print(gcd,"is the gcd among",a,"and",b)