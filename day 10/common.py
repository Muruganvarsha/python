list1 = list(map(int, input("Enter elements of first list (separated by space): ").split()))
list2 = list(map(int, input("Enter elements of second list (separated by space): ").split()))
common = set(list1) & set(list2)
if common:
    print("The lists have common elements:", common)
else:
    print("The lists have no elements in common.")
