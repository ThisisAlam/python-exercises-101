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

with open("notes.txt","w") as file:
    result= file.write("python")
    print(result)
print(result)

with open("justice.txt","w") as file:
    file.write("Batman")
    file.write("Superman")
