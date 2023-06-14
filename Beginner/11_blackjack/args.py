def get_chips():
    chips = input("How many chips do you want? ")
    if chips.isdigit():
        return int(chips)
    else:
        print(f"The amount you chose {chips} is not a valid number. The game will default to $500.")
        chips = 500
        return chips


def get_bet():
    bet = input("How much do you want to bet? ")
    if bet.isdigit():
        return int(bet)
    else:
        print(f"The amount you chose {bet} is not a valid number. The game will default to $100.")
        return bet
