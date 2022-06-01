#	card, suit, rank, value, deck, player
import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        #	if the object is called to be printed or functions as a string, prints the returning value
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        #	empty list without any user input
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #	create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        #	shuffles the deck of all_cards
        random.shuffle(self.all_cards)

    def deal_one(self):
        #	popping and returning the present card
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
        #	extends() method merges the lists
        self.name = name
        #   list of cards that is confined to this specific class
        self.all_cards = []

    def remove_one(self):
        #   assure the card is being popped from bottom
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        #   if the type of new_cards is list, we will have multiple cards to be appended, which is basically merging two lists
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            #   if there is only a single card to be appended, it is not a list;therefore, append.
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


if __name__ == '__main__':
    #   create two instances of each player.
    #   create an instance of a deck and then shuffle
    #   split between p1 and p2 half half
    #   check the winner; check for 0 card if a player has a list of card that its length is equal to 0
    #   have a big while game_on loop
    #   each player draws a card then compares. Add the card to the bottom of winner's deck
    #   when the cards are equal, put the while loop until there is no more war(state of same cards being drawn)
    #   after adding all the cards to winner, check the ultimate wiiner

    #   Game Setup
    player_one = Player('One')
    player_two = Player('Two')

    new_deck = Deck()
    new_deck.shuffle()

    for card in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True
    round_num = 0
    #   while game_on
    while game_on:
        round_num += 1
        print(f'Round {round_num}')

        if len(player_one.all_cards) == 0:
            print('Player one, out of cards! Player two wins')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print('Player two, out of cards! Player one wins')
            game_on = False
            break

        #   Start a new round
        player_one_cards = []
        #p1 grabs a card
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        #p2 grabs a card
        player_two_cards.append(player_two.remove_one())

        #   while at_war
        #   at_war is false when the first drawn match up situation is resolved. Before the resolution, cards will be continuously stacked up
        #   each player must draw 5 cards when war occurred
        #   if a player does not have 5 cards to draw at war situation, he loses
        #   while at_war == True
        #   if one > two, add cards to one, at_war = False
        #   elif one < two, add cards to two, at_war = False
        #   else check if players have enough cards, draw additional cards

        at_war = True
        while at_war:
            #   get the card at the top, which is the last card
            if player_one_cards[-1].value > player_two_cards[-1].value:
                #   getting the drawn cards back
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                #   getting the drawn cards back
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print('WAR!')

                if len(player_one.all_cards) < 5:
                    print("Player one is unable to play the war! ")
                    print("Player two wins")
                    game_on = False
                    at_war = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player two is unable to play the war! ")
                    print("Player one wins")
                    game_on = False
                    at_war = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

