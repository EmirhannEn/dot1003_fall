my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
element = int(input("coulmm no: "))

def sum_of_coulmm(matrix,sutun_indeksi):
    toplam= 0
    for satir in matrix:
        toplam = toplam + satir[sutun_indeksi]
    return toplam

print(sum_of_coulmm(my_matrix,element))


    