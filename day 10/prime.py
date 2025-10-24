def is_prime(n):
    if n<2:
        return false
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return false
        return true
numbers=int(input("Enter the number:"))
numbers.split()
prime_count=sum(1 for num in numbers if is_prime(num))
print(f"The of prome nubers in the set is:{prime-count}")
