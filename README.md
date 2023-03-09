# Python Blackjack Game
This is a Python implementation of the classic card game Blackjack, built in VScode using the Pygame, Random, and Math Python libraries.

# Game Rules
The objective of Blackjack is to have a hand value of 21 or as close to 21 as possible without going over. Each card in the deck has a value. Number cards are worth their face value, face cards (Kings, Queens, and Jacks) are worth 10, and Aces can be worth 1 or 11, depending on which value would be more beneficial to the player.

At the start of the game, each player (including the dealer) is dealt two cards. The player's cards are dealt face up, while one of the dealer's cards is dealt face down (known as the hole card).

Players then have the option to hit (take another card), stand (keep their current hand value), double down (double their bet and receive one more card), or split (if they have a pair of cards with the same value, they can split them into two separate hands).

The dealer must hit until they have a hand value of 17 or higher. If the dealer's hand value exceeds 21, they bust and all remaining players win.

# Features
- Multi Deck Shoe: The game uses multiple decks of cards, which are shuffled together at the start of each round.
- Double Down Functionality: Players can choose to double their bet and receive one more card.
- Multi Ace auto value: The game automatically assigns the best value for Aces in a player's hand (either 1 or 11).
- Dealer hits on x: The dealer must hit until they have a hand value of 17 or higher.
- Error Handling
# Dependencies
Pygame
Random
Math
# How to Play
To run the game, run the blackjack.py file in your Python environment.

Once the game is started, follow the on-screen instructions to play.

Good luck, and have fun!

# Change Log
- 0.0 -> Initial Release [@LakshmanChelliah](https://github.com/LakshmanChelliah)
- 0.1 -> Bug Fixes and Error Handling [@DylanDominic](https://github.com/DylanD2402)
- 0.2 -> Added Delays when Dealer Hits, Added Count to Players Hand, Added Comments [@LakshmanChelliah](https://github.com/LakshmanChelliah)
