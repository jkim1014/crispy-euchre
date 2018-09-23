# Build custom deck with details specified by user
from card import Card
import random
import math

class Deck:
	def __init__(self, begin_index=0, end_index=0, current_round=0):
		# Assign trivialities
		self.begin_index = begin_index
		self.end_index = end_index
		self.current_round = current_round

		# Create the deck with right specs
		sorted_deck = []
		for suite in range(1, 5):
			for value in range(begin_index, end_index + 1):
				sorted_deck.append(Card(value, suite, False, False, False, False))

		self.deck = sorted_deck

	def shuffle():
		num_shuffles = int(math.floor((((self.end_index - self.begin_index + 1) * 4)/52) * 7))
		for i in range(num_shuffles):
			random.shuffle(array)

	def deal():
		# Deal a card and set it's dealt property to true
		self.deck[-1].dealt == True
		self.deck[-1:] + self.deck[:-1]
		return self.deck[0]

	def trumpitize(trump_suite):
		# Decide which will be trump suite and which suite Left Bower belongs to
		second_trump_suite = -1
		if trump_suite - 2 > 0:
			second_trump_suite = trump_suite - 2
		else:
			second_trump_suite = trump_suite + 2

		for card in self.deck:
			if card.suite == trump_suite:
				card.is_higher_trump == True
			elif card.suite == second_trump_suite:
				card.is_higher_trump == True

	def cleanse():
		# Reset all cards to default
		for card in self.deck:
			card.is_higher_trump == False
			card.is_high_trump == False
			card.dealt == False