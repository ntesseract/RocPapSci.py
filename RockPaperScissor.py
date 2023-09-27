import random

def create_header(title, creator):
    # Creating Box model to be the header
    title_length = len(title)
    cr_length = len(creator)
    box_width1 = title_length + 2
    box_width2 = title_length - cr_length
    paddingcont2 = " " * box_width2

    top_border = "+" + "-" * box_width1 + "+"
    boxContent1 = f"| {title} |"
    boxContent2 = f"| {creator}" + paddingcont2 + " |"
    bottom_border = "+" + "-" * box_width1 + "+"

    header = "\n".join([top_border, boxContent1, boxContent2, bottom_border])

    return header

def get_player_choice():
    while True:
        print("Choose one:\n1. Rock\n2. Paper\n3. Scissors")
        choice = input("Input number (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            # In case if the choice are not in list
            print("Your choice are incorrect, Please choose one between 1, 2, or 3.")

def determine_winner(player_choice, computer_choice):
    # Giving a win condition in game
    if player_choice == computer_choice:
        return "Draw"
    if (
        (player_choice == "Rock" and computer_choice == "Scissor")
        or (player_choice == "Scissor" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    ):
        return "Win"
    return "Lose"

def main():
    # Title Game and the credits
    title = "Rock, Paper, and Scissors"
    creator = "By NTesseract"
    header = create_header(title, creator)
    print(header)

    while True:
        # Player choice
        player_choice = get_player_choice()
        if player_choice == "1":
            player_choice_str = "Rock"
        elif player_choice == "2":
            player_choice_str = "Paper"
        else:
            player_choice_str = "Scissors"

        print(f"You're choosing: {player_choice_str}")

        # Randomized Computer choice
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        print(f"Computer choose: {computer_choice}")

        result = determine_winner(player_choice_str, computer_choice)
        if result == "Win":
            print("You Win!")
        elif result == "Lose":
            print("You Lose.")
        else:
            print("It's Draw.")

        # This one is defenitely a retry option
        play_again = input("Play again? (type 'yes' to continue): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
