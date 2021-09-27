#
# hand.py
#
# CS 111, Boston University
#

from card import *
import random

class Hand:
    """ a class for objects that represent a single hand of cards """

    def __init__(self):
        """ constructor for Hand objects """
        self.cards = []

    def __repr__(self):
        """ returns a string representation of the called Hand object (self) """
        return str(self.cards)

    def add_card(self, card):
        """ add the specified Card object (card) to the list of cards
            for the called Hand object (self)
        """
        self.cards += [card]

    def num_cards(self):
        '''returns the number of cards in the hand object'''
        num = len(self.cards)
        return num

    def get_length(self):
        length = len(self.cards)
        return length

    def get_value(self):
        
        total_val = 0
        
        for i in self.cards:
            total_val += i.get_value()

        return total_val

    def has_any(self, check):

        for i in self.cards:
            if i.rank == check:
                return True

        return False

class BlackjackHand(Hand):

    def get_value(self):

        value = super().get_value()

        ace_boo = False

        for i in self.cards:
            if i.rank == 'A':
                ace_boo = True

        if ace_boo == True:
            if value <= 11:
                value += 10

        return value

    def hit(self):

        rank_list = ['A', 'K', 'Q', 'J', 10,9,8,7,6,5,4,3,2]
        suit_list = ['H', 'D', 'C', 'S']

        new_card_rank = random.choice(rank_list)
        new_card_suit = random.choice(suit_list)

        c1 = Card(new_card_rank, new_card_suit)

        self.add_card(c1)
                
            
