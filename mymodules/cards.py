
import random
from IPython.display import clear_output
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
class Cards:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    



class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    def deal(self):
        single_card=self.deck.pop()
        return single_card
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def __str__(self):
        for cards in self.deck:
            return f"{cards.suit} of {cards.rank}"
        
class Table:
    def __init__(self):
        self.cards = []   
        self.value = 0   
        self.aces = 0    
    
    def show_player(self):

        print("\nPlayer's Cards: \n")
        for c in range(0,len(self.cards)):
            print(self.cards[c])  
    
    def show_dealer_half(self):
        print("\nDealer's Cards: \n")
        print("<card hidden>")
        for b in range(1,len(self.cards)):
            print(self.cards[b])
        print('\n')
    
    def show_dealer_full(self):
        print("\nDealer's Cards: \n")
        for b in range(0,len(self.cards)):
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