name=input("Please enter string:")
arayiş=input(">Please enter search item:")
if name.find(arayiş) >= 0 :
    print(f"found{name.find(arayiş)}")
else:
    print("not found")