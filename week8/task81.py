def biggest_in_list(new_list):
    ans = max(new_list)
    return ans
def shortest_list(unshorted_list):
    ans= sorted(unshorted_list)
    return ans

my_list = [695735, 169439, 41406, 112517, 457053]

print(f"my bigest {biggest_in_list(my_list)}")
print(f"shorted {shortest_list(my_list)}")