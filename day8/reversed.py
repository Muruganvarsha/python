s=input("Enter the string:")
reversed_string=s[::-1]
for char in s:
    reversed_string=char + reversed_string
print("Reversed string:",reversed_string)
