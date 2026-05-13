from Cards import RANK,SUIT, card_evaluation
from Participant import Player 
import random

class GAME:
    
    def __init__(self):
        self.TABLE = []
        self.pot = 0
        self.USER = Player()
        self.COMP = Player()
        self.deal()
        
    
    # deals a random card
    def random_card(self) -> str:
        rank_power = random.randint(0,len(RANK)-1)
        suit_index = random.randint(0,len(SUIT)-1)
        card = (str(RANK[rank_power]), str(SUIT[suit_index]))
        return card
    
    def deal(self):
        # distributing the deck
        while len(self.TABLE) < 3:
            card = self.random_card()
            self.TABLE.append(card)
        
        # distributes 2 cards to each player
        player_hand = []
        comp_hand = []
        while len(player_hand) < 2:
            p_card = self.random_card()
            player_hand.append(p_card)
            c_card = self.random_card()
            comp_hand.append(c_card)
        
        self.USER.hand = player_hand
        self.COMP.hand = comp_hand
    
    # raise
    def _raise(self, amt:int, participant:Player):
        self.pot += amt
        participant.chips -= amt
        participant.current_bet += amt
        
    # call: pot - 2 * (player_current_bet)
    def _call(self, participant:Player):
        call_amount = self.pot - (2*participant.current_bet)
        self.pot += call_amount
        participant.chips -= call_amount
        participant.current_bet += call_amoun
    
        
        
        
if __name__ == "__main__":
    deck = GAME()
    print(deck.TABLE)
    print(f"your cards are {deck.USER.hand}")
        
    


'''
Dealer func

Func - deals 5 cards and gives 2 cards to each player


raise
check
bet
fold



'''


