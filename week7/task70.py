def coordinator(x, y):
    return (x, y)

# 3x3'lük oyun tahtamızı (liste içinde liste) oluşturuyoruz
# Başlangıçta hepsi alt çizgi (_)
game_table = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

user_inputs = []  # Kullanıcının girdiği koordinatları burada saklayacağız

while True:
    command = input("Please type new or exit: ")
    
    if command == "exit":
        break  # Döngüden çık ve çizim kısmına geç
        
    elif command == "new":
        # Kullanıcıdan x ve y değerlerini al
        # Not: Listelerde indeksler int olmalı, o yüzden int() kullanıyoruz
        x = int(input("Please enter x: "))
        y = int(input("Please enter y: "))
        
        # coordinator fonksiyonunu kullanarak tuple oluştur ve listeye ekle
        coord_tuple = coordinator(x, y)
        user_inputs.append(coord_tuple)

# --- Döngü bitti, şimdi tahtayı güncelleme zamanı ---

# user_inputs listesindeki her bir koordinat (tuple) için işlem yap
for coord in user_inputs:
    # coord[0] -> x değeri (satır)
    # coord[1] -> y değeri (sütun)
    r = coord[0]
    c = coord[1]
    
    # Tahtadaki o noktayı yıldıza çevir
    game_table[r][c] = "*"

# --- Sonucu Ekrana Yazdır ---
print("\n--- Game Board ---")
for row in game_table:
    print(row)

