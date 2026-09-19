import os
import sys
import time
import random

# Constants
SUITS = ('♥', '♦', '♠', '♣')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}


# Utility functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_writer(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def banner(text):
    lines = [
        "╔" + "═" * (len(text) + 2) + "╗",
        f"║ {text} ║",
        "╚" + "═" * (len(text) + 2) + "╝"
    ]

    for line in lines:
        type_writer(line, delay=0.02)


def ascii_card(value, suit):
    v = value if len(value) == 2 else value[0]
    top = f"{v:<2}"
    bottom = f"{v:>2}"

    return [
        "┌─────────┐",
        f"│{top}       │",
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│       {bottom}│",
        "└─────────┘"
    ]


def display_hand(cards):
    arts = [ascii_card(card.rank, card.suit) for card in cards]

    for i in range(7):
        type_writer(
            "  ".join(art[i] for art in arts),
            delay=0.002
        )


# Game classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Display functions
def show_some(player, dealer):
    clear_screen()

    print("\nDEALER'S HAND:")

    hidden = [
        "┌─────────┐",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "└─────────┘"
    ]

    visible = ascii_card(
        dealer.cards[1].rank,
        dealer.cards[1].suit
    )

    for i in range(7):
        print(hidden[i] + "  " + visible[i])

    print(
        f"Dealer's Value: ??? + "
        f"{VALUES[dealer.cards[1].rank]}"
    )

    print("\nPLAYER'S HAND:")
    display_hand(player.cards)

    print(f"Player's Value = {player.value}")


def show_all(player, dealer):
    clear_screen()

    print("\nDEALER'S HAND:")
    display_hand(dealer.cards)
    print(f"Dealer's Value = {dealer.value}")

    print("\nPLAYER'S HAND:")
    display_hand(player.cards)
    print(f"Player's Value = {player.value}")


# Game logic
def take_bet(chips):
    while True:
        type_writer(
            f"Chips count: {chips.total}   "
            f"How many chips would you like to bet? ",
            delay=0.05
        )

        try:
            bet = int(input())

            if bet <= 0:
                type_writer(
                    "Bet must be greater than 0.",
                    delay=0.05
                )

            elif bet > chips.total:
                type_writer(
                    f"Not enough chips! You have: {chips.total}",
                    delay=0.05
                )

            else:
                chips.bet = bet
                break

        except:
            type_writer(
                "Please provide a valid integer.",
                delay=0.05
            )


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    while True:
        type_writer(
            "Hit or Stand? (h/s): ",
            delay=0.05
        )

        choice = input().lower()

        if choice.startswith('h'):
            hit(deck, hand)
            break

        elif choice.startswith('s'):
            type_writer(
                "Player Stands. Dealer's Turn.",
                delay=0.05
            )
            playing = False
            break

        else:
            type_writer(
                "Please enter 'h' or 's'.",
                delay=0.05
            )


def player_busts(chips):
    banner("PLAYER BUSTED!")
    chips.lose_bet()


def player_wins(chips):
    banner("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    banner("DEALER BUSTED! PLAYER WINS!")
    chips.win_bet()


def dealer_wins(chips):
    banner("DEALER WINS!")
    chips.lose_bet()


def push():
    banner("PUSH - IT'S A TIE!")


# Start screen
def start_screen():
    clear_screen()

    title = [
        "██████╗ ██╗      █████╗  ██████╗ ██╗  ██╗         ██╗  █████╗  ██████╗ ██╗  ██╗",
        "██╔══██╗██║     ██╔══██╗██╔════╝ ██║ ██╔╝         ██║ ██╔══██╗██╔════╝ ██║ ██╔╝",
        "██████╔╝██║     ███████║██║      █████╔╝          ██║ ███████║██║      █████╔╝",
        "██╔══██╗██║     ██╔══██║██║      ██╔═██╗     ██   ██║ ██╔══██║██║      ██╔═██╗",
        "██████╔╝███████╗██║   ██║╚██████╗██║  ██╗    ╚█████╔╝ ██║   ██║╚██████╗██║  ██╗",
        "╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝  ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝"
    ]

    for line in title:
        type_writer(line, delay=0.002)

    print()

    type_writer("1. Play", delay=0.03)
    type_writer("2. Quit", delay=0.03)

    while True:
        type_writer(
            "\nChoose an option (1 or 2): ",
            delay=0.03
        )

        choice = input().strip()

        if choice == '1':
            break

        elif choice == '2':
            type_writer(
                "Goodbye!",
                delay=0.05
            )
            sys.exit()

        else:
            type_writer(
                "Invalid option. Try again.",
                delay=0.05
            )


# Main game loop
start_screen()

player_chips = Chips()

while True:
    playing = True

    clear_screen()

    type_writer(
        "Welcome to BlackJack",
        delay=0.05
    )

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    take_bet(player_chips)

    show_some(
        player_hand,
        dealer_hand
    )

    while playing:
        hit_or_stand(
            deck,
            player_hand
        )

        time.sleep(1)

        show_some(
            player_hand,
            dealer_hand
        )

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(
                deck,
                dealer_hand
            )

        show_all(
            player_hand,
            dealer_hand
        )

        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()

    # Chips status
    type_writer(
        f"Chips remaining: {player_chips.total}",
        delay=0.05
    )

    # OUT OF CHIPS MENU
    if player_chips.total == 0:

        time.sleep(1)

        banner("OUT OF CHIPS!")

        type_writer(
            "1. Get 100 more chips",
            delay=0.04
        )

        type_writer(
            "2. Quit",
            delay=0.04
        )

        while True:
            type_writer(
                "\nChoose an option (1 or 2): ",
                delay=0.04
            )

            choice = input().strip()

            if choice == '1':
                player_chips.total = 100

                type_writer(
                    "You received 100 more chips!",
                    delay=0.05
                )

                time.sleep(1)
                break

            elif choice == '2':
                type_writer(
                    "Thank you for playing!",
                    delay=0.05
                )

                time.sleep(2)
                clear_screen()
                sys.exit()

            else:
                type_writer(
                    "Invalid option. Try again.",
                    delay=0.05
                )

    # Normal play-again menu
    else:
        type_writer(
            "Would you like to play another hand? y/n: ",
            delay=0.05
        )

        if not input().lower().startswith('y'):
            type_writer(
                "Thank you for playing!",
                delay=0.05
            )

            time.sleep(2)
            clear_screen()
            break