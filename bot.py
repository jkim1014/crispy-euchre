class Bot:
	def __init__(self, hand=None, current_deck=None):
		self.current_deck = [] if cards is None else current_deck
		self.hand = [] if cards is None else hand

	def get_my_hand(hand):
		self.hands = hand
		
	def play_one_card():
		# TODO

	def add(card):
		self.hand.append(card)

	def use(card):
		self.hand.remove(card)

	def swap(my_card, foreign_card):
		self.hand.append(foreign_card)
		self.hand.remove(my_card)