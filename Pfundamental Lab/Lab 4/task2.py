yos= int(input("enter year of service"))
q= input("enter your qualification")
que=q.lower()
if yos>=10 and que=="masters":
    print("Your Salary is 150000")
elif yos>=10 and que=="bachelors":
    print("your salary is 100000")
elif yos<10 and que=="masters":
    print("your salary is 100000")
elif yos<10 and que=="bachelors":
    print("your salary is 70000" )
else:
    print("you are not qualified enough")