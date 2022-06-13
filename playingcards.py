# Created by Kenneth Reichelderfer Jr
# Date: 6/11/2022
#
# **************************************************************************
# Classes: 
# **************************************************************************
# 
# Suit - Class Enum that represents the suits of playing cards.
#   Valid options:
#     Suit.HEARTS
#     Suit.DIAMONDS
#     Suit.CLUBS
#     Suit.SPADES
#
#   Used by Card class to instantiate a card class with the desired suit.
#   When printed, the Suit will output it's suit with only the first
#   letter capitalized via the __str__ dunder method.
#
# **************************************************************************
# **************************************************************************
# 
# Card - Represents a card - Takes two arguments:
#   1. Suit Class Enum
#   2. An integer value from 1 - 13
#
#   Card objects have three properties:
#     1. Card.suit - This is the Suit Class Enum that is passed to it.
#     2. Card.value - This is the integer value passed to it.
#     3. Card.name - This is a string derived from the value passed to it.
#       - The name matches with the value except in the following cases:
#         1, 10, 11, and 12 - These values convert to "Ace", "Jack",
#         "Queen", and "King" respectively.   
#
#   Example usage: 
#     # This creates the card representing the Ace of Diamonds. 
#     ace_of_diamonds = Card(Suit.DIAMONDS, 1)
#
#     ace_of_diamonds.suit
#     # Returns Suit.DIAMONDS unless used in a string
#     # If used in a string, returns "Diamonds"
#
#     ace_of_diamonds.value
#     # Returns 1
#
#     ace_of_diamonds.name
#     # Returns "Ace"
#
# **************************************************************************
# **************************************************************************
# 
# Deck - Represents a collection of cards - Allows for shuffling and 
#   drawing of cards - Keeps track of cards that are no longer in the deck -
#   On creation, creates 52 Card objects and shuffles them. 
#   Takes no arguments.
#
#   Deck objects have two properties and two methods:
#     # Properties     
#     1. Deck.deck - Represents a list of card objects, 0th index is
#                      the bottom of a face-down deck, last index is
#                      the top of the deck
#     2. Deck.used - Represents a list of card objects that have been
#                      drawn and removed from the deck.
#       
#     # Methods
#     1. Deck.shuffle() - Combines the current Deck.deck and Deck.used into
#                           Deck.deck, clears Deck.used, and randomizes the
#                           order of the card objects in Deck.deck 
#
#     2. Deck.draw() - Removes the last card object from Deck.deck, adds
#                        it to Deck.used, and returns the removed card obj
#                        If Deck.deck has no card objects when called, it
#                        will return None.
#
#   Example usage:
#     # Initializes my_deck as a Deck object and starts with a randomized
#     # deck order
#     my_deck = Deck()
#    
#     my_deck.draw()
#     # Removes the last card object in my_deck.deck, moves it to
#     # my_deck.used, and returns it
#
#     my_deck.shuffle()
#     # All card objects put back into my_deck.deck, my_deck.used is
#     # cleared, and my_deck.deck is re-randomized
#
#     my_deck.deck
#     # Returns a list of card objects that are in the deck
#
#     my_deck.used
#     # Returns a list of card objects that have been drawn
#
# **************************************************************************



from enum import Enum, auto
import random

class InvalidCardSuit(Exception):
	def __init__(self, suit, message="The provided suit is not a valid option. Please use the Suit Class Enum, e.g. Suit.HEARTS"):
		self.suit = suit
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f"{self.suit} -> {self.message}"


class InvalidCardValue(Exception):
	def __init__(self, value, message="The provided value must be between 1-13 inclusive"):
		self.value = value
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f"{self.value} -> {self.message}"


class Suit(Enum):
	HEARTS = auto()
	DIAMONDS = auto()
	CLUBS = auto()
	SPADES = auto()

	def __str__(self):
		return f"{self.name[0]}{self.name[1:].lower()}"

	def __repr__(self):
		return f"Suit.{self.name}"


class Card:
	def __init__(self, suit, value):
		if not isinstance(suit, Suit):
			raise InvalidCardSuit(suit)
		if value not in range(1, 14):
			raise InvalidCardValue(value)
		self.suit = suit
		self.value = value
		self.name = self._get_name(value)

	def _get_name(self, value):
		match value:
			case 1:
				return "Ace"
			case 11:
				return "Jack"
			case 12:
				return "Queen"
			case 13:
				return "King"
			case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
				return f"{value}"

	def __str__(self):
		return f"{self.name} of {self.suit}"

	def __repr__(self):
		return f"Card({repr(self.suit)}, {self.value})"


class Deck:
	def __init__(self):
		self.deck = self._create_deck()
		self.used = []
		self.shuffle()

	def _create_deck(self):
		deck = []
		
		for new_suit in Suit:
			for value in range(1, 14):
				deck.append(Card(new_suit, value))

		return deck

	def _print_cards(self):
		for card in self.deck:
			print(f"{card} is in the deck")
		for card in self.used:
			print(f"{card} is in use")

	def shuffle(self):
		self.deck = self.deck + self.used
		self.used.clear()
		random.shuffle(self.deck)

	def draw(self):
		if len(self.deck) <= 0:
			return None

		drawn_card = self.deck.pop()
		self.used.append(drawn_card)
		# print(f"You drew the {drawn_card}")
		return drawn_card


def main():
	my_deck = Deck()
	my_deck._print_cards()
	input('Press enter to continue...')
	my_deck.draw()
	my_deck.draw()
	my_deck.draw()
	input('Press enter to continue...')
	my_deck._print_cards()
	input('Now, we\'re going to shuffle the deck! Press enter to continue...')
	my_deck.shuffle()
	my_deck._print_cards()


if __name__ == "__main__":
	main()


