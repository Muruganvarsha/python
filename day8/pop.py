number=[]
for i in range(5):
    num=int(input("Enter the number:"))
    number.append(num)
removed_element=number.pop()
print("removed element:",removed_element)
print("updated list:",number)
