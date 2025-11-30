my_list=[]

başlat = True


while başlat:
    item=input("enter a item")
    if item == "exit" :
        başlat=False
        print(my_list)
    else:
        my_list.append(item)
