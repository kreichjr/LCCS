import modules.vuerencards as Cards

def check_guess(card, card2, guess):
	delta = card.value - card2.value
	if (
			(delta < 0 and guess == 'higher') or 
			(delta == 0 and guess == 'same') or 
			(delta > 0 and guess == 'lower')):
		print(f"You guessed correctly! The first card was the {card.display_name} and the second was the {card2.display_name} ")
	else:
		print(f"You guessed wrong. The first card was the {card.display_name} and the second was the {card2.display_name} ")

	return True

def main():
	still_playing = True
	deck = Cards.Deck().shuffle()
	
	while still_playing:
		current_card = deck.draw_card()
		following_card = deck.draw_card()
		guessed = False
		player_guess = ''
		valid_guesses = ['higher', 'lower', 'same']

		while not guessed:	
			player_guess = input(f'\nThe current card is {current_card.display_name}. Will the next card be higher, lower, or the same value? ("higher", "lower", "same") ')
			
			if player_guess in valid_guesses:
				guessed = check_guess(current_card, following_card, player_guess)
			else:
				print('\nThat was an invalid guess. Please enter "higher", "lower", or "same".\n')

		answer = ''
		while answer.lower() != 'y' and answer.lower() != 'n':
			
			answer = input('\nDo you want to keep playing? (y/n)  ')

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