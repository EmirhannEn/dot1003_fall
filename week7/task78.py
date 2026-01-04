def new_game():
    name = input("Game name: ")
    # Kural: Boş isim veya 40 karakterden uzun isim [cite: 443, 444]
    if name == "" or len(name) > 40:
        raise ValueError("Invalid name!") 

    year = int(input("Release year: "))
    # Kural: Negatif yıl veya 2024'ten büyük yıl [cite: 445, 446]
    if year < 0 or year > 2024:
        raise ValueError("Invalid year!")

    return (name, year) # Değerleri tuple olarak döndürüyoruz
game_list = []
başlat = True

while başlat:
    hareket = input("add or exit?: ")
    
    if hareket == "add":
        try:
            # Fonksiyonu çağırıyoruz, eğer hata fırlatırsa direkt 'except'e atlar
            yeni_oyun = new_game()
            game_list.append(yeni_oyun)
        except ValueError as e:
            # raise ile fırlattığımız mesajı burada yakalayıp yazdırıyoruz
            print(f"Hata: {e}") 
            
    elif hareket == "exit":
        for game in game_list:
            print(f"Name: {game[0]}, Year: {game[1]}") [cite: 471]
        başlat = False
    


