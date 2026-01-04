weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]

def print_best_weapon(weapon_list):
    current_max_danage= 0
    best_weapon_name = " "

    for weapon in weapon_list:
        damage = weapon[1]
        name= weapon[0]

        if damage > current_max_danage:
            current_max_danage = damage
            best_weapon_name = name
    print(best_weapon_name)

print_best_weapon(meele_weapon)


