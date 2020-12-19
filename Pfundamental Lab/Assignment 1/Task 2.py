roll=int(input("Enter roll number:"))
for i in range(1,11):
    if roll<=100:
        print(roll,"x",i,"=",roll*i)
    else:
        break