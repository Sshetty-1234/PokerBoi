from treys import Card, Evaluator

evaluator = Evaluator()

RANK = [
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
    "TEN",
    "JACK",
    "QUEEN",
    "KING",
    "ACE"
]

SUIT = [
    "CLUBS",
    "SPADES",
    "HEARTS",
    "DIAMONDS"
]

rank_map = {
    "ACE": "A",
    "KING": "K",
    "QUEEN": "Q",
    "JACK": "J",
    "TEN": "T",
    "NINE": "9",
    "EIGHT": "8",
    "SEVEN": "7",
    "SIX": "6",
    "FIVE": "5",
    "FOUR": "4",
    "THREE": "3",
    "TWO": "2"
}

suit_map = {
    "HEARTS": "h",
    "DIAMONDS": "d",
    "CLUBS": "c",
    "SPADES": "s"
}

def card_evaluation(board, player):
    board = [ Card.new(rank_map[r] + suit_map[s]) for r, s in board ]
    player = [ Card.new(rank_map[r] + suit_map[s]) for r, s in player ]
    
    return (evaluator.evaluate(board, player))


