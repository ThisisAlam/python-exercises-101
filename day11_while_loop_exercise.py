print('Guessing game') 
# Guess the correct number in 3 guesses. 
# If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, 
# so If you want to see prints during whle loop, then print to the input box
word= input("Guess the word: ")
won = False
for i in range(1,4):
    if word == "python":
        print("Congratulations: You have made the correct guess ^_^")
        won = True
        break
    elif word != "python":
        print("Incorrect guess :(")
        print("Hint: Its a computer snake.")
        word= input("Make another guess: ") 
if not won:
    print("You lost the game")
    print("The user never guessed the correct word: python")

#Modification 1: number 1-100, tell user if guess is too high/low,
# and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, 
# so If you want to see prints during whle loop, 
# print to the input box (This is specific to this platform)

# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 