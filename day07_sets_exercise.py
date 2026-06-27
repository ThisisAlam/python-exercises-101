friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
if('Eric' in friends and 'John' in friends):
    print('Eric and John are present in Friends')

#2. combine or add the two sets 
all_friends = friends.union(my_friends)
print("Union/Combine: ", all_friends)

#3. Find names that are in both sets
common_friends=friends.intersection(my_friends)
print("Mutual/Common names: ", common_friends)

#4. find names that are only in friends
unique_in_friends= friends.difference(my_friends)
print('Unique friends: ',unique_in_friends) 

#5. Show only the names who only appear in one of the lists
only_unique_in_friends= friends.symmetric_difference(my_friends)
print('Names unique to the lists: ',only_unique_in_friends)

#6. Create a new cars-list without duplicates
cars_list=set(cars)
print('Cars with no duplicates: ',cars_list)