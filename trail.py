from treys import Card, Evaluator
from Cards import rank_map, suit_map, RANK, SUIT
import random


def random_card() -> str:
    rank_power = random.randint(0,len(RANK)-1)
    suit_index = random.randint(0,len(SUIT)-1)
    card = (str(RANK[rank_power]), str(SUIT[suit_index]))
    return card

print(random_card())


# evaluator = Evaluator()
# board = [
#     ("JACK", "CLUBS"),
#     ("ACE", "CLUBS"),
#     ("TWO", "CLUBS")
# ]
# player = [
#     ("FOUR", "HEARTS"),
#     ("ACE", "HEARTS")
# ]

# def card_evaluation(board, player):
#     board = [ Card.new(rank_map[r] + suit_map[s]) for r, s in board ]
#     player = [ Card.new(rank_map[r] + suit_map[s]) for r, s in player ]
    
#     print(evaluator.evaluate(board, player))

# card_evaluation(board, player)