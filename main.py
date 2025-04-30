import json

# read `expenses.json`
with open("expenses.json", "r") as pet_store:
    whole_thing = json.load(pet_store)

# get and print total "price" for all expenses at the "pet store"

#stuff = whole_thing["pet store"]
#print(stuff)
total = 0
something = whole_thing["pet store"]
for stuff in something:
    total += stuff["price"]
print(total)