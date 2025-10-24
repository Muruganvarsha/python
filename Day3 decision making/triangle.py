a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))
if a==b and b==c:
    print("Issosceles triangle")
elif b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triange")
    



