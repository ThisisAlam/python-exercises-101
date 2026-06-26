# 🏁 Pit Stop Timing Optimizer 🔧
#
# Ask the user for the total race time in seconds.
total_race_time = float(input('What is the total race time in seconds(s)? '))
# Ask how many pit stops were made.
total_number_of_pit_stops= int(input('How many pit stops were made? '))
# Ask for the average pit stop duration (in seconds).
avg_time_inside_one_pit= float(input('what is the average pit stop duration in seconds(s)? '))

#
# Then:
# - Calculate the total pit stop time.
total_pit_stop_time= total_number_of_pit_stops * avg_time_inside_one_pit
# - Calculate the percentage of the race spent in the pits.
percentage_of_race_time_in_pit= float(total_pit_stop_time/total_race_time)*100
# - Round the percentage to 2 decimal places.
percentage_of_race_time_in_pit_round= round(percentage_of_race_time_in_pit,2)
#
# Finally, print all of the following:
# - Total pit stop time in seconds
print(f'{total_pit_stop_time}s')
# - Percentage of race time spent in pits
print(f'{percentage_of_race_time_in_pit_round}')
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"
if(percentage_of_race_time_in_pit_round>5):
    print("You need a new pit crew. 🛠️")