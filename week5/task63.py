my_lucky_numbers = [4,8,15,16,23,42]
my_triple_numbers = []



def tripler(liste):
    for i in liste:
        new_number = 3 * i
        my_triple_numbers.append(new_number)
    return my_triple_numbers

print(my_lucky_numbers)
print(tripler(my_lucky_numbers))
    