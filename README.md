LCCS Round 2

Info:
This is the first part of a small challenge series done for the LexicalScoped Community
This is designed to practice and showcase our skills, while also demonstrating the diversity that can be found when multiple programmers attempt a single challenge.

Limitations
In order to keep the playground as simplified as possible we will be limiting things to the following:
Language: Python 3 (up to and including 3.10)
Operating System assumed will be Windows 10 (do not use system commands for other operating systems or you risk issues occurring)

Part 2 Objectives:

Without modifying the cards module you got from Round 1 results, create a High-Low-Same guessing game.

Must contain a Function to perform card comparison.
Must keep track of cards remaining and shuffle when we reach the end of the deck or shortly before (up to 5 cards before end of deck is acceptable)
Must validate input is correct, if incorrect must re-request input.
Must prompt after each round if you would like to continue playing or exit.


Game Description:
Draw a card face up (tell the user what the card is)
Ask the User if they think this card will be higher, lower or the same as the next card
Draw a second card, compare the two and determine if the user guessed correctly.

###


LS Code Challenge #1
This will be a multi-part challenge

Information:
This is the first part of a small challenge series done for the LexicalScoped Community
This is designed to practice and showcase our skills, while also demonstrating the diversity that can be found when multiple programmers attempt a single challenge.
Limitations
In order to keep the playground as simplified as possible we will be limiting things to the following: Language: Python 3 (up to and including 3.10)
Operating System assumed will be Windows 10 (do not use system commands for other operating systems or you risk issues occurring)
Part 1 Objectives
Develop a module to handle Playing Cards
Need to define cards to contain 
•	name (String > value, except for 1 (Ace) 11 (Jack), 12 (Queen), 13 (King))
•	value (integer >  1 to 13)
•	suit (String > Spades, Clubs, Hearts, Diamonds)
Need to define Deck:
•	Contain Cards in Deck
•	Contain Cards that have been drawn (in use/discard pile)
Need build functions or methods to handle the following:
•	Shuffle (adding the in use/discards back into the deck and randomize)
•	Draw (pull card from top of Cards in Deck, put the card in the “in use/discard pile” and return the card object to where-ever the “draw” was called from)

Requirements:
Need to be able to work with the Deck, Shuffle and Draw functions outside of the module.  Need a Comment section at the top of the module to outline the creator and basic instructions on what the method calls are to create deck, shuffle deck and draw from deck.

