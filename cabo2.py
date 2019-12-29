from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []
player_hand = []
rejected= []

# cards enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = -1
    ACE = 1
    JOCKER = 0


# suit enum for cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'


# cabo class
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit


# function to deal full deck of cards

def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck
#shuffle
import random
random.shuffle(full_deck)
print("Your cards")
    for i in range(4)
        print(deck[i][0], 'of', full_deck[i][1])

# draw single card from deck
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)
#showHand to player_1
#def showHand(player_1):
def assignCard(player_1):
    count = 0
    while (count < 4):
        
