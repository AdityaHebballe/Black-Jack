class Chips:
    def __init__(self,total=100):
        self.betting=0
        self.total=total

    def win_bet(self):
        self.total += self.betting
    
    def lose_bet(self):
        self.total -= self.betting


