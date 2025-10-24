for i in range(8):
    for j in range(5):
        if((j==0 or j==4)and (i!=3 and i!=6))or((i==0 or i==3 or i==6)(j>0 and j<4)):
            print("*",end="")
        else:
                print("",end="")
        print()
           
