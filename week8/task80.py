list_size=int(input("List Size:"))
Element_type=input("Element Type:")
mylist=[]

for i in range(list_size):
    if Element_type== "integer":
        import random

        rastgele_sayi = random.randint(0, 99999)
        mylist.append(rastgele_sayi)
    else:
        import random
        random.uniform(0,99999)


print(mylist)




