price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
totalcost=price*quantity
if totalcost>1000:
    discount=totalcost*0.10
    totalcost-=discount
print("discount")
print("total cost pay")


             
