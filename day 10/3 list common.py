list1 = list(map(int, input("Enter elements of first list (separated by space): ").split()))
list2 = list(map(int, input("Enter elements of second list (separated by space): ").split()))
list3 = list(map(int, input("Enter elements of third list (separated by space): ").split()))
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common_elements = set1 & set2 & set3
if common_elements:
    print("Common elements in all three lists:", common_elements)
else:
    print("No common elements found in all three lists.")
