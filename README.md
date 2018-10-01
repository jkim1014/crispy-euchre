# Crispy Euchre

## Inspiration
Euchre was a game I loved to play with my friends on bus rides to math competitions or on nights that we wanted to challenge each other. I thought that this was a great chance to add variations to the game and share with others what I enjoy. With that being said, enjoy! =D
## How to Run
After downloading all the files, go into the directory of where the files are saved. Run ```python game.py ```. MAKE SURE THAT YOU ARE RUNNING THIS ON PYTHON 2.7!!!
## Instructions
This game is a 4 player game. I have created 3 bots for you to play with! Here are the standard rules for the game, without my variation on it. I will explain the variation afterwards. Citing 'https://cardgames.io/euchre/' for their readable standard instructions!
### Overview
Euchre is a trick taking game with a trump, played by four players in teams of two. The basic play is similar to Whist, i.e. each player plays one card, the highest card of the suit led wins the trick, unless someone has played a card of the trump suit. An important difference from Whist is that one of the teams names the trump and must then win the majority of the tricks in that hand. The game is played over several rounds until one team has gotten 10 points.
### Dealing
Euchre uses a non standard deck of 24 cards. It's made up of the 9, 10, Jack, Queen, King and Ace of each suit. Some variations also use the Joker, but this version does not. The initial dealer is chosen randomly, in the next round the player to the dealer's left is the new dealer and so on. Five cards are dealt to each player in two rounds of dealing. Once all players have their cards, the top card of the deck is turned face up, so it's ready for the next part of the game, which is...
### Naming Trump
After the cards are dealt they players must pick what will be the trump suit. At this point there is one face up card on the table, the suit of that card is the potential trump suit. Going clockwise around the table, starting with the player to the dealer's left, each player can either say "Pass", meaning they don't want the suit to become trump, or they can say "Order it up" in which case the suit of the card becomes trump and the calling round ends immediately. The face up card on the table goes to the dealer which takes it and discards one of the cards from his hand and then the game is ready to begin. The team that picked the trump are known as the "Makers" and the other team are known as the "Defenders".

If all players pass on the trump card then there's another round of naming trumps, where a player may simply name which suit he wants to be trump (although he may not name the suit everyone just passed on), or say pass. If all players pass on this round as well then the deal is ruined and a new hand is dealt.
### Ranking of Trump Cards
The trump ranking in Euchre is quite different from most other trump taking games. The trump suit ranks higher than the other suits, but within the trump suit the Jack (known as the Right Bower) is the highest card. Then, in a weird twist, the Jack in the other suit that's the same color as the trump is the next best trump card. E.g. if spades are trump then the Jack of clubs would be the next best card, known as the Left Bower). After that the rest of the trump cards follow in order from high to low, Ace, King, Queen, 10, 9. The Left Bower is considered for all purposes as a member of the trump suit. Just to make it clearer, if trump suit was Hearts, the ranking of trump cards would be:
1. Jack of Hearts (Right Bower)
2. Jack of Diamonds (Left Bower)
3. Ace of Hearts
4. King of Hearts
5. Queen of Hearts
6. 10 of Hearts
7. 9 of Hearts

### Playing
Play is like in most trick taking games. A player leads with a suit, other players must follow suit if they have it, but are otherwise free to play any card if they have nothing in the lead suit. Cards are ranked from high to low, trump beats lead suit, lead suit beats other suits. The person who takes a trick leads in the next trick.
### Scoring
A team that wins 3 or more tricks wins the hand and gets points, the losing team gets no points.
### Winning
A team wins once it has gotten 10 points.
### Variation
The variation that I introduce to the game is that my game allows for more card variety. Standard Euchre, as described above, is a 24 cards game. However, I think that we can have more variety on the winning condition of the game. We don't need to limit the game from allowing only values from 9 to Ace for each suite. We can have it be anywhere from 2 to just the top four values of each suite. This allows for a large range of cards to receive when being dealt cards which translates to less predictive winning conditions for each team.

## Design Choices

### Classes
1. Card
Card object is the basis of this game. Every game starts and ends based on the information given by the card. Here are some things we need to keep track of for the card and things I've implemented in its constructor:
	* Value
	* Suite
	* Has it been dealt?
Specifying the state if being dealt (boolean) simplifies the dealing process. We can easily ensure that a card never gets dealed to a player if it has been before. Perhaps the most important detail of the game that needs to be tracked is what the trump suite is. Each card in my implementation has a boolean value for whether or not it belongs in the trump suite or not. As we will see, this simplifies the process of both the player and the bot pick cards to play. For players, we can easily recognize if the user has picked an invalid card to play. For bots, we can easily recognize which cards are playable in its current round.
2. Deck
Deck object contains metadata about the game as well as the cards for the game. This centralizes the information needed for player and bots later when playing the game! Our deck keeps track of the lowest value specified by the user for the game and the highest value of a card, defaulted to the Ace of any suite. It also keeps track of the current trump suite. This way, when preparing for the next set in the game, we can easily refresh the trump suite and all the cards' trump suite value.
3. Player
The hardest part about the player is defining the legal boundaries of moves. In the player class's ```play_one_card``` function, we define exactly which suites of cards are playable for the set and which inputs are legal. 
4. Bot
The bot class defines how the bot will play in the game. Afterall, we need four players for the game! Some of the problems that I implemeneted a solution to are as follows:
	* When should the bot swap?
	* What card should it swap?
	* What are the valid cards to play for a turn?
	* If not swapping what suite should it call trump?
While the bot is not the smartest bot that you may have seen (haha), I can guarantee you that it will only do legal moves and be somewhat smart about what cards it will play.
5. Team
This class keeps data about the scores of the game and surrounds the two players of a team. Each round has sets to keep track of for each team, so it centralizes all the small scoring details.

### Important Functions
1. Deal
We need to deal randomly between 2 or 3 and then the rest after! We also need to accurately give it to each player in the game.
2. Print Hand
As a user, it would be really hard to play the game without knowing what cards are in your hand. Print print print!
3. Swamp Trump
This functions utilizes the swap functions for bots and gives the human player the option to switch one of their card for the card at the top of the deck. You have all the options in your own hands!
4. Pick Trump
If swapping round does not go through, the game is designed so that each player can call a suite to make trump suite (providing more information!).
5. Win Analysis
Who wins based on the cards played in the set? This is non-trivial and we need to calculate what trump cards were played and if not, what other cards were played.
6. Play One Card
This function, for both bots and player, handle legal moves possible for all rounds.

### Data Structures
1. Counter
Counter is really really useful when helping the bot choose what card to play. This adds some smartness to the bots, giving them a chance to beat the human player >:)
2. Arrays
Arrays are very important when keeping track of all the cards being played in the game as well as other major components of the game: the deck, the player's hand, the cards played in a set, the team membersm, etc.

## Why in Python?
I think given that Euchre is already a complicated game, for anyone who is wanting to read the code behind it or wanting to dissect each component of the game, it is important to maintain a readable code base. While we can add as many comments as we want for code written in Java, Python helps to keep every loop, if statements, and movement of data readable. It is also very easy to echo the inputs and print to the terminal, which is the main console for the game!
