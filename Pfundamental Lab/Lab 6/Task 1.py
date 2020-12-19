s=0
for num in range(1,8):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
        
    factorial_s= num/factorial
    s= s+factorial_s
    
print("sum of first seven numbers of the series is =",round(s,3))