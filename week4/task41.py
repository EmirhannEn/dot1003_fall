def my_longer(a,b):
    if len(a) > len(b):
        return a
    elif len(a) == len(b):
        print("Their length are same")
    else:
        return b
    
print(my_longer("emirhan","yavuz"))
    