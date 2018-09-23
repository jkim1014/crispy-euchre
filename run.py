from deck import Deck
from hand import Hand
from bot import Bot
from player import Player
import random

def main():
	# Randomly decide position
	positions = [1, 2, 3, 4]
	random_deals = [2, 3]
	my_position = random.choice(positions)

	# Take input from user
	print "Welcome to Crispy Euchre!"
	num_cards_deck = int(raw_input("How many cards should we play with?"))

	# Make deck
	game_deck = Deck(14 - num_cards_deck + 1, 14, 0)
	game_deck.shuffle()

	# Make game players
	players_arr = []
	bot_1 = Bot(None, game_deck)
	players_arr.append(bot_1)
	bot_2 = Bot(None, game_deck)
	players_arr.append(bot_2)
	bot_3 = Bot(None, game_deck)
	players_arr.append(bot_3)
	me = Player()
	players_arr.insert(my_position-1, me)

	# First round of dealing
	for i in range(4):
		hand = Hand()
		random_index = randrange(len(random_deals))
		for j in range(random_deals[random_index]):
			card_dealt = game_deck.deal()
			hand.cards.get_card(card_dealt)
		if (my_position == i):
			me.get_my_hand(hand)
		else:	
			players_arr[i].get_my_hand(hand)

	# Second round of dealing
	for player in players_arr:
		for x in range(5 - len(player.hand)):
			card_dealt = game_deck.deal()
			player.hand.add(card_dealt)


	# Second round of dealing
if__name__== "__main__":
	main()