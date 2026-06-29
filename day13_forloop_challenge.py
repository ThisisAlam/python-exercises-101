# 🐍 For Loops – Exercise
# Party Invitation

# You're having a party and want to invite your friends.
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
all_names= (names+names1)
friends=[]
print(f"These are the people who are already selected for invitation at the party!")
for people in all_names:
    # print(f'{people.lower().title()}')
    friends.append(people.lower().title())
print(friends)
# Requirements
# You want to print out an invitation for each friend using for loops.

# The names are stored in two lists:
# names
# names1
# When the program runs, ask the user to enter two additional names using input().
invitation= input("Enter more friends names for invitation: (seperated with comma 'A , B') ")
# Add those two names to the list(s).
friends.extend(invitation.split(', '))
# Print one invitation per line.
for friend in friends:
# Make sure each person's name is properly capitalized.
    print(f'{friend.title()}! You are invited to the party on Saturday')

# Example Output
# John Cleese! You are invited to the party on Saturday.
# Eric Idle! You are invited to the party on Saturday.

