sesliharfler= "aeiouAEIOU"
inp=input("cümle?")






def seslimetin(metin):
    sonuc= ""
    for harf  in metin:
        if harf  not in sesliharfler:
            sonuc += harf
    return sonuc

print(seslimetin(inp))