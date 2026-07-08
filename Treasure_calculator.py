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

    print("gold coins divide by silver gold_coins is")
    
    division = gold_coins / silver_coins

    print(division)

else:

    print("silver coins divide by gold coins is")

    division = silver_coins / gold_coins

    print(division)

print("gold coins are:",gold_coins)

print("silver coins are:",silver_coins)

print("total coins are:",total_coins)









