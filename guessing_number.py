import random

def guessing_game(guessLimit, number):
	random_number = random.randint(1, number)
	try:
		while guessLimit > 0:
			guess = int(input("What is your guess? : "))
			guessLimit -= 1
			if random_number == guess:
				print('Congrats, You got it right!')
				break
			elif guess > number:
				print('Your Guess is out of range!')
				print(f'You have {guessLimit} guess(es) left...')
			elif guess > random_number:
				print('Your Guess is bigger!')
				print(f'You have {guessLimit} guess(es) left...')
			elif guess < random_number:
				print('Your Guess is smaller!')
				print(f'You have {guessLimit} guess(es) left...')
		print('Game Over!!')
		print(f'The random number was {random_number}.')
	except ValueError:
		print('Only integers are allowed!')

def easy():
	print("You have to guess a number between 1 and 10, and you have 6 guesses...")
	guessing_game(6, 10)

def medium():
	print("You have to guess a number between 1 and 20, and you have 4 guesses...")
	guessing_game(4, 20)

def hard():
	print("You have to guess a number between 1 and 40, and you have 3 guesses...")
	guessing_game(3, 40)

def try_again():
	again = input('Do you want to play again? Yes/No : ')
	if again.upper() == 'YES':
		welcome()
	elif again.upper() == 'NO':
		print('Thanks for playing.')
	else:
		print('Wrong input!!')
		try_again()

def welcome():
	print('Welcome to the guessing game...')
	difficulty = input("Choose your level between Easy, Medium and Hard : ")
	if difficulty.upper() == "EASY":
		easy()
		try_again()
	elif difficulty.upper() == "MEDIUM":
		medium()
		try_again()
	elif difficulty.upper() == "HARD":
		hard()
		try_again()
	else:
		print("This is Wrong input!!!")
		welcome()

if __name__ == "__main__":
	welcome()

