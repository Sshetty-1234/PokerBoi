from phevaluator import evaluate_cards
import random
from Cards import DECK, convert_card_notation


def simulate(hand, table, num_players):

    stack = list(set(DECK) - set(hand + table))
    random.shuffle(stack)

    # Give opponents cards
    player_hands = []
    for _ in range(num_players):

        if len(stack) < 2:
            print("No More Cards!")
            break

        player_hands.append([
            stack.pop(),
            stack.pop()
        ])

    # Complete board
    while len(table) < 5:
        table.append(stack.pop())

    
    # Evaluate your hand
    hand_pwr = evaluate_cards(*convert_card_notation(hand + table))
    
    for opp_hand in player_hands:
        opp_eval = evaluate_cards(*convert_card_notation(opp_hand + table))

        # LOWER score = better hand
        if hand_pwr < opp_eval:
            continue        

        elif hand_pwr == opp_eval:
            return 2        

        else:
            return 1        

    return 0                
    
    

hand = [('EIGHT', 'SPADES'), ('TWO', 'HEARTS')]
table = [('KING', 'HEARTS'), ('TEN', 'DIAMONDS'), ('QUEEN', 'HEARTS')]

simulate(hand,table,2)




