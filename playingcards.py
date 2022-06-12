from enum import Enum, auto

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


	def _create_deck(self):
		deck = []

		for new_suit in Suit:
			for value in range(1, 14):
				deck.append(Card(new_suit, value))

		return deck

	def print_cards(self):
		for card in self.deck:
			print(card)

			
