size=int(input("pls input a tablet size"))
leaf = 1
space = size - 1
space_original = space
spruce = True
lap = 0
while spruce:
   lap = lap + 1
   if size == lap:
     spruce = False
    
   print (space * " " + leaf * "*")
   leaf = leaf + 2
   space = space - 1

print(space_original * " " + "*")