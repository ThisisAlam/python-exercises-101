
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = [] #'Exercise: fill me with names'
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# csv1= csv.replace(':',',')
# csv2= csv1.replace(';',',')
# csv_list= csv2.split(',')
# friends_list= csv_list.copy()
# use print() statements to work your way through the exercise
friends_list=(
    csv.replace(':',',')
    .replace(';',',')
    .split(',')
)
print(friends_list)

