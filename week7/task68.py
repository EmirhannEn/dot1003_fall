my_coordinates = {}
my_coordinates[(0,0)] = "home"
my_coordinates[(1,1)] = "work"
my_coordinates[(-1,-1)] = "school"

def coordinator(x,y):
    my_coordinates = coordinator(x,y)
    return (x,y)

for k,v in my_coordinates.items():
 print(f"position: {k} name: {v}")

