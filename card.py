#
# card.py
#
# CS 111, Boston University
#

RANK_NAMES = {'A': 'Ace', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'}
SUIT_NAMES = {'C': 'Clubs', 'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds'}

class Card:
    """ a class for objects that represent a single card
        from a deck of cards. Each Card has two attributes:
          - a rank, which is either an int or a single-letter upper-case string
          - a suit, which is a single-letter upper-case string
        For example:
          - the 10 of Clubs has rank 10 and suit 'C'
          - the Ace of Hearts has rank 'A' and suit 'H'
    """
    def __init__(self, rank, suit):
        """ constructor for Card objects """
        if type(rank) == int:
            self.rank = rank
        else:
            self.rank = rank[0].upper()
        self.suit = suit[0].upper()

    def __repr__(self):
        """ returns a string representation of the
            called Card object (self)
        """
        s = str(self.rank)
        if s in RANK_NAMES:
            n = RANK_NAMES[s]
        else:
            n = s

        n += ' of '
        n += SUIT_NAMES[self.suit]
        
        return n

    def get_value(self):
        """ returns the value of the called Card object (self) """
        if type(self.rank) == int:
            return self.rank
        elif self.rank == 'A':
            return 1
        else:
            return 10
