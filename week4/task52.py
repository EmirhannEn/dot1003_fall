my_list = [1.2345, 2.3456, 3.4567, 4.5678]
new_list=[]




def to_two_decimal(liste):
    for name in liste:
        name1 = "{:.2f}".format(name)
        name3 = float(name1)
        new_list.append(name3)
    return new_list

new_list = to_two_decimal(my_list)
print(new_list)




    
        

    
