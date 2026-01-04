name=input("What are you looking for?")
cumle="The quick brown fox jumps over the lazy dog"
if cumle.find(name) >=0 :
    print(f"found it at {cumle.find(name)}")
elif name == "-1" :
    print("Bye.")
else:
    print("not found") 