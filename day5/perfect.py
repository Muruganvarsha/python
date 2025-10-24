n=int(input("Enter the number:"))
for num in range(1,num):
    sum_of_divisor=0
    for i in range(1,num):
        if num %1==0:
            sum_of_divisor +=i
        if sum_of_divisor==num:
            print(num)
