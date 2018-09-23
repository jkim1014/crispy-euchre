# Build a custom hand, cards taken from Deck in deck.py
class Hand:
	def __init__(self, cards=None, num_cards=0, round_id=0):
		self.cards = [] if cards is None else cards
		self.num_cards = num_cards
		self.round_id = round_id

	def get_card(card):
		self.cards.append(card)