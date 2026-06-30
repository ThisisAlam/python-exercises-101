# file = open("heroes.txt")

# heroes = file.readlines()

# for hero in heroes:
#     print(hero.strip())

# file.close()

# with open("heroes.txt") as file:
#     heroes= file.readlines()
#     for hero in heroes:
#         print(hero.strip()) 
# print("\nFinished\n\n")

# with open("heroes.txt") as file:
#     print(file.readline().strip())
# print(file.closed)
# print(file.readline())

# with open("notes.txt","w") as file:
#     result= file.write("python")
#     print(result)
# print(result)

# with open("justice.txt","w") as file:
#     file.write("Batman")
#     file.write("Superman")


cart = {
    "iron sword": {
        "price": 120,
        "description": "A reliable sword."
    },
    "bread": {
        "price": 5,
        "description": "Freshly baked."
    }
}
with open("cart.txt", "a") as file:
    file.write(f"{'=' * 30}\n")
    file.write("SHOPPING CART\n")
    file.write(f"{'=' * 30}\n")
    for key, value in cart.items():
        file.write(f"Item: {key}\n")
        file.write(f"Price: {value['price']}\n")
        file.write(f"Description: {value['description']}\n")
        file.write("-" * 30 + "\n\n")