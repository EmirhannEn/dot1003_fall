

game_list=[]




liste = True
while liste:
    games=input("oyun adi?")
    if games != "exit":
         game_list.append(games)
    else:
        liste=False
        print(game_list)

def anarya(tersten):
    game_list = tersten[::-1]
    return game_list
    
print(anarya(game_list))
print(game_list)




    





