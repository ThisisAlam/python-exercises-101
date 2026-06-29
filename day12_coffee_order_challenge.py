# ☕ Coffee Order Queue Challenge

# 1. Set up two variables: one for total price, one for drink count
total_price= 0 
drink_count= 0
print("Drinks available: latte, americano, espresso")
order= input("Would you like to add another drink? (yes/done) ")
def reorder():
    drink_count += 1
    print(f'Total Price: {total_price} and Drinks: {drink_count}')
    order= input("Would you like to add another drink? (yes/done) ")

# 2. Start a while True loop
while order != 'done':
    drink_order= input("Add a drink in the order: ")
    if drink_order == "latte":
        total_price += 3.50
        drink_count += 1
        print(f'Total Price: {total_price} and Drinks: {drink_count}')
        order= input("Would you like to add another drink? (yes/done) ")
    elif drink_order == "americano":
        total_price += 3.00
        drink_count += 1
        print(f'Total Price: {total_price} and Drinks: {drink_count}')
        order= input("Would you like to add another drink? (yes/done) ")
    elif drink_order == "espresso":
        total_price += 2.50
        drink_count += 1
        print(f'Total Price: {total_price} and Drinks: {drink_count}')
        order= input("Would you like to add another drink? (yes/done) ")
    else:
        print("Not in menu. Select from the menu again")
        order= input("Would you like to add another drink? (yes/done) ")
print("Here's your complete order:")
print(f"Total drinks: {drink_count}")
print(f"Total Price of the order: {total_price}")
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price