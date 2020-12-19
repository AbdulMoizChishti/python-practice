# Abdul Moiz Chishti BSE=20F-022
str = input("Enter the string phrase : ")
vowels = 0
characters = 0
consonants = 0
spaces = 0
words = 0
str = str.lower()
#Vowels, Consonents and space count
for i in range(0, len(str)):
    if (str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        vowels = vowels + 1
    elif((str[i] >= 'a' and str[i] <= 'z')):
        consonants = consonants + 1
    elif (str[i] ==' '):
        spaces = spaces + 1
#total word count
words=1
for i in range(len(str)):
    if(str[i] == ' ' or str == '\n' or str == '\t'):
        words = words + 1
#Total Character count
characters=0
for i in str:
    characters = vowels + consonants    
print("Total Vowels: ", vowels)
print("Total Consonants: ", consonants)
print("Total spaces: ", spaces)
print("Total words : ", words)
print("Total Characters: ", characters)