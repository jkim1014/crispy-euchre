from collections import Counter
from deck import Deck

class Bot:
	def __init__(self, hand=None, current_deck=Deck()):
		self.current_deck = current_deck
		self.hand = [] if hand is None else hand

	def get_my_hand(self, hand):
		self.hand = hand
		
	def play_one_card(self, played_arr):
		trump = self.current_deck.current_trump
		card_index = len(self.hand)
		for card in self.hand:
			has = False
			if len(played_arr) > 0:
				if card.suite == (played_arr[0][0].suite or trump) or (card.is_high_trump and card.value == 10):
					has = True
			if has:
				while (self.hand[card_index - 1].suite != (played_arr[0][0].suite or trump) or not (self.hand[card_index - 1].is_high_trump and self.hand[card_index - 1].value == 10)) and card_index > 1:
					card_index -= 1
		return self.hand.pop(card_index - 1)

	def add(self, card):
		self.hand.append(card)

	def use(self, card):
		self.hand.remove(card)

	def swap(self, my_card, foreign_card):
		self.hand.append(foreign_card)
		self.hand.remove(my_card)

	def should_swap(self, suite):
		confidence = 0
		for card in self.hand:
			if card.suite == suite:
				confidence += 1
		return confidence >= 2

	def to_swap(self, suite):
		# Arbitrary large values to start the first assignment
		value = 20
		suite = 20
		card_return = None
		for card in self.hand:
			if card.suite != suite and not card.is_high_trump and card.value < value:
				card_return = card
		return card_return

	def call_trump(self):
		confidence = Counter({'1': 0, '2': 0, '3': 0, '4': 0})
		for card in self.hand:
			# If you have a jack in your hand
			if card.value == 10:
				confidence[str(card.suite)] += 14
			else:
				confidence[str(card.suite)] += card.value
		highest_confidence_score = confidence.most_common(1)
		standard = int(len(self.current_deck.deck) / 4)
		# If the value of a suite is at least the value of two median cards of a suite...
		if highest_confidence_score >= 13 + (13 - standard + 1):
			return True, highest_confidence_score[0][0]
		else:
			return False, None