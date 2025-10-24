held=int(input("Enter the number of held:"))
attended=int(input("Enter the number attended:"))
percentage=(attended/held)*100
print("attendance percentage:",percentage)
if percentage>=75:
    print("allowed to sit in exam")
else:
    print("not alowed to sit in exam")
