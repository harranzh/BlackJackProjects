import random

# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11}
playing = True
game_on = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        # Creating a deck 
        for suit in suits:
            for rank in ranks:
                # create card object
                # add card to all deck
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has ' + deck_comp

    def shuffle(self):
        # Shuffling the deck
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
        
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 # Keep track of number of aces 

    def add_card(self, card_dealt):
        self.cards.append(card_dealt)
        self.value += values[card_dealt.rank]

        # Track aces
        if card_dealt.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        # If total value is greater than 21 and I have one ace, change value of ace to 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
class Chips:

    def __init__(self):
        self.total = 0
        self.bet = 0

    def cash_in(self):
        # Takes from user total value of chips 
        self.total = int(input('Enter your initial bidding amount: '))

    def win_bet(self):
        # Add winnings into total
        self.total += self.bet

    def lose_bet(self):
        # Substract losses from total
        self.total -= self.bet

    def continue_bidding(self):
        self.total += self.total

    def cash_out(self):
        return self.total

def take_bet(chips):

    while True:
         
        try:
            chips.bet = int(input('Enter how many chips you would like to bet: '))

        except ValueError:
            print('Enter an integer value for the number of chips.')

        else:
            if chips.bet > chips.total:
                print('Sorry, your bet is greater than your total number of chips.')
                print(f'You have: {chips.total} available chips.')
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player Stands! Dealer Turn')
            playing = False 
        
        else:
            print('Sorry, I did not understand that. Enter h or s only.')
            continue 
        break

def show_some(player, dealer):

    print("\nDealer's Hand: ")
    print("<card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

def show_all(player, dealer):

    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand = ",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand = ",player.value)

def player_busts(player, dealer, chips):

    print('Player BUSTS!')
    chips.lose_bet()

def player_wins(player, dealer, chips):

    print('Player WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):

    print('Player WINS! Dealer BUSTS')
    chips.win_bet()

def dealer_wins(player, dealer, chips):

    print('Dealer WINS! Player BUSTS')
    chips.lose_bet()

def push(player, dealer):
    
    print('Dealer and Player Tie! PUSH!')

# GAME LOGIC
while game_on:

    print('WELCOME TO BLACKJACK!')
    
    # Create and Shuffle Deck
    deck = Deck()
    deck.shuffle()

    # Setup Players 
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Setup Dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Setup Players Chips
    player_chips = Chips()
    player_chips.cash_in()
    
    # Ask Player's for their bet
    take_bet(player_chips)
    

    while playing:

        # player_chips.continue_bidding()

        # Show cards to player
        show_some(player_hand, dealer_hand)

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break 
    
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        
        else:
            push(player_hand, dealer_hand)

    print('\n Players total chips are at: {}'.format(player_chips.total))

    continue_game = input('Would you like to continue to play? Y/N ')

    if continue_game[0].lower() == 'y':
        playing = True
        continue

    elif continue_game[0].lower() == 'n':
        # playing = False
        print('Your total chips are {}.'.format(player_chips.cash_out()))
        print('Thank you for playing!')
        break