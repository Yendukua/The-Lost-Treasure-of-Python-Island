print("Hello, welcome")

name = input("Please may i know your name: ")

print("Hello,nice to meet you!", name)

age = int(input(f"{name} How old are you?: "))

color = input("What is your favorite color?: ")

animal = input("What is your favorite animal?: ")

pirate_name = (name + animal[0:3] + color[-3:])

print(f"Your pirate name is: {pirate_name}")

gold_coins = int(input(f"{name}, how many gold coins did you find?: "))

print(gold_coins, "gold coins is a lot of treasure! You are rich!")

number_of_pirates = int(input(f"{name}, what is the total number of pirates in your crew including yourself?: "))

each_pirate_share = int(gold_coins / number_of_pirates)

print(f"Each pirate will get {each_pirate_share} gold coins!")

if each_pirate_share >= 15 : 
    
    print("Yes, each pirate gets at least 15 gold coins 😁🥳!")

else: 
    
    print("No, each pirate does not get at least 15 gold coins  😢😭!")

items = ["sword", "compass", "map", "key", "latern"]

for item in items:

    print(item)

print(len(items), "items in the treasure chest!")

gold_coins = int(input("how many gold coins did you find?: "))

silver_coins = int(input("how many silver coins did you find?: "))

total_coins = gold_coins + silver_coins

if gold_coins > silver_coins:

    print("difference between gold coins and silver coins is")
    
    difference = gold_coins - silver_coins

    print(difference)

else:

    print("difference between silver coins and gold coins is")

    difference = silver_coins - gold_coins

    print(difference)

product = gold_coins * silver_coins

print("product of gold coins and silver coins is", product)

if gold_coins > silver_coins:

    print("gold coins divide by silver coins is")
    
    division = gold_coins / silver_coins

    print(division)

else:

    print("silver coins divide by gold coins is")

    division = silver_coins / gold_coins

    print(division)

print("gold coins are:",gold_coins)

print("silver coins are:",silver_coins)

print("total coins are:",total_coins)

for item in items:

    print(item)

print(len(items), "items in the treasure chest!")