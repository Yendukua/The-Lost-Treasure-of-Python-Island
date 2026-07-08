name = input("Please may i know your name: ")

gold_coins = int(input(f"{name}, how many gold coins did you find?: "))

print(gold_coins, "gold coins is a lot of treasure! You are rich!")

number_of_pirates = int(input(f"{name}, what is the toltal number of pirates in your crew including yourself?: "))

each_pirate_share = int(gold_coins / number_of_pirates)

print(f"Each pirate will get {each_pirate_share} gold coins!")