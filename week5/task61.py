my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
element = int(input("row no: "))

def sum_of_row(matrix,satirindexi):
    secilensatir=matrix[satirindexi]
    sum= 0
    for i in secilensatir:
        sum = sum + i
    return sum
print(sum_of_row(my_matrix,element))
    
    




