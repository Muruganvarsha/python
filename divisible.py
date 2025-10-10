count = 0
sum = 0
for i in range(100, 201):
    if i % 9 == 0:
        count += 1
        sum += i
print("Total numbers divisible by 9:", count)
print("Sum of those numbers:", sum)
