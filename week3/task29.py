şifre= "1234567"
cauntdown= 3 
başlat =True

while başlat:
    password=input("password")
    cauntdown= cauntdown - 1
    if cauntdown==0:
        print("şifre kilit")
        başlat= False
    elif şifre != password:
        
        print("try again")
    else:
        başlat=False
        print("welcome")

