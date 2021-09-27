# Human player plays the game blackjack against a computer player
# All gameplay takes place in the terminal window
# A project based on a problem set from BU course CS111
# Professor David Sullivan, PhD
# Written by Brad Lewis

from card import *
from hand import *
import random

class Bank:
    '''A class that contains a total amount of money. The user
    can use this money to place bets.'''

    def __init__(self, total):
        self.total = total
        self.result = "push"
        self.double_down = False

    def __repr__(self):
        '''returns a string representation of the bank'''
        s = str(self.total)
        rep = "$" + s
        return rep

    def take_from(self, amt):
        self.total -= amt

    def add_to(self, amt):
        self.total += amt

    '''This allows the game result to be stored somewhere without being returned
    Possible results include "win", "blackjack", "dd win",
    "loss", "dd loss", "push" '''
    
    def game_result(self, text):
        self.result = text

    

def check_blackjack(h1):
    total = h1.get_value()
    if total == 21:
        return True
    else:
        return False

def hit_hand(player_hand, call):
    player_hand.hit()
    new_card = player_hand.cards[-1]
    if call == 'd':
        print("DOUBLE DOWN")
    else:
        print("HIT")
    print("New card: " + str(new_card))
    total = player_hand.get_value()
    print("New total: " + str(total))
    print(player_hand)

def first_move(ph, dh):
    options = ["HIT", "STAND", "DOUBLE DOWN", "SPLIT"]
    total = ph.get_value()
    dealer_card = dh.cards[0]
    dealer_rank = dealer_card.rank
    print()
    print("Dealer shows a " + str(dealer_rank))
    print("Current total is " + str(total))
    rank1 = ph.cards[0].rank
    rank2 = ph.cards[1].rank
    if rank1 != rank2:
        options.remove("SPLIT")
    if ph.get_length() > 2:
        options.remove("DOUBLE DOWN")
    print("Choose your move:")
    for i in range(len(options)):
        choice = options[i]
        let = choice[0].lower()
        if choice == "SPLIT":
            let = let + "p"
        print("   " + choice + " - " + let)
    move = input("Your choice: ")
    print()
    return move

def player_turn(player_hand,dealer_hand,bet):
    if bank.result == "blackjack":
        return 21
    playing = True
    while playing == True:           # Player turn

        move = first_move(player_hand, dealer_hand)
        total = player_hand.get_value()
        print()
        print("-" * 20)
        print()

        if move == 'd':
            bank.double_down = True
            hit_hand(player_hand, move)
            bank.take_from(bet)
            playing = False
            if total > 21:
                bank.result = "loss"
                print("BUST!")
                playing = False            

        elif move == 'h':
            hit_hand(player_hand, move)
            total = player_hand.get_value()
            if total > 21:
                bank.result = "loss"
                print("BUST!")
                playing = False

        else:       #move == 's'
            print("STAND")
            playing = False

    return total

    
def dealer_turn(dealer_hand,playing):
    dtotal = dealer_hand.get_value()
    print("Dealer hand:")
    print(dealer_hand)
    print("Dealer total is " + str(dtotal))
    print()
        
    if dtotal < 17:
        dealer_hand.hit()
        print("DEALER HIT")

    else:       #Dealer stand
        playing = False
        print("DEALER STAND")

    return playing

def get_result(bet):
    if bank.double_down == True:
        bank.result = "dd " + bank.result
    
    if bank.result == "win":
        win = bet * 2
    elif bank.result == "blackjack":
        win = round(bet * 2.5, 2)
    elif bank.result == "push":
        win = bet
    elif bank.result == "dd win":
        bet *= 2
        win = bet * 2
    else:
        win = 0

    return [win, bet]

def deal_hands():
    dealer_hand = BlackjackHand()
    player_hand = BlackjackHand()

    dealer_hand.hit()
    player_hand.hit()
    player_hand.hit()

    print("Dealer hand:")
    print(dealer_hand)
    print("Your hand:")
    print(player_hand)
    print()

    return [player_hand, dealer_hand]
    
def game(bet, bank):

    playing = True

    '''Calls the deal_hands() function which deals
        both the player hand and dealer hand '''

    these_hands_they_are_my_own = deal_hands()
    player_hand = these_hands_they_are_my_own[0]
    dealer_hand = these_hands_they_are_my_own[1]

    '''Calls check_blackjack to see if player_hand is
        a blackjack. Gameplay stops immediately
        in this case.'''

    if check_blackjack(player_hand) == True:
        bank.result = "blackjack"
        print("BLACKJACK!")

    '''Calls the player_turn() function which returns
        the total value of the hand.'''

    total = player_turn(player_hand,dealer_hand,bet)

    '''Determines whether or not the dealer needs to play.'''

    playing = False
    
    if check_blackjack(player_hand) == False and total <= 21:
        playing = True                  # Dealer turn

    while playing == True:
        playing = dealer_turn(dealer_hand,playing)

    ptotal = player_hand.get_value()
    dtotal = dealer_hand.get_value()
    print()
    print("Dealer total is " + str(dtotal))
    print("Your total is " + str(ptotal))

    if bank.result != "blackjack":
        if dtotal > 21:
            print("DEALER BUST! YOU WIN!")
            bank.result = "win"

        elif ptotal > 21:
            print("You lose :(")
            bank.result = "loss"

        elif ptotal > dtotal:
            print("YOU WIN!")
            bank.result = "win"

        elif ptotal < dtotal:
            print("You lose :(")
            bank.result = "loss"

        else:
            print("Push.")
            bank.result = "push"

    print()

    win_and_bet = get_result(bet)

    win = win_and_bet[0]
    bet = win_and_bet[1]

    bank.add_to(win)
    print()
    
    if bank.result == "push":
        print("You earned back the " + str(win) + " that you bet.")
        
    amtwon = win - bet
    if amtwon > 0:
        print("You won $" + str(amtwon) + "!")
    else:
        print("You lost " + str(bet))
    print("Your total amount of money is " + str(bank))


    print()
    again = input("Play again? y/n" )
    print()

    if again == 'y':
        a = place_bet(bank)
        game(a, bank)
    else:
        print("Thank you for playing.")
        print("Your total money remaining is " + str(bank))

def place_bet(b):
    print("You have " + str(b) + " available to bet.")
    bet = int(input("Enter your bet: "))
    while bet > b.total:
        print("That bet is more than you have available.")
        bet = int(input("Enter your bet: "))
    b.take_from(bet)
    return bet

def init_game_setup():
    b = Bank(1000)
    amt = place_bet(b)
    return [amt, b]

bet_and_bank = init_game_setup()
bet = bet_and_bank[0]
bank = bet_and_bank[1]
game(bet, bank)
