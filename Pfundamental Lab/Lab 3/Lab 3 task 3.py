#course detail
course=50
Islamiat=input("Enter Marks of Islamiat: ")
English=input("\n Enter the Marks of english: ")
LinAlg=input("\n Enter the marks of Lin-algebra: ")
Pfund=input("\n Enter the marks of Pfundamental: ")
ITC=input("\n Enter the marks of ITC: ")
Obtained_Marks=int(Islamiat)+int(English)+int(LinAlg)+int(Pfund)+int(ITC)
Total_Marks=course*5
average = Obtained_Marks/5
percentage=(Obtained_Marks*100)/Total_Marks
print("\n Total Percentage Calculated: ", percentage)
print("\n Final Average Calculated: ", average)