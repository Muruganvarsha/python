username=input("Enter the username:",)
email=input("Enter the email id:",)
print("Validation results")
if len(username)>3:
    print("username is valid")
else:
    print("username is invalid")
if "@" in email and "." in email:
    print("email is valid")
else:
    print("email is invalid")
