DECK = []

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

for r in RANK:
    for s in SUIT:
        DECK.append((r,s))

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

def convert_card_notation(chosen_cards):
    res = []
    for card in chosen_cards:
        res.append((rank_map[card[0]] + suit_map[card[1]]))
    
    return res


