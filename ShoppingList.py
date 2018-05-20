pasta_bake = ['penne pasta', 'creamy tomato sauce', 'cheese']
steak = ['sirlion steak', 'potatoes', 'pepper sauce', 'carrots']
burger_and_chips = ['quarter pounders', 'cheese', 'potatoes', 'onions', 'tomato']

print ("What would you like to cook on the weekend?")
print ("Here are the options:")
print ("1. Pasta Bake")
print ("2. Steak")
print ("3. Burger & Chips")

choose = input("> ")

if choose == '1':
    print ("Buy", ", ".join(pasta_bake) + "." )

elif choose == '2':
    print ("Buy", ", ".join(steak) + ".")

elif choose == '3':
    print ("Buy", ", ".join(burger_and_chips) + ".")

else:
    print ("Hmmm. No such food on the list.")