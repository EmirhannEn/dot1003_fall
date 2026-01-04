file= open("quote_from_bane.txt", "r")

soru=int(input("hangi satırı yazdırmak istersin"))
line= file.readlines(soru)

print(line)