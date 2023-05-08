import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

#Define a class card with attributes suit and rank and printing returns "rank of suit"
class Cards:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    


#Create a deck of 52 cards
class Deck:
    
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))
    #function to deal a card and remove one card from deck 
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def __str__(self):
        for cards in self.deck:
            return f"{cards.suit} of {cards.rank}"


#A table class used to keep the cards on a table
class Table:
    #the value of cards and number of aces defined in the attributes
    def __init__(self):
        self.cards = []   
        self.value = 0   
        self.aces = 0    
    
    def show_player(self):

        print("\nPlayer's Cards: \n")
        for playercards in range(len(self.cards)):
            print(self.cards[playercards])  
    
    def show_dealer_half(self):
        print("\nDealer's Cards: \n")
        print("<card hidden>")
        for dealercards in range(len(self.cards)):
            print(self.cards[dealercards])
        print('\n')
    
    def show_dealer_full(self):
        print("\nDealer's Cards: \n")
        for b in range(len(self.cards)):
            print(self.cards[b])
        print('\n')
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

#To keep count of the bets
class Chips:
    def __init__(self,total=100):
        self.betting=0
        self.total=total

    def win_bet(self):
        self.total += self.betting
    
    def lose_bet(self):
        self.total -= self.betting


def ask_bet(chips):
    while True:
        try:
            chips.betting = int(input("How much would you like to bet: "))
        except:
            print("Dont be an idiot")
            continue
        else:
            if chips.betting > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(player, deck):
    player.add_card(deck.deal())
    player.adjust_for_ace()


def hit_or_stand(player, deck, dealer):
    global playing
    while True:
        try:
            x = input("Hit or Stand: ")
            if x.startswith('h'):
                hit(player=player, deck=deck)
            elif x.startswith('s'):
                print('\n Dealer playing')
                playing = False
                hit(player=dealer, deck=deck)

        except:
            print("sorry try again")
            continue
        else:
            break


def ask_bet(chips):
    while True:
        try:
            chips.betting = int(input("Enter how much to bet: "))

        except:
            print("Enter a valid integer")
            continue
        else:
            break


playing = True

while True:
    new_deck = Deck()
    new_deck.shuffle()
    player = Table()
    dealer = Table()
    chips = Chips()
    ask_bet(chips=chips)
    print(f"Player bets {chips.betting}")
    player.value = 0
    dealer.value = 0
    hit(player=player, deck=new_deck)
    hit(player=player, deck=new_deck)
    hit(player=dealer, deck=new_deck)
    hit(player=dealer, deck=new_deck)
    dealer.show_dealer_half()
    player.show_player()

    while playing:
        hit_or_stand(player=player, dealer=dealer, deck=new_deck)
        dealer.show_dealer_half()
        player.show_player()
        if player.value > 21:
            print("\n    Player Busts")
            chips.lose_bet()
            break

    if player.value <= 21:
        while dealer.value < 17:
            dealer.add_card(new_deck.deal())
            dealer.show_dealer_half()
            player.show_player()

        if dealer.value > 21:
            dealer.show_dealer_full
            player.show_player
            print(" \n    Dealer Busts")
            chips.win_bet()

        elif player.value > dealer.value:
            print("\n    Player wins")
            chips.win_bet()

        elif player.value < dealer.value:
            print("\n    Dealer wins")
            chips.lose_bet()

        else:
            print("\nDealer and Player Tie")

    print(f"\nPlayer chips currently {chips.total}")
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print("Thanks for playing!")
        break
