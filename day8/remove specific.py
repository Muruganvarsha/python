item=[]
for i in range(5):
    a=input("Enter the item name:")
    item.append(a)
print("original list:",item)
remove=input("Enter the remove the item list:")
if remove in item:
    item.remove(remove)
print("updated list:",item)
