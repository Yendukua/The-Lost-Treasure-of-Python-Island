name = input("Please may i know your name: ")

print("Hello,nice to meet you!", name)

age = int(input(f"{name}, how old are you?: "))

color = input("What is your favorite color?: ")

animal = input("What is your favorite animal?: ")

pirate_name = (name + animal[0:3] + color[-3:])

print(f"Your pirate name is: {pirate_name}")
