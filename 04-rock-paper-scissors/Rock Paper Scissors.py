import random
import os
import time


# =========================
# CLEAR SCREEN
# =========================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# ASCII ART
# =========================

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
move_names = ["Rock", "Paper", "Scissors"]


# =========================
# GAME
# =========================

def play_game():

    player_score = 0
    computer_score = 0
    round_number = 1

    while player_score < 2 and computer_score < 2:

        clear_screen()

        print("=" * 40)
        print("        ROCK PAPER SCISSORS")
        print("=" * 40)

        print(f"\nROUND {round_number}")
        print(f"\nPlayer: {player_score}   |   Computer: {computer_score}")

        print("\nChoose your move:")
        print("0 - Rock")
        print("1 - Paper")
        print("2 - Scissors")

        # Player choice
        while True:
            try:
                player_choice = int(input("\nYour choice: "))

                if player_choice in [0, 1, 2]:
                    break
                else:
                    print("❌ Invalid choice! Choose 0, 1 or 2.")

            except ValueError:
                print("❌ Please enter a number!")

        # Computer choice
        computer_choice = random.randint(0, 2)

        clear_screen()

        print("=" * 40)
        print(f"              ROUND {round_number}")
        print("=" * 40)

        print("\nYou chose:")
        print(moves[player_choice])

        print("\nComputer chose:")
        print(moves[computer_choice])

        # =========================
        # RESULT
        # =========================

        if player_choice == computer_choice:

            print("\n🤝 IT'S A DRAW!")
            print("Nobody gets a point.")

        elif (
            (player_choice == 0 and computer_choice == 2)
            or
            (player_choice == 1 and computer_choice == 0)
            or
            (player_choice == 2 and computer_choice == 1)
        ):

            player_score += 1

            messages = [
                "🔥 NICE MOVE!",
                "💪 YOU GOT THIS ROUND!",
                "😎 WELL PLAYED!",
                "🏆 POINT FOR YOU!"
            ]

            print(f"\n🎉 {random.choice(messages)}")
            print("You win this round!")

        else:

            computer_score += 1

            messages = [
                "💀 COMPUTER WINS!",
                "🤖 THE COMPUTER GOT YOU!",
                "😬 UNLUCKY!",
                "⚡ COMPUTER TAKES THE ROUND!"
            ]

            print(f"\n{random.choice(messages)}")
            print("You lose this round!")

        print(f"\nSCORE: {player_score} - {computer_score}")

        round_number += 1

        time.sleep(2)


    # =========================
    # FINAL SCREEN
    # =========================

    clear_screen()

    print("=" * 40)
    print("            FINAL RESULT")
    print("=" * 40)

    print(f"\nPlayer:    {player_score}")
    print(f"Computer:  {computer_score}")

    if player_score > computer_score:
        print("\n🏆 YOU WON THE MATCH!")
        print("Congratulations! You defeated the computer!")

    else:
        print("\n💀 YOU LOST THE MATCH!")
        print("The computer takes the victory!")

    print("\n" + "=" * 40)


# =========================
# MAIN MENU
# =========================

while True:

    clear_screen()

    print("=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)

    print("\n1. Play")
    print("2. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        play_game()

        print("\nWould you like to play again?")
        print("1. Play Again")
        print("2. Main Menu")

        again = input("\nChoose an option: ")

        if again == "1":
            continue
        else:
            continue

    elif choice == "2":

        clear_screen()

        print("=" * 40)
        print("       THANKS FOR PLAYING!")
        print("=" * 40)

        break

    else:

        print("\n❌ Invalid option!")

        time.sleep(1.5)