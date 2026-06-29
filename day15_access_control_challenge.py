revoked_badge = {1, 3, 5, 7, 11, 13, 17, 19}

approved = []
denied = []

visitor_info = input("Do you wish to continue? (yes/done) ")

while visitor_info != "done":
    visitor_info = input("Enter name: (name/done) ")

    if visitor_info == "done":
        break

    badge_number = int(input("Please enter valid badge number: "))

    if badge_number in revoked_badge:
        print("Access Denied")
        denied.append(visitor_info)
    else:
        print("Access Granted")
        approved.append(visitor_info)

approved.sort()
denied.sort()

print("List of approved people:")
for i, name in enumerate(approved, start=1):
    print(f"{i}. {name}")

print("List of denied people:")
for i, name in enumerate(denied, start=1):
    print(f"{i}. {name}")

print(f"Total number of approved people: {len(approved)}")
print(f"Total number of denied people: {len(denied)}")