def age_calc():
    
    soru=int(input("yaş kaç"))
    return soru
    
    
    
    
başlat = True
while başlat:
        try:
           
           print(f"you are {age_calc()} years old")
           başlat = False
        except ValueError:
            print("İnvalid input")