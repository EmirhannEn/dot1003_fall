hourly_wage=float(input("Hourly wage:"))
hours_worked=int(input("Hours worked:"))
day_of=input("Day of the week:")
daily_wages=hourly_wage*hours_worked

print(f"Hourly wage:{hourly_wage}")
print(f"Hours worked:{hours_worked}"),
print(f"Day of the week:{day_of}")

if day_of == "sunday":
    daily_wages=daily_wages*2
    print(f"daily wages {daily_wages}")

