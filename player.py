from deck import Deck

class Player:
	def __init__(self, hand=None, current_deck=Deck()):
		self.current_deck = current_deck
		self.hand = [] if hand is None else hand

	def get_my_hand(self, hand):
		self.hand = hand

	def add(self, card):
		self.hand.append(card)

	def play_one_card(self, played_arr):
		trump = self.current_deck.current_trump
		card_index = int(raw_input("What card would you like to play?\n"))
		while card_index > len(self.hand):
			card_index = int(raw_input("You don't have that many cards in your hand! Pick a valid card to play:\n"))
		# If you are not the first person to play, make sure you can only play valid cards
		if len(played_arr) > 0:
			has = False
			for card in self.hand:
				if card.suite == played_arr[0][0].suite:
					has = True
			if has:
				while self.hand[card_index - 1].suite != (played_arr[0][0].suite or trump):
					card_index = int(raw_input("Invalid card to play! Try another card\n"))
		return self.hand.pop(card_index - 1)

	def swap(self, my_card, foreign_card):
		self.hand.append(foreign_card)
		self.hand.remove(my_card)