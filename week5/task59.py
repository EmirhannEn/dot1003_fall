gamelist=["Doom", "Max Payne", "FTL"]


def longest_name(liste):
    en_uzun =  liste[0]
    for eleman in liste:
        if len(eleman) > len(en_uzun):
            en_uzun=eleman
            return en_uzun
print(gamelist)
print(longest_name(gamelist))
        


