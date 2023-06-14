from args import get_chips, get_bet
from cards import check_blackjack, check_if_ace, deal_hand, deal_one, get_cards_total, show_hand
from utils import clear
from typing import Tuple
from art import NO_CHIPS, LOGO, THANKS

print(LOGO)

print("""
Welcome to BlackJack 1.0!
In this game you win if you manage to
score higher than the computer, but lower or equal to 21.
""")


# TODO
# TODO A bug might happen if BET > CHIPS
# TODO FIX LATER


def take_turn() -> str:
    """
    Returns
    -------
    action
        A string representing an action in Blackjack.
        'hit', 'stand', 'double down' or 'surrender'.
    """

    action = str(input("What do you want to do: 'hit', 'stand', 'double down' or 'surrender':\n")).lower()
    return action


def check_results(player_points: int, dealer_points: int, chips: int, bet: int) -> Tuple[int, str]:
    """
    Check which player won the game.

    Parameters
    ----------
    player_points
        Number of points in player's hand.
    dealer_points
        Number of points in dealer's hand.
    chips
        Amount of money left in player's purse.
    bet
        How much was bet in current game.

    Returns
    -------
        Updated chips (after win or defeat) and a text showing the results.
    """

    if player_points > dealer_points and player_points <= 21:
        result = f"Player wins!\nPlayer's score: {player_points}\nDealer's score: {dealer_points}"

        chips += bet

    elif dealer_points > player_points and dealer_points <= 21:
        result = f"Dealer wins!\nPlayer's score: {player_points}\nDealer's score: {dealer_points}"
        chips -= bet

    elif player_points == dealer_points:
        result = f"Push!\nPlayer's score: {player_points}\nDealer's score: {dealer_points}"
        chips -= bet

    elif dealer_points > 21 and player_points <= 21:
        result = f"Dealer bust!\nPlayer's score: {player_points}\nDealer's score: {dealer_points}"
        chips += bet

    else:
        result = f"Player bust!\nPlayer's score: {player_points}\nDealer's score: {dealer_points}"
        chips -= bet

    return chips, result


def play(chips: int, bet: int):
    """
    Start a Blackjack session.
    The game will proceed until
    a player busts, wins or score's a Blackjack (Ace + 10).

    Blackjack rules:

    -> The goal of blackjack is to beat the dealer's hand without going over 21. -> Each player is dealt 2 cards to
    start. -> Aces can be worth 1 or 11, face cards (King, Queen, Jack) are worth 10, and all other cards are worth
    their face value. -> Players can choose to "hit" and receive additional cards in an attempt to get closer to 21,
    or "stand" and keep their current hand. -> If a player's hand exceeds 21, they "bust" and lose the game. -> Once
    all players have finished their turns, the dealer reveals their second card and hits until their hand has a value
    of at least 16. -> If the dealer's hand exceeds 21, all remaining players win the game. -> If the dealer and a
    player both have hands with a value of less than or equal to 21, the one with the highest value wins. Parameters
    ---------- chips Amount of money left in player's purse. bet How much was bet in current game.
    """

    START_GAME = True
    player_hand = deal_hand()
    dealer_hand = deal_hand()

    while START_GAME is True and chips > 0:
        print(f"Chips left: {chips}")
        print(f"Bet: {bet}")

        player_points = get_cards_total(player_hand)
        dealer_points = get_cards_total(dealer_hand)

        print(show_hand('Player', player_hand))
        print(show_hand('Dealer', dealer_hand))
        print()

        print("Let's play")
        turn = take_turn()

        if turn == 'double down':
            bet *= 2
            print(f"You just doubled your bet to ${bet}")

        elif turn == 'hit':
            clear()
            deal_more = 'y'
            while deal_more == 'y':
                card = deal_one()
                player_hand.append(card)
                print(show_hand('Player', player_hand))
                player_points += get_cards_total([card])

                if player_points < 21:
                    deal_more = str(input("Deal more?: 'y' or 'n'")).lower()

                if player_points >= 21:
                    deal_more = 'n'

        elif turn == 'surrender':
            chips += bet // 2
            print(f"Returning half of your ${bet}.\nYou still have ${chips} left.")

        elif turn == 'stand':
            print(f"Showing hands:\n")
            print(show_hand('Player', player_hand))
            print(show_hand('Dealer', dealer_hand))
            print()
            clear()

        # If the dealer has less than 17 points, try to deal
        while dealer_points <= 16:
            print('Dealer is drawing a card.')
            new_card = deal_one()
            dealer_hand.append(new_card)
            dealer_points += get_cards_total([new_card])
            clear()
        print(show_hand('Dealer', dealer_hand))

        # Check if anyone has an Ace
        player_has_ace = check_if_ace(player_hand)
        dealer_has_ace = check_if_ace(dealer_hand)

        if player_has_ace and player_points > 21:
            print("Player has an ace, but more than 21. Ace will now count as 1 point.")
            player_points -= 10
            if check_blackjack(player_hand):
                print(f"PLAYER BLACKJACK!")
        if dealer_has_ace and dealer_points > 21:
            print("Dealer has an ace, but more than 21. Ace will now count as 1 point.")
            print(f"DEALER BLACKJACK!")
            dealer_points -= 10

        chips, outcome = check_results(player_points, dealer_points, chips, bet)
        print(outcome)

        print(f"Remaining chips: ${chips}")

        # Check if player wants to keep playing.
        keep_playing = str(input("Keep playing?: 'y' or 'n'"))
        clear()

        if chips <= 0:
            print("You don't have anymore money!")
            print(NO_CHIPS)
            START_GAME = False

        if keep_playing == 'y':
            player_hand = deal_hand()
            dealer_hand = deal_hand()
            bet = get_bet()
            if bet > chips:
                bet = int(input("Your previous bet was higher than the amount of money you have."
                                "\nPick another value: "))

        if keep_playing == 'n':
            print("See you next time!\nEND GAME.")
            print(f"Remaining chips: ${chips}")
            START_GAME = False

    clear()
    print(THANKS)


if __name__ == '__main__':
    CHIPS = get_chips()
    BET = get_bet()
    if BET > CHIPS:
        BET = int(input("Your previous bet was higher than the amount of money you have.\nPick another value: "))
    clear()
    play(CHIPS, BET)
