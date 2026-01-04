girilenmetin=input("Enter the input to search:")
istenenkelime=input("Which item do you want to search?:")



def my_function(inp,word):
    adet = inp.count(word)
    print(f"'{word}' öğesi, '{inp}' içinde {adet} kere bulundu.")


my_function(girilenmetin,istenenkelime)



    


