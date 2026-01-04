def ladinagacı():
    h=int(input("yükseklik giriniz"))
    box=int(input("box size giriniz"))
    box *=2

    if box < h*2-1:
        print("box size h ın en az iki katı olmalı")
    

    print("-"*box)

    for i in range(1,h+1):
        yıldızsayisi=2*i-1
        bosluksayısı=" " *(h-i)
        yıldızlar = bosluksayısı + "*"* yıldızsayisi
        solboşluk= yıldızlar + " "*(box-len(yıldızlar) )
        sapbosluğu=" "*(h-1)
        sapsolbosluğu= sapbosluğu + "*" + " "*(box-len(sapbosluğu))
        print("| " + solboşluk + " |")
    print("| " + sapsolbosluğu + " |")



ladinagacı()

        
        


