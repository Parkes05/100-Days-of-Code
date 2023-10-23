## Project - Blackjack
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import sys
sys.path.append('../Data')
import os
import random
from art_11 import logo
def clear():
    os.system('cls')

def card_draw():
    '''Retruns a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    draw = random.choice(cards)
    return draw

def current_score(cards):
    '''Return 0 if Blackjack else returns sum of cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player, dealer):
    '''compares dealers and players scores'''
    if player == dealer:
        return '\nDraw\n'
    elif player == 0:
        return '\nYou have Blackjack. You win\n'
    elif dealer == 0:
        return '\nDealer has Blackjack. You lose\n'
    elif player > 21:
        return '\nYou went over. You lose\n'
    elif dealer > 21:
        return '\nDealer went over. You win\n'
    elif player > dealer :
        return '\nYou win\n'
    else: 
        return '\nYou lose\n'

def play():
    '''Plays game if player types "y"'''
    dealer_cards = []
    player_cards = []
    stop_game = False
                
    for i in range(2):
        player_cards.append(card_draw())
        dealer_cards.append(card_draw())

    while not stop_game:
        player_score = current_score(player_cards)
        dealer_score = current_score(dealer_cards)
        print(f'\nYour cards: {player_cards}, current score: {player_score}')
        print(f'Computer\'s first card: {dealer_cards[0]}')

        if player_score == 0 or dealer_cards == 0 or player_score > 21:
            stop_game = True
        else:
            add_card = input('Type "y" to add another card, type "n" to pass: ').lower()
            if add_card == 'y':
                player_cards.append(card_draw())
                player_score = current_score(player_cards)
            else:
                stop_game = True

    while dealer_score < 21 and dealer_score != 0:
        dealer_cards.append(card_draw())
        dealer_score = current_score(dealer_cards)

    print(f'\nYour final hand: {player_cards}, final score: {player_score}')
    print(f'Computer\'s final hand: {dealer_cards}, final score: {dealer_score}')
    print(compare(player_score, dealer_score))

while input('Do you want to play a game of Blackjack? Type "y" or "n": ') == 'y':
    clear()
    print(logo)
    play()