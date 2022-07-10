import modules.vuerencards as Cards

def check_guess(card, guess):
	if card.value > guess:
		print('You guessed too low!')
		return False
	if card.value < guess:
		print('You guessed too high')
		return False
	print('You got it!')
	return True

def main():
	still_playing = True
	deck = Cards.Deck().shuffle()
	
	while still_playing:
		current_card = deck.draw_card()
		guessed = False
		player_guess = ''
		valid_guesses = [str(num) for num in range(1,14)]

		while not guessed:	
			player_guess = input('\nPlease guess the value of the drawn card! (1-13) ')
			
			if player_guess in valid_guesses:
				guessed = check_guess(current_card, int(player_guess))
			else:
				print('\nThat was an invalid guess. Please enter a value of 1 through 13.\n')

		answer = ''
		while answer.lower() != 'y' and answer.lower() != 'n':
			
			answer = input('\nDo you want to keep playing? y/N  ')

			if answer.lower() == 'y':
				print(f'Remaining cards in the deck: {len(deck)}')
				if len(deck) == 0:
					print('\n\nShuffling the deck...\n\n')
					deck.create_standard_deck().shuffle()
			elif answer.lower() == 'n':
				still_playing = False
			else:
				print('Invalid input. Please enter \'y\' or \'n\'... ')

	print('\n\nThank you for playing!\n')
	

if __name__ == "__main__":
	main()