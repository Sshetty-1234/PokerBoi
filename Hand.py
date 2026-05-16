from Cards import RANK,SUIT, card_evaluation
from Participant import Player 
from GameState import GamePhases
import random

class GAME:
    
    def __init__(self):
        self.TABLE = []
        self.pot = 0
        self.used_cards = set()
        self.USER = Player()
        self.COMP = Player()
        self.phase = GamePhases.PREFLOP
        
    def play(self,):
        
        self.deal()
        
        while self.phase != GamePhases.SHOWDOWN:
            
            print("\n")
            print(f"Current phase is {self.phase}")
            print("----------------------------------------------------------------------------------------------")
            
            if self.phase != GamePhases.PREFLOP:
                print(f"The card on the table {self.TABLE}") 
            print(f"Your Cards are  {self.USER.hand}") 
            print("Choose between the following actions")
            choice = (input("1: FOLD, 2: CHECK, 3: RAISE, 4:CALL: "))
            
            while self.action(choice) is False:
                choice = (input("1: FOLD, 2: CHECK, 3: RAISE, 4:CALL: "))
                
            if self.phase == GamePhases.PREFLOP:
                
                for _ in range(3):
                    self.TABLE.append(self.draw_random_card())
                self.phase = GamePhases.FLOP 
                
            elif self.phase == GamePhases.FLOP:
                
                self.TABLE.append(self.draw_random_card())
                self.phase = GamePhases.TURN
                
            elif self.phase == GamePhases.TURN:
                
                self.TABLE.append(self.draw_random_card())
                self.phase = GamePhases.RIVER
                
            elif self.phase == GamePhases.RIVER:
                
                print("\n")
                usr_scr = card_evaluation(self.TABLE, self.USER.hand)
                com_scr = card_evaluation(self.TABLE, self.COMP.hand)
                print(f"Your Cards are  {self.USER.hand}") 
                print(f"The opponent had {self.COMP.hand}")
                if usr_scr < com_scr:
                    print(f"You won! {self.pot}")
                    self.USER.chips += self.pot
                else:
                    print(f"You lost {self.USER.current_bet}")
                    self.COMP.chips += self.pot
                
                self._next_round()
                
    
    def action(self, val: int):
        if not val.isdigit():
            print("Invalid choice try again!")
            return False

        val = int(val)
        
        if val == 1:
            
            self._fold()
            
        elif val == 2:
            
            pass
        
        elif val == 3:
            
            amt = int(input("Raise by: "))
            self._raise(amt, self.USER)
            self._call(self.COMP)
            
            print(f"Your remaining amount is: {self.USER.chips}")
            print(f"Money in the pot is: {self.pot}")
            
        elif val == 4:
            
            amt = input("Raise by: ")
            self._call(self.COMP)
            
        else:
            
            print("Invalid choice try again!")
            return False
        
        return True
            
    # deals a random card
    def draw_random_card(self) -> str:
        
        while True:
            rank_power = random.randint(0, len(RANK)-1)
            suit_index = random.randint(0, len(SUIT)-1)

            card = (RANK[rank_power], SUIT[suit_index])

            if card not in self.used_cards:
                self.used_cards.add(card)
                return card

    def _next_round(self,):
        resume = input("Do you wish to continue? (y/N): ")
        if resume == "y":
            self.phase = GamePhases.PREFLOP
            self.TABLE = []
            self.used_cards = set()
            self.deal()
            self.pot = 0
        else:
            print(f"Your total earnings are: {self.USER.chips}")
            print(f"You bet {self.USER.current_bet}")
            print(f"Thank you")
            self.phase = GamePhases.SHOWDOWN
    
    def deal(self):
        
        # distributes 2 cards to each player
        player_hand = []
        comp_hand = []
        while len(player_hand) < 2:
            p_card = self.draw_random_card()
            player_hand.append(p_card)
            
            c_card = self.draw_random_card()
            comp_hand.append(c_card)
        
        self.USER.hand = player_hand
        self.COMP.hand = comp_hand
    
    
    '''
    Actions a player can take
    '''
    # raise
    def _raise(self, amt:int, participant:Player):
        self.pot += amt
        participant.chips -= amt
        participant.current_bet += amt
        
    # call: pot - 2 * (player_current_bet)
    def _call(self, participant:Player):
        call_amount = self.USER.current_bet - self.COMP.current_bet
        self.pot += call_amount
        participant.chips -= call_amount
        participant.current_bet += call_amount
        
    # fold
    def _fold(self,):
        self.COMP.chips += self.pot
        self._next_round()
        
        
if __name__ == "__main__":
    deck = GAME()
    deck.play()    
    
