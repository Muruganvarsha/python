import math
def is_perfect(n):
    if n<=1:
        return false
    s=1
    for d in range(2,int(math.sqrt(n))+1):
        if n%d==0:
            s+=d
            other=n//d
            if other !=d:
                s+=other
    return s==n
numbers=input("Enter the numbers separated by spaces:")
num_set={int(x) for x in numbers.split()}
perfect_numbers=[n for n in num_set if is_perfect(n)]
if perfect_numbers:
    print("perfect numbers from the set are:",perfect_numbers)
else:
    print("No perfect numbers found in the set:")
