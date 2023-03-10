import random
from mymodules.cards import Cards
from mymodules.cards import Deck
from mymodules.player import Chips
from mymodules.cards import Table

def ask_bet(chips):
    while True:
        try:
            chips.betting=int(input("How much would you like to bet: "))
        except:
            print("Dont be an idiot")
            continue
        else:
            if chips.betting > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(player,deck):
    player.add_card(deck.deal())
    player.adjust_for_ace()

def hit_or_stand(player,deck,dealer):
    global playing
    while True:
        try:
            x=input("Hit or Stand: ")
            if x.startswith('h'):
                hit(player=player,deck=deck)
            elif x.startswith('s'):
                print('\n Dealer playing')
                playing=False
                hit(player=dealer,deck=deck)
    
        except:
            print("sorry try again")
            continue
        else:
            break
        

def ask_bet(chips):
    while True:
        try:
            chips.betting=int(input("Enter how much to bet: "))
        
        except:
            print("Enter a valid integer")
            continue
        else:
            break
    
playing=True

while True:
    new_deck=Deck()
    new_deck.shuffle()
    player=Table()
    dealer=Table()
    chips=Chips()
    ask_bet(chips=chips)
    print(f"Player bets {chips.betting}")
    player.value=0
    dealer.value=0
    hit(player=player,deck=new_deck)
    hit(player=player,deck=new_deck)
    hit(player=dealer,deck=new_deck)
    hit(player=dealer,deck=new_deck)
    dealer.show_dealer_half()
    player.show_player()
    
    while playing:
        hit_or_stand(player=player,dealer=dealer,deck=new_deck)
        dealer.show_dealer_half()
        player.show_player()
        if player.value>21:
            print("\n    Player Busts")
            chips.lose_bet()
            break
            
    if player.value<=21:
        while dealer.value<17:
            dealer.add_card(new_deck.deal())
        
        dealer.show_dealer_half()
        player.show_player()
        
        if dealer.value>21:
            dealer.show_dealer_full
            player.show_player
            print(" \n    Dealer Busts")
            chips.win_bet()
        
        elif player.value>dealer.value:
            print("\n    Player wins")
            chips.win_bet()
        
        elif player.value<dealer.value:
            print("\n    Dealer wins")
            chips.lose_bet()
        
        else:
            print("\nDealer and Player Tie")
            
    print(f"\nPlayer chips currently {chips.total}")
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    
    else:
        print("Thanks for playing!")
        break