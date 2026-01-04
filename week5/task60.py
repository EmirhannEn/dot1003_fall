my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
element=int((input("item to search?:")))



def founder(liste,arananf):

    for i in range(len(liste)):
        for j in range(len(liste[i])):
            print(liste[i][j])
            if liste[i][j] == arananf:
                print(f"find at row: {i} column: {j}")
                return True
    return False
                

print(founder(my_matrix,element))
    
