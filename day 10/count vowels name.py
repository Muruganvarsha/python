names=input("Enter the names:")
names.split()

vowels="aeiouAEIOU"
for name in names:
    count=0
    for char in names:
        if char in vowels:
            count+=1
print(f"{name}:{count}vowels")
