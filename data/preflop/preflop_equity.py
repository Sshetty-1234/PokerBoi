

from phevaluator import evaluate_cards
import random


hands = [
    # Pairs
    "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",

    # Suited
    "AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s",
    "KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s","K4s","K3s","K2s",
    "QJs","QTs","Q9s","Q8s","Q7s","Q6s","Q5s","Q4s","Q3s","Q2s",
    "JTs","J9s","J8s","J7s","J6s","J5s","J4s","J3s","J2s",
    "T9s","T8s","T7s","T6s","T5s","T4s","T3s","T2s",
    "98s","97s","96s","95s","94s","93s","92s",
    "87s","86s","85s","84s","83s","82s",
    "76s","75s","74s","73s","72s",
    "65s","64s","63s","62s",
    "54s","53s","52s",
    "43s","42s",
    "32s",

    # Offsuit
    "AKo","AQo","AJo","ATo","A9o","A8o","A7o","A6o","A5o","A4o","A3o","A2o",
    "KQo","KJo","KTo","K9o","K8o","K7o","K6o","K5o","K4o","K3o","K2o",
    "QJo","QTo","Q9o","Q8o","Q7o","Q6o","Q5o","Q4o","Q3o","Q2o",
    "JTo","J9o","J8o","J7o","J6o","J5o","J4o","J3o","J2o",
    "T9o","T8o","T7o","T6o","T5o","T4o","T3o","T2o",
    "98o","97o","96o","95o","94o","93o","92o",
    "87o","86o","85o","84o","83o","82o",
    "76o","75o","74o","73o","72o",
    "65o","64o","63o","62o",
    "54o","53o","52o",
    "43o","42o",
    "32o"
]

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suits = ["h", "d", "c", "s"]

deck = [rank + suit for suit in suits for rank in ranks]



def hand_to_cards(hand):
    if len(hand) == 2:  # pair
        return [hand[0] + "s", hand[1] + "h"]

    r1, r2, typ = hand[0], hand[1], hand[2]

    
    if typ == "s":
        return [r1 + "s", r2 + "s"] 
    
    return [r1 + "s", r2 + "h"]

def simulate(hand, table, num_players):

    opps = num_players - 1
    stack = list(set(deck) - set(hand + table))
    random.shuffle(stack)
    

    # Give opponents cards
    player_hands = []
    for _ in range(opps):

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
    hand_pwr = evaluate_cards(*(hand + table))
    tied = False
    for opp_hand in player_hands:
        opp_eval = evaluate_cards(*(opp_hand + table))

        # LOWER score = better hand
        if hand_pwr > opp_eval:
            return 1        

        if hand_pwr == opp_eval:
            tied = True        

    if tied:
        return 2     

    return 0                
    
    
def monte_carlo( hand, players=2, samples=10000):
        dist = [0,0,0]

        for i in range(samples):
            outcome = simulate(hand[:], [], players)
            dist[outcome] += 1
        res = list(map(lambda x: x/samples, dist))
        return res
res = {}
for hand_comb in hands:
    card1,card2 = hand_to_cards(hand_comb)
    wins, _, ties = monte_carlo([card1,card2],2)
    res[card1,card2] = f"{(wins+(0.5*ties))*100:.2f}"
    

with open("preflop_equities.csv", "w") as f:
    
    for hand, equity in res.items():
        f.write(f"{hand},{equity}\n")


print("Done ✅")



