names=input("Enter the name:")
names.split()
ku_names=[names for name in names if "ku" in names]
print(f'names containing "ku": {ku_names}')
print(f'number of names of contining "ku":{len(ku_names)}')
