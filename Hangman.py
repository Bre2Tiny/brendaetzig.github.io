word = "Halloween"
progress = ""
guesses = []

for i in range(len(word)):
	progress += "_"

print(progress)

word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guesses = []
maxfails = 5

lives= 5

while(lives > 0):
	  guess = input("Guess a letter: ")

	  if guess in guesses:
		  print("already guessed")
	  else:
		  guesses.append(guess)
		  #replace the proper underscore with
          #with the correct guess
          index = word.find(guess)
		  if index == -1:
			  #character not found in words
          print("Guess is incorrect")
		  lives -= 1
