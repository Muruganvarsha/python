names=[]
while True:
    name=input("Enter the name(or type 'stop' to finish):")
    if name.lower()=='stop':
        break
    names.append(name)
print("names entered:",names)
