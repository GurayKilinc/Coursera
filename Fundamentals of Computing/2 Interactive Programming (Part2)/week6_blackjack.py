# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
score = 0
deck = []
dealer = []
player = []
d_pos = (100, 120)
p_pos = (100, 300)

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        hand_cards = ""
        for i in range(len(self.cards)):
            hand_cards = hand_cards + self.cards[i].get_suit() + self.cards[i].get_rank() + " "
        return "Hand contains " + hand_cards

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        points = 0
        ace = 0
        for card in self.cards:
            points += VALUES[card.get_rank()]
            if card.get_rank() == 1:
                ace += 1
        if ace > 0 and points < 12:
            points += 10
        return points
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, (pos[0] + i * CARD_SIZE[0], pos[1]))
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i, j))


    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        temp_card = random.choice(self.deck)
        self.deck.remove(temp_card)
        return temp_card
    
    def __str__(self):
        # return a string representing the deck
        deck_cards = ""
        for i in range(len(self.deck)):
            deck_cards = deck_cards + self.deck[i].get_suit() + self.deck[i].get_rank() + " "
        return "Deck contains " + deck_cards


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, outcome, score
    if in_play == True:
        outcome = "Player has lost!"
        score -= 1
    deck = Deck()
    player = Hand()
    dealer = Hand()
    outcome = "Hit or stand?"
    
    deck.shuffle()
    player_card = deck.deal_card()
    player.add_card(player_card)
    # print("Player's first card: " + player_card.get_suit() + player_card.get_rank())
    player_card = deck.deal_card()
    player.add_card(player_card)
    # print("Player's second card: " + player_card.get_suit() + player_card.get_rank())
    
    dealer_card = deck.deal_card()
    dealer.add_card(dealer_card)
    # print("Dealer's first card: " + dealer_card.get_suit() + dealer_card.get_rank())
    dealer_card = deck.deal_card()
    dealer.add_card(dealer_card)
    # print("Dealer's second card: unknown")
    
    in_play = True

def hit():
    global in_play, deck, player, outcome, score
    player_card = deck.deal_card()
    player.add_card(player_card)
    # print("Player's new card: " + player_card.get_suit() + player_card.get_rank())
    if player.get_value() > 21:
        # print("You have busted!")
        outcome = "You have busted!"
        score -= 1
 
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, dealer, player, outcome, score
    in_play = False
    # print("Dealer's second card: " + dealer.cards[1].get_suit() + dealer.cards[1].get_rank())
    while dealer.get_value() < 17:
        dealer_card = deck.deal_card()
        dealer.add_card(dealer_card)
        # print("Dealer's new card: " + dealer_card.get_suit() + dealer_card.get_rank())
    if dealer.get_value() > 21:
        # print("Dealer has busted!")
        outcome = "Dealer has busted!"
        score += 1
    else:
        if player.get_value() > dealer.get_value():
            # print("Player has won!")
            outcome = "Player has won!"
            score += 1
        else:
            # print("Dealer has won!")
            outcome = "Dealer has won!"
            score -= 1
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global outcome, score, in_play
    dealer.draw(canvas, d_pos)
    player.draw(canvas, p_pos)
    canvas.draw_text(outcome, (300, 250), 30, "white")
    canvas.draw_text("Blackjack", (50, 50), 30, "white")
    canvas.draw_text("Dealer", (50, 100), 30, "white")
    canvas.draw_text("Player", (50, 250), 30, "white")
    canvas.draw_text("Score: " + str(score), (300, 50), 30, "white")
    if in_play == True:
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_SIZE, (d_pos[0]+CARD_CENTER[0], d_pos[1]+CARD_CENTER[1]), CARD_SIZE)
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric