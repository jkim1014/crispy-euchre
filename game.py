from deck import Deck
from bot import Bot
from player import Player
from team import Team
import random

# Define playing card values for visibility in terminal
suite_guide = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
value_guide = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def deal(random_deals, game_deck, my_position, players_arr):
	# First round of dealing. Randomly choose from 2 or 3 cards to deal per person
	for i in range(4):
		hand = []
		random_index = random.randrange(len(random_deals))
		for j in range(random_deals[random_index]):
			card_dealt = game_deck.deal()
			hand.append(card_dealt)
			players_arr[i].get_my_hand(hand)

	# Second round of dealing. Deal the remaining number of cards such that each person has exactly 5 in their hand
	for player in players_arr:
		for x in range(5 - len(player.hand)):
			card_dealt = game_deck.deal()
			player.add(card_dealt)

def print_hand(player):
	hand = player.hand
	for i in range(len(hand)):
		print str(i+1) + ') ' + value_guide[hand[i].value - 1] + ' of ' + suite_guide[hand[i].suite - 1]

def swap_trump(my_position, me, players_arr, game_deck, trumped, top_card):
	# Ask each player in order
	for j in range(1, 5):
		# Give the terminal user the option to swap with one of their cards
		if j == my_position:
			trade = str(raw_input("Trade one of your cards for this card? [y/n]\n"))
			if trade == 'y':
				which = str(raw_input("Which card number would you like to switch with? [press 'n' to not trade]\n"))
				if which == 'n':
					continue
				# First announce the swapped card and the trump suite. Then 'trumpitize' the entire deck and swap the cards. Print the new hand
				else:
					print 'Swapped ' + value_guide[me.hand[int(which)-1].value - 1] + ' of ' + suite_guide[me.hand[int(which)-1].suite - 1] + ' for ' + value_guide[top_card.value - 1] + ' of ' + suite_guide[top_card.suite - 1]
					print 'Trump suite set to ' + suite_guide[top_card.suite-1] + ' by me after swapping!'
					game_deck.trumpitize(top_card.suite)
					trumped += 1
					me.swap(me.hand[int(which)-1], top_card)
					print 'New hand after swap:'
					print_hand(me)
					break
		# If bot does not think that it should not swap, do not swap
		else:
			if not players_arr[j-1].should_swap(top_card.suite):
				continue
			# Set trump suite to the top card if appropriate
			else:
				print 'Trump suite set to ' + suite_guide[top_card.suite-1] + ' by player ' + str(j) + ' after a swap!'
				game_deck.trumpitize(top_card.suite)
				trumped += 1
				card_to_swap = players_arr[j-1].to_swap(top_card.suite)
				players_arr[j-1].swap(card_to_swap, top_card)
				break
	return trumped

def pick_trump(my_position, me, players_arr, game_deck, trumped):
	# Again, go through each player to see if anyone would want a suite to be trump suite, based on their current cards
	for k in range(1, 5):
		# Give terminal user the option to pick the trump suite
		if k == my_position:
			res = str(raw_input("Would you like to make one of your cards' suite the trump suite? [y/n]\n"))
			if res == 'y':
				content = str(raw_input("Which suite would you like to switch with? [press 'n' to cancel]\n"))
				if content == 'n':
					continue
				else:
					if content not in suite_guide:
						# Error handling for invalid suite
						while content not in suite_guide:
							fixed = str(raw_input("Invalid suite, please type again!\n"))
							content = fixed
					print 'Made ' + content + ' as trump suite.'
					game_deck.trumpitize(suite_guide.index(content) + 1)
					trumped += 1
					break
		else:
			# Given a true/false as to make a suite trump, either make a suite trump or do nothing
			yes_no, suite = players_arr[k-1].call_trump()
			if not yes_no:
				print 'Player ' + str(k) + ' passed.'
				continue
			else:
				trumped += 1
				print suite_guide[suite - 1] + ' has been made trump suite by player ' + str(k)
				game_deck.trumpitize(suite)
				break
	# If no one wanted to make a suite trump, then 'misdeal'. Terminate game and restart
	if trumped != 1:
		print 'Cannot deal. Case of misdeal. Start new game.'
		return None

def win_analysis(cards_arr, game_deck, players_arr, team_one, team_two):
	win_card = None
	first_card_suite = cards_arr[0][0].suite
	trump = game_deck.current_trump
	trumps = []
	for card in cards_arr:
		if card[0].is_higher_trump or (card[0].is_high_trump and card[0].value == 10):
			trumps.append(card)
	if len(trumps) > 0:
		win_card = trumps[0]
		for card in trumps:
			if card[0].value > win_card[0].value:
				win_card = card

	else:
		win_card = cards_arr[0]
		for card in cards_arr:
			if card[0].value > win_card[0].value:
				win_card = card

	player_num = win_card[1]
	if players_arr[player_num - 1] in team_one.players:
		team_one.win_set()
		print 'Your team won the set'
	else:
		team_two.win_set()
		print 'Opponent team won the set'
	print 'Current score:\n Your team: ' + str(team_one.set_points) + '\n Opponent team: ' + str(team_two.set_points)

def main():
	# Randomly decide position
	positions = [1, 2, 3, 4]
	random_deals = [2, 3]
	my_position = random.choice(positions)
	print 'myposition: ' + str(my_position)
	odd_or_even = (my_position - 1) % 2

	# Take input from user
	print "Welcome to Crispy Euchre!"
	lowest_value = int(raw_input("What should be the lowest value of cards for this game?\n"))

	# Make deck
	game_deck = Deck(lowest_value - 1, 13, 0, 0)
	for i in range(7):
		random.shuffle(game_deck.deck)

	# Make game players
	players_arr = []
	bot_1 = Bot(None, game_deck)
	players_arr.append(bot_1)
	bot_2 = Bot(None, game_deck)
	players_arr.append(bot_2)
	bot_3 = Bot(None, game_deck)
	players_arr.append(bot_3)
	me = Player(None, game_deck)
	players_arr.insert(my_position-1, me)

	# Make two teams
	team_one = []
	team_two = []
	player_number = 0
	for i in range(len(players_arr)):
		if i % 2 == odd_or_even:
			team_one.append(players_arr[i])
			if i + 1 != my_position:
				player_number = i + 1
		else:
			team_two.append(players_arr[i])
	my_team = Team(team_one, 0, 0)
	other_team = Team(team_two, 0, 0)

	# Announce who your teammate is!
	print "You are teammates with player " + str(player_number) 

	# Enter game! Finish only if the score for winning has been reached by a team
	while my_team.round_points != 5 or other_team.round_points != 5:

		# Get dealt cards
		deal(random_deals, game_deck, my_position, players_arr)

		# Play while we haven't exhausted 5 sets
		while game_deck.current_set != 5:
			# Show current hand
			print 'Your current hand:'
			print_hand(me)
			print 'Card at the top of the deck:'

			# Reveal top card
			trumped = 0
			top_card = game_deck.deal()
			print value_guide[top_card.value - 1] + ' of ' + suite_guide[top_card.suite - 1]

			# Ask each player if they would like to switch a card and make the new card's suite the trump suite
			trumped = swap_trump(my_position, me, players_arr, game_deck, trumped, top_card)

			if trumped != 1:
				# Or go around asking if someone would like to make a suite a trump suite
				pick_trump(my_position, me, players_arr, game_deck, trumped)

			# Play game
			set_game_cards = []
			for i in range(1, 5):
				card_played = players_arr[i-1].play_one_card(set_game_cards)
				if i == my_position:
					print 'You played the ' + value_guide[card_played.value - 1] + ' of ' + suite_guide[card_played.suite - 1]
				else:
					print 'Player ' + str(i) + ' played the ' + value_guide[card_played.value - 1] + ' of ' + suite_guide[card_played.suite - 1]
				set_game_cards.append((card_played, i))
			win_analysis(set_game_cards, game_deck, players_arr, my_team, other_team)

			print 'Finished set'
			game_deck.finish_set()

		# Handle round score
		if my_team.set_points > other_team.set_points:
			my_team.win_round()
		else:
			other_team.win_round()

		# Prepare for a new round
		game_deck.cleanse()
		my_team.reset_set()
		other_team.reset_set()

	print "Finished game"
	if my_team.round_points > other_team.round_points:
		print "Your team won!"
	else:
		print "You team did not win... Play again!"
	
if __name__ == "__main__":
	main()