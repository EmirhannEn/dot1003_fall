def finder(file_name):
    open(file_name,"r")
    ans = max(file_name)
    return ans
print(f"biggest {finder("random_numbers.txt")}")
