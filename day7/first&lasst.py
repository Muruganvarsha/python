s=input("Enter the string:")
s="".join([i for i in s if not i.isdigit()])
s=s[0].upper()+s[1:-1]+s[-1].upper()
print(s)
