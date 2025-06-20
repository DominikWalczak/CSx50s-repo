m = input("What's the mass in kg which you want to switch to jules? ")
if m.isdigit():
    m = int(m)
    m = m*pow((3*pow(10, 8)), 2)
    print(f"Amount of Jules is {m}")
else:
    print("You gotta give me a digit nothing else")

