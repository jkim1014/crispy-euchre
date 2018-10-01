from bot import Bot

class Team:
	def __init__(self, players=None, round_points=0, set_points=0):
		self.players = [] if players is None else players
		self.round_points = round_points
		self.set_points = set_points

	def win_round(self):
		self.round_points += 1

	def win_set(self):
		self.set_points += 1

	def reset_set(self):
		self.set_points = 0