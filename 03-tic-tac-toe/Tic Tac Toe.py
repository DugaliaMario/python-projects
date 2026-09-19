import time
import random
import os

import os
import time
import random

# ================= UTIL =================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_writer(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# ================= BOARD =================

def display_board(board):
    clear_screen()
    print("\n    TIC TAC TOE\n")
    print("      |     |     ")
    print(f"   {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print(f"   {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print(f"   {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("      |     |     ")


def display_position_guide():
    print("\nPOSITION GUIDE:\n")
    print("      |     |     ")
    print("   1  |  2  |  3  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print("   4  |  5  |  6  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print("   7  |  8  |  9  ")
    print("      |     |     \n")


# ================= GAME LOGIC =================

def player_input():
    marker = ''

    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose X or O: ").upper()

    return ('X', 'O') if marker == 'X' else ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark)
    )


def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))


def player_choice(board):
    while True:
        try:
            pos = int(input("Choose your position (1-9): "))

            if pos in range(1, 10) and space_check(board, pos):
                return pos

            type_writer("Invalid or occupied position.")

        except ValueError:
            type_writer("Please enter a number between 1 and 9.")


# ================= EASY AI =================

def easy_ai_choice(board):
    """
    Easy AI:
    Alege o pozitie libera la intamplare.
    """

    available = [
        i for i in range(1, 10)
        if space_check(board, i)
    ]

    return random.choice(available)


# ================= IMPOSSIBLE AI =================

def minimax(board, ai_marker, player_marker, maximizing):
    """
    Minimax:
    Computerul analizeaza toate mutarile posibile
    si alege rezultatul cel mai bun pentru el.
    """

    # Computerul a castigat
    if win_check(board, ai_marker):
        return 10

    # Playerul a castigat
    if win_check(board, player_marker):
        return -10

    # Tabla este plina -> egal
    if full_board_check(board):
        return 0

    available = [
        i for i in range(1, 10)
        if space_check(board, i)
    ]

    if maximizing:
        best_score = -float('inf')

        for position in available:
            board[position] = ai_marker

            score = minimax(
                board,
                ai_marker,
                player_marker,
                False
            )

            board[position] = ' '

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for position in available:
            board[position] = player_marker

            score = minimax(
                board,
                ai_marker,
                player_marker,
                True
            )

            board[position] = ' '

            best_score = min(best_score, score)

        return best_score


def impossible_ai_choice(board, ai_marker, player_marker):
    """
    AI Impossible:
    Analizeaza fiecare mutare posibila si o alege
    pe cea care produce cel mai bun rezultat.
    """

    best_score = -float('inf')
    best_moves = []

    available = [
        i for i in range(1, 10)
        if space_check(board, i)
    ]

    for position in available:
        board[position] = ai_marker

        score = minimax(
            board,
            ai_marker,
            player_marker,
            False
        )

        board[position] = ' '

        if score > best_score:
            best_score = score
            best_moves = [position]

        elif score == best_score:
            best_moves.append(position)

    # Daca mai multe mutari sunt la fel de bune,
    # alege una dintre ele aleatoriu.
    return random.choice(best_moves)


# ================= AI LEVEL =================

def choose_ai_level():
    while True:
        clear_screen()

        print("\n    COMPUTER DIFFICULTY\n")
        print("    1. Easy")
        print("    2. Impossible\n")

        choice = input("Choose difficulty (1-2): ").strip()

        if choice == '1':
            return 'easy'

        elif choice == '2':
            return 'impossible'

        type_writer("Invalid choice. Try again.", 0.04)
        time.sleep(1)


# ================= REPLAY =================

def replay():
    return input("Play again? (yes / no): ").lower().startswith('y')


# ================= MENU =================

def interactive_menu():
    while True:
        clear_screen()

        type_writer("WELCOME TO TIC TAC TOE\n", 0.04)

        type_writer("1. Player vs Computer")
        type_writer("2. Player vs Player")
        type_writer("3. Quit\n")

        choice = input("Choose an option (1-3): ").strip()

        if choice in ['1', '2', '3']:
            return choice

        type_writer("Invalid choice. Try again.", 0.04)
        time.sleep(1)


# ================= MAIN =================

def main():

    choice = interactive_menu()

    if choice == '3':
        type_writer("Goodbye!", 0.05)
        return

    # Alegem dificultatea doar pentru Player vs Computer
    ai_level = None

    if choice == '1':
        ai_level = choose_ai_level()

    the_board = [' '] * 10

    clear_screen()
    display_position_guide()

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    type_writer(
        f"\n{turn} will go first.\n",
        0.05
    )

    game_on = True

    while game_on:

        # ================= PLAYER 1 =================

        if turn == 'Player 1':

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(
                the_board,
                player1_marker,
                position
            )

            if win_check(the_board, player1_marker):

                display_board(the_board)

                type_writer(
                    "🎉 PLAYER 1 WINS! 🎉",
                    0.04
                )

                game_on = False

            elif full_board_check(the_board):

                display_board(the_board)

                type_writer(
                    "It's a tie!",
                    0.04
                )

                break

            else:
                turn = 'Player 2'

        # ================= COMPUTER / PLAYER 2 =================

        else:

            display_board(the_board)

            if choice == '1':

                type_writer(
                    "Computer is thinking...",
                    0.04
                )

                time.sleep(1)

                # EASY
                if ai_level == 'easy':

                    position = easy_ai_choice(
                        the_board
                    )

                # IMPOSSIBLE
                else:

                    position = impossible_ai_choice(
                        the_board,
                        player2_marker,
                        player1_marker
                    )

            else:

                position = player_choice(
                    the_board
                )

            place_marker(
                the_board,
                player2_marker,
                position
            )

            if win_check(the_board, player2_marker):

                display_board(the_board)

                winner = (
                    "COMPUTER"
                    if choice == '1'
                    else "PLAYER 2"
                )

                type_writer(
                    f"🎉 {winner} WINS! 🎉",
                    0.04
                )

                game_on = False

            elif full_board_check(the_board):

                display_board(the_board)

                type_writer(
                    "It's a tie!",
                    0.04
                )

                break

            else:
                turn = 'Player 1'

    # ================= REPLAY =================

    if replay():
        main()

    else:
        type_writer(
            "Thanks for playing!",
            0.05
        )


# ================= RUN =================

if __name__ == "__main__":
    main()
