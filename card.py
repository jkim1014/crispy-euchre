class Card:
	def __init__(self, value=-1, suite=-1, is_higher_trump=False, is_high_trump=False, dealt=False):
		self.value = value
		self.suite = suite
		self.is_higher_trump = is_higher_trump
		self.is_high_trump = is_high_trump
		self.dealt = dealt