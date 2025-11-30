şifre=input("pls enter your password")
password = True

while password:
    match=input("enter again")
    if şifre != match:
        print("they are not same")
    else:
        password=False
        print("Your password matches and account created successfully")
