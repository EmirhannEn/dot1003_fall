my_dictionary = {}

my_dictionary["item1"] = 3
my_dictionary["item2"] = 1
my_dictionary["item3"] = 5




def remove_item(item,çikti):
    if item in my_dictionary:
        my_dictionary[item] = my_dictionary[item] - çikti
        if my_dictionary[item] <= 0:
            del my_dictionary[item]
    










remove_item("item1",4)
print(my_dictionary)
    
    

    
    
        
