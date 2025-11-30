numero1=(input("Type the first number:"))
numero2=(input("Type the second one: "))

if numero1 > numero2:
    print(f"First one is greater {numero1}>{numero2}")
elif numero1 == numero2:
    print(f"These are equal {numero1}={numero2}")
else:
    print(f"Second one is greater {numero2}>{numero1}")