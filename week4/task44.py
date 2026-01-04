name=input("enter a name")
büyüktür= ">"
küçüktür= "<"
line=len(name)
basson= "|"
üstalt= "-"
sayi=(18-line)//2

başlat=True

while başlat:
    if len(name) < 18:
        print(f"{üstalt*20}")
        print(f"{basson}{sayi * büyüktür}{name}{sayi * küçüktür}{basson}")
        print(f"{üstalt*20}")
        başlat=False



