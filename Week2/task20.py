yil=int(input("Please type in a year: "))
if yil % 400 == 0 :
    print("leap")
elif yil % 100 == 0 :
    print("not leep")
elif yil % 4 == 0 :
    print("leap")