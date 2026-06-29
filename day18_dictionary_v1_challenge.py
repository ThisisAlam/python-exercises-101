#It’s...not really an adventure game...#Ver 1.0

#Your village is being attacked by 'a germanic tribe' 
# and you need to run to the stores and get the right things to save 
# your village, and probably some good looking girl or boy you want to marry. 
# All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!

#The code should allow you to get 1 thing from each store and each item 
# you get should be removed from the store inventory, then do same for 
# next store...

# one way to buy by typing the key 'newt' in an input box...or something

# at end you should print the 'items' you have taken..in this version you 
# don't have to pay for stuff or add it up 

#ver 1.2 add ability to exit a store without buying and go to next by 
# typing 'exit', and to exit if a nonexistant item is bought(typed)

#Add purse with 1000 gold pieces and payment for the items during or at 
# end of code and show a message about total cost and how much gold 
# you have left

#ver 1.4 random bug fix, ' browser compatability', refactoring code... 
# basically being lazy ..stop scrolling TikTok/Facebook! ;-)

#Ver 1.5 print inventory before and after purchases as one department_store 
# of stuff(combine inventories from all stores into one...pretend Big Biz 
# bought all the local stores, and want constant reporting for 
# inventory management...)

# as in all games there is a special way to do this that actually makes 
# money and solves the problem...can you find 'them'? Do you know why? 
# May require knowledge of actual python 'lore'
weapon_shop = {
    "iron sword": {
        "price": 120,
        "description": "A reliable sword forged from iron."
    },
    "battle axe": {
        "price": 180,
        "description": "Heavy axe capable of crushing armor."
    },
    "long bow": {
        "price": 150,
        "description": "A bow with excellent range."
    },
    "steel dagger": {
        "price": 80,
        "description": "Small but deadly in close combat."
    },
    "war hammer": {
        "price": 220,
        "description": "A massive hammer for powerful attacks."
    }
}

magic_shop = {
    "health potion": {
        "price": 50,
        "description": "Restores health instantly."
    },
    "mana potion": {
        "price": 45,
        "description": "Restores magical energy."
    },
    "fire scroll": {
        "price": 130,
        "description": "Casts a powerful fire spell."
    },
    "teleport rune": {
        "price": 250,
        "description": "Teleports you to a safe location."
    },
    "wizard staff": {
        "price": 300,
        "description": "Increases spell power."
    }
}

food_market = {
    "bread": {
        "price": 5,
        "description": "Freshly baked village bread."
    },
    "cheese": {
        "price": 12,
        "description": "A wheel of aged cheese."
    },
    "roasted chicken": {
        "price": 35,
        "description": "Perfect meal for a hungry traveler."
    },
    "apple": {
        "price": 3,
        "description": "A sweet red apple."
    },
    "honey": {
        "price": 20,
        "description": "Pure forest honey."
    }
}

pet_shop = {
    "wolf pup": {
        "price": 400,
        "description": "A loyal companion in battle."
    },
    "falcon": {
        "price": 350,
        "description": "Can scout enemies from the sky."
    },
    "black horse": {
        "price": 500,
        "description": "Fast and fearless."
    },
    "orange cat": {
        "price": 40,
        "description": "Keeps rats away from your house."
    },
    "white rabbit": {
        "price": 15,
        "description": "Cute and harmless."
    }
}

blacksmith = {
    "iron shield": {
        "price": 140,
        "description": "Protects against enemy attacks."
    },
    "steel helmet": {
        "price": 110,
        "description": "Protects your head in battle."
    },
    "chainmail armor": {
        "price": 280,
        "description": "Strong armor made of steel rings."
    },
    "boots": {
        "price": 60,
        "description": "Comfortable boots for long journeys."
    },
    "gauntlets": {
        "price": 90,
        "description": "Protective gloves made of steel."
    }
}

def remove_item_from_store(store, wealth, cart):
    print("\nLIST OF ITEMS IN STORE")
    for key,value in store.items():
        print(f" name: {key} | Price: {value["price"]} | description: {value["description"]}")
    item_from_store = input("\nEnter the item name to buy (or type 'exit'): ").lower()
    if item_from_store == "exit":
        print("You exit from the store")
        return wealth
    else:
        if item_from_store not in store:
            print(f"\n'{item_from_store}' is not available in this store.")
            return remove_item_from_store(store, wealth, cart)
        else:
            removed_item= store.pop(item_from_store)
            cart[item_from_store] = removed_item
            wealth -= removed_item["price"]
            print("\nItem Purchased")
            print(f"Name        : {item_from_store}")
            print(f"Price       : {removed_item['price']}")
            print(f"Description : {removed_item['description']}")
            print(f"Gold Left   : {wealth}")
            return wealth

cart={}
wealth= 1000

print(f"\nStarting Gold: {wealth}")

wealth = remove_item_from_store(weapon_shop, wealth, cart)
wealth = remove_item_from_store(magic_shop, wealth, cart)
wealth = remove_item_from_store(food_market, wealth, cart)
wealth = remove_item_from_store(pet_shop, wealth, cart)
wealth = remove_item_from_store(blacksmith, wealth, cart)

print("\n" + "=" * 40)
print("SHOPPING CART")
print("=" * 40)

total_spent = 0

for item, details in cart.items():
    print(f"{item:<20} {details['price']} gold")
    total_spent += details["price"]

print("-" * 40)
print(f"Total Spent : {total_spent} gold")
print(f"Gold Left   : {wealth} gold")
