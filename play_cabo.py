from enum import Enum
from enum import IntEnum
from random import * 

full_deck = []
partial_deck = []

# cards enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN= 7
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
   #function to deal full deck of cards

def create_deck():
    for suit in Suit : 
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit))) 
    return full_deck

# draw single card from deck 
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)
#dealer 4 cards for each player 
#1st round of a game turn 1st 
#each player is checking his 2 of 4 random hand cards

#1st round of a game turn 2nd
#player1 takes one card from stock 

def deal_1st():
    while(len(partial_deck) > 0): 
        player1_cards.append(drew_card(partial_deck))
        
create_deck()
partial_deck = list(full_deck)
deal_1st()

for i in range(0, len(player1_cards)):   
    if (player1_cards[i].card > player1_cards[j].card):
        return player1_cards[i].card(rand_card)
    if (player1_cards[i].card < player1_cards[j].card):
        return player1_cards[j].card()

def deal_player1_cards():
    print('\nYou are dealt the following four cards:')
    player_hand = []
    for i in range(4):
        letters_list = ['a', 'b', 'c', 'd']
        given_card = ran _card()
        if given_card not in player_hand:
            print('%s) %s of %s' %
                  (letters_list[i]),
                  draw_card
            player1_cards.append(drew_card(partial_deck))
#player 1 returns or swap card 
def discard_card():
    print('\nYou may choose to discard up 1 card for new one.') 
    print('Which card do you wish to swap (0-1)'?)
    while True:
            try:
                  discard_x_cards = int(input('\n>'))
                  if valid_discard_num (discard_x_cards):
                    break
                  else: 
                    print('That is not allowed. Please choose between 0 and 1 card to discard.')
            except ValueError:
                  print('Invalid command. Imput a number between 0-1.')
    return discard_x_cards
# return true onlu when the player1 choose to discard 0-1 cards
def valid_discard_num(discard_num):
    if 0 <= discard_num <= 1:
                return True
#ask to specify what card is to be discarded one at the time
# if no card is to be discarded, then return none
# otherwise, the function returns a list of lower-case letters (representing cards) to be discarded
def specify_discard_cards (tot_discarded_cards):
                if tot_discarded_cards == 0:
                            print('\nYou choose to stick with the hand you were dealt.')
                            return [] #empty = no cards
                            discard_card_list = []
                  i = 0
                while i < tot_discarded_cards:
                    print('nType the letter of card #%s to be discarded. (a-d)' % (i+1)) 
                    discard_card = input('>').lower()
                    if not valid_card_letter(discard_card):
                        continue 
                  discard_card_list.append(discard_card)
                  i = i + 1
                return discard_card_list
#return true if player inputs a letter between a-d (representing one card from the player's hand)
#return false plus a printed info message if the user does not type a valid letter
#uses inputted letter as an argument 
def valid_card_letter(letter_input):
                  four letters = ['a', 'b', 'c', 'd']
                if letter_input.lower() not in four_letters:
                    print("that's not allowed. Choose one card with an assigned letter (a-d)")
                    return False
                else:
                  return True
#returns true if the user hasn't already chosen a letter representing a card to discard
#return false and a print info message if the user chooses the same card to discard again
#first argument is the inputted letter. Second argument is a list of already inputted letters

def check_card_exists(letter_input, used_letters):
	if letter_input.lower() not in used_letters:
		return True
	else:
		print('You already chose to discard this card. What else will you discard?')
		return False

#player2 takes one card from stock
#player3 takes one card from stock 
#player4 takes one card from stock

 
 
