my_sett= set()

döngü = True

while döngü:
    soru=input("pls enter eleman")
    if soru in my_sett:
        print("zaten var")
    elif soru != "exit":
        my_sett.add(soru)
    else:
        print(my_sett)
        döngü= False