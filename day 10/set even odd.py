b={1,12,5,24,7,36,11,48,55,60}
even=0
odd=0
for number in b:
    if number % 2==0:
        even+=1
    else:
        odd+=1
print(b)
print("Enter the even number is:",even)
print("Enter the odd number is:",odd)
