# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
dog_bus = {
    1: {
        "name": "Buddy",
        "breed": "Golden Retriever",
        "pickup": "08:00 AM",
        "dropoff": "04:00 PM"
    },
    2: {
        "name": "Bella",
        "breed": "Beagle",
        "pickup": "08:15 AM",
        "dropoff": "04:15 PM"
    },
    3: {
        "name": "Max",
        "breed": "German Shepherd",
        "pickup": "08:30 AM",
        "dropoff": "04:30 PM"
    },
    4: {
        "name": "Luna",
        "breed": "Poodle",
        "pickup": "08:45 AM",
        "dropoff": "04:45 PM"
    },
    5: {
        "name": "Charlie",
        "breed": "Labrador",
        "pickup": "09:00 AM",
        "dropoff": "05:00 PM"
    }
}
max_seats= 10
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
while len(dog_bus) < max_seats:
    pet_roster= f"This is the latest pet roster:"
    print(pet_roster)
    for key, value in dog_bus.items():
        print(f"Seat number: {key} | Dog name: {value["name"]} | Pickup time: {value["pickup"]}")

    # 3. Add one new pet if there’s room on the bus.
    #    - Use MAX_SEATS to limit capacity.
    print(f"Currently occupied seats are: {len(dog_bus)}")
    print("MAX_SEATS capacity is 10.")
    print("Add new pet:")
    #    - Dynamically assign the next seat number.  
    if len(dog_bus) < max_seats:
        next_seat = max(dog_bus.keys()) + 1

        pet_name = input("Enter new pet name: ")
        pet_breed = input("Enter pet breed: ")

        dog_bus[next_seat] = {
            "name": pet_name,
            "breed": pet_breed,
            "pickup": "09:00 AM",
            "dropoff": "05:00 PM"
        }
    #    - Print the updated roster showing all pets after pickup.  
    print(pet_roster)
    for key, value in dog_bus.items():
        print(f"Seat number: {key} | Dog name: {value["name"]} | Pickup time: {value["pickup"]}")

    # 4. Ask which pet leaves early.  
    print("Enter the Name of the dog which leaves early! (name|none)")
    removed_pet_name= input("Enter the name: ")
    if removed_pet_name == "none":
        print("No pet has left yet!")
        continue
    else:
        #    - Remove that pet from the bus. 
        seat_to_remove= 0 
        for key, value in dog_bus.items():
            if value["name"] == removed_pet_name:
                seat_to_remove = key
                break
        #    - Print a message saying they’ve headed home.  
        if seat_to_remove:
            dog_bus.pop(seat_to_remove)
            print(f"Pet: {removed_pet_name} on seat: {seat_to_remove} has left for home.")
        else:
            print("Pet not found.")
        # 5. Print a final roster listing the remaining pets and their dropoff times.  
        print("Final roster: ")
        print(pet_roster)
        for key, value in dog_bus.items():
            print(f"Seat number: {key} | Dog name: {value["name"]} | Dropoff time: {value["dropoff"]}")
print("The bus has reached its limit of total 10 seats")