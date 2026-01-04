def ask_name():
    my_ans = ""
    return input("Please enter a character from Lord of the Rings")

def ask_age():
    my_ans = int(input(f"How old are {name}: "))
    return my_ans

real_age = 55000
name = ask_name()
question = f"Here is the questions about {name}"
print("")
user_guess = ask_age()
if real_age == user_guess:
    my_ans = "You’re Right"
    print(my_ans)
else:
    print("Nope") 