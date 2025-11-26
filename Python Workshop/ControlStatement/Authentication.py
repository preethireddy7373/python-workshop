user_name=input("Enter the usrname:")
if(user_name=="user"):
    print("Username is valid")
    password=input("Enter password:")
    if(password=="user@123"):
        print("Login Successfull")
    else:
        print("Login un Successfull")
else:
    print("Username is not valid")