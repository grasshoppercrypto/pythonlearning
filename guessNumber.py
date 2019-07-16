import random


print('Hello, what is your name?')
name = input()

print('Well, '+name+', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)


for guessesTaken in range(1,7) :
	print('Take a guess.')
	try:
		guessNumber = int(input())
		if guessNumber < secretNumber:
			print('Your guess is too low.')
		elif guessNumber > secretNumber:
			print('Your guess is too high.')
		else:
			break # This condition is for the correct guess!
	except ValueError:
		print('You need to type in number, you only have '+str(6-guessesTaken)+' chances left')
	

if guessNumber == secretNumber: 
	print('Good job, ' + name+'! You guessed my number in ' + str(guessesTaken)+' numbers!')
else:
	print('The number i was thinking of was ' + str(secretNumber))
