var = input("enter a phrase")
v=var.lower()
for i in v:
    if i in ('aeiou'):
        print(i)

print("\t these are the vowels present in the phrase", v)