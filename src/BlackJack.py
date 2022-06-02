#   Computer dealer and a human player
#   Player starts with 2 cards face up, dealer starts with 1 card face up and 1 card face down
#   Player Goal: get closer to a total value of 21 than the dealer does.
#   Hit: grab another card from a deck and put on hand
#   Stay: stop receiving card
#   If the player goes over 21, he bust; he loses the bet; then dealer collects the money
#   jack, queen, king count as value of 10
#   Aces can be either 1 or 11

import random

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.suit} {self.rank}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                temp_card = Card(suit, rank)
                self.deck.append(temp_card)

    def __str__(self):
        for a in self.deck:
            print(a)
        return 'end of deck'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        #   grab a card from deck
        grabbed_card = self.deck.pop()
        return grabbed_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        #   add a card to hand
        self.cards.append(card)
        #   keep tracking the total value of cards on hand
        self.value += values[card.rank]

        if card.rank == 'Ace':
            #   keep tracking the number of aces
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            #   if the total value is > 21 and i still have an ace
            #   then change my ace to be a 1 instead of 11
            self.value -= 10
            self.aces -= 1
            #   if ace become 1 from 11, subtracting 10 from the total value is done


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        #   a function used in the situation of winning the bet
        self.total += self.bet

    def lost_bet(self):
        #   a function used in the situation of losing the bet
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please provide the amount of chips to bet on  "))
        except:
            print('You did not enter the valid input, please provide a valid amount of chips to bet on')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips, you currently have {}'.format(chips.total))
            else:
                print('You have successfully bet some chips')
                break


def hit(deck, hand):
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    while True:
        choice = input('Hit or stand? Enter h or s ')
        if choice[0].lower() == 'h':
            hit(deck, hand)
        elif choice[0].lower() == 's':
            print('Player stands. Dealers turn')
            playing = False
        else:
            print('Sorry, I did not understand that. Please enter h or s  ')
            continue
        break


def show_some(player, dealer):
    #   showing one from dealer, all from the player
    print("\n Dealer's Hand: ")
    print('First card: hidden ')
    print(dealer.cards[1])
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    #   showing all the cards from dealer and player
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("Bust Player! ")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player Wins! Dealer Busted!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lost_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH!')


if __name__ == '__main__':
    while playing:
        # Print an opening statement
        print("Welcome to BlackJack!")
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        # Set up the Player's chips
        player_chips = Chips()
        # Prompt the Player for their bet
        take_bet(player_chips)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        while playing:
            # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player_hand.value <= 21:
                while dealer_hand.value < player_hand.value:
                    hit(deck, dealer_hand)
                # Show all cards
                show_all(player_hand, dealer_hand)
                # Run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)
                else:
                    push(player_hand, dealer_hand)
            # Inform Player of their chips total
            print('\n Player total chips are at: {}'.format(player_chips.total))
            # Ask to play again
            new_game = input('Would you like to play another game? y/n')
            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print("Thank you for playing")
                break
