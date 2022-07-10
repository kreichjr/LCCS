from random import shuffle as randshuffle
from random import randint
from math import floor

###################################################################
#                                                                 #
#  Developer: Vueren Kuraenir                                     #
#  Details: This module supplies a Card class and a Deck class.   #
#                                                                 #
#  Card: ((num) val = 0-12, (num) suit_val = 0-3)                 #
#  name - Ace/2/3/4/5/6/7/8/9/10/Jack/Queen/King                  #
#  value - 1/2/3/4/5/6/7/8/9/10/11/12/13 (for comparing)          #
#  suit - Spades/Clubs/Hearts/Diamonds                            #
#  color - Black/Red                                              #
#  display_name - name of suit                                    #
#                                                                 #
#  Deck: ((bool) standard_fill = fill deck with standard cards)   #
#  shuffle - randomizes all cards in the deck                     #
#  create_standard_deck - puts all 52 cards into deck             #
#  draw_card__ - returns & removes card from specified position   #
#  draw_card - returns & removes a card from the top of the deck  #
#  put_card__ - adds card to deck in specified position           #
#                                                                 #
###################################################################

# CONSTANTS
CARD_NAMES = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
CARD_SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
CARD_COLORS = ("Black", "Red")

class Card:
    def __init__(self, val, suit_val):
        if val < 0 or val >= len(CARD_NAMES):
            raise Exception("Card Creation Exception: Name value out of bounds: " + str(val))
        if suit_val < 0 or suit_val >= len(CARD_SUITS):
            raise Exception("Card Creation Exception: Suit value out of bounds: " + str(suit_val))
        
        self.name = CARD_NAMES[val]
        self.value = val + 1
        self.suit = CARD_SUITS[suit_val]
        self.color = CARD_COLORS[floor(suit_val / 2)]
        self.display_name = self.name + " of " + self.suit
        self._display_info = self.display_name + " = " + str(self.value)

class Deck:
    # Shuffle
    def shuffle(self): 
        randshuffle(self.__deck)
        return self
    def _display_info(self): # debug stuff
        accumulator = ""
        for idx,card in enumerate(self.__deck):
            accumulator += str(idx) + ": " + card._display_info
            accumulator += "\n"
        print(accumulator)
    # creates a fresh deck with all 52 cards in order
    def create_standard_deck(self): 
        deck = []
        for suit in range(len(CARD_SUITS)):
            for value in range(len(CARD_NAMES)):
                deck.append(Card(value, suit))
        self.__deck = deck
        return self
    # draw card options
    def draw_card_at(self, index):
        if len(self.__deck) == 0 or abs(index) >= len(self.__deck):
            return None
        return self.__deck.pop(index)
    def draw_card_top(self):
        return self.draw_card_at(0)
    def draw_card_bottom(self):
        return self.draw_card_at(-1)
    def draw_card_random(self):
        return self.draw_card_at(randint(0, len(self.__deck) - 1))
    # Draw Card
    def draw_card(self): 
        return self.draw_card_top()
    # put card options
    def put_card_top(self, card):
        self.__deck.insert(0, card)
        return self
    def put_card_bottom(self, card):
        self.__deck.append(card)
        return self
    def put_card_at(self, card, index):
        if index < 0:
            self.put_card_top(card)
        elif index >= len(self.__deck):
            self.put_card_bottom(card)
        else:
            self.__deck.insert(index, card)
        return self
    def put_card_random(self, card):
        self.put_card_at(card, randint(0, len(self.__deck)))
        return self
    # gets number of cards in the deck
    def __len__(self):
        return len(self.__deck)
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < len(self.__deck):
            result = self.__deck[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
    def __init__(self, standard_fill = True):
        self.n = 0
        if standard_fill:
            self.create_standard_deck()
        else:
            self.__deck = []