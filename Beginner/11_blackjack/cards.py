import itertools
import random

CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
CARD_NAMES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
SUITS = ["\u2663", "\u2666", "\u2665", "\u2660"]  # Suits

ALL_CARDS_VALUES = list(zip(CARD_NAMES, CARD_VALUES))
DECK = list(itertools.product(SUITS,
                              ALL_CARDS_VALUES))

# Shuffle the deck
random.shuffle(DECK)


def format_card(card):
    """
    Formats a card draw from the deck.
    Parameters
    ----------
    card
        A card draw from the deck in the format
        ('SUIT', ('CARD_NAME', 'CARD_VALUE'))
    Returns
    -------
    card_string
        String representation with card value and suit.

    """
    suit, name_value = card
    return f"{name_value[0]}{suit}"


def check_if_ace(hand):
    for card in hand:
        _, name_value = card
        if name_value[0] == 'Ace':
            return True
    return False


def check_blackjack(hand):
    is_blackjack = 0

    for card in hand:

        _, name_value = card

        if name_value[0] == 'Ace':
            is_blackjack += 1

        elif name_value[0] == '10':
            is_blackjack += 1

    if is_blackjack < 2:
        return False
    return True


def deal_one():
    """
    Deals a random card from the deck.
    Returns
    -------
        A random card from DECK
    """
    card_index = random.randint(0, len(DECK) - 1)
    return DECK[card_index]


def deal_hand():
    """
    Deals a hand (2 cards) from the deck.
    Returns
    -------
        A random card from DECK
    """
    return [deal_one(), deal_one()]


def get_cards_total(cards):
    total = 0
    for card in cards:
        _, name_value = card
        total += name_value[1]
    return total


def show_hand(player, cards):
    text = f"{player}'s cards: "
    for idx, card in enumerate(cards):
        card_format = format_card(card)
        text += f'{card_format}, '
    return text
