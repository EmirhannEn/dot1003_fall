my_dictionary = {}

my_dictionary["item1"] = 3
my_dictionary["item2"] = 1
my_dictionary["item3"] = 5

item=input("yeni item")
değeri=int(input("sayisi"))

def add_item(add,number):
    if add in my_dictionary:
        my_dictionary[add] = my_dictionary[add] + number
        print(my_dictionary)
    else:
        my_dictionary[add] = number
        print(my_dictionary)
           

add_item(item,değeri)


    