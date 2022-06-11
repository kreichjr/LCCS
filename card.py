from enum import Enum, auto

class Suit(Enum):
	HEARTS = auto()
	DIAMONDS = auto()
	CLUBS = auto()
	SPADES = auto()

	def __str__(self):
		return f"{self.name[0]}{self.name[1:].lower()}"


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


print(Suit)
print(Suit.HEARTS)
print(Suit.DIAMONDS)
print(Suit.CLUBS)
print(Suit.SPADES)
