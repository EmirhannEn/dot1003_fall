total_number=0
sum=0
mean=0
odd=0
even=0

hesaplama=True
while hesaplama:
    sayi=int(input("pls enter a number"))
    if sayi != 0:
        total_number=total_number+1
        sum= sum+ sayi
        mean=sum/total_number
        if sayi % 2 == 0 and sayi !=0 :
            even=even+1
        else :
            odd=odd+1
    else:
        hesaplama = False
print(total_number)
print(sum)
print(mean)
print(odd)
print(even)
