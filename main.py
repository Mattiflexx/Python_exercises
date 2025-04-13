import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Lists with player and dealer cards
start_cards_player = []
cards_dealer = []

game_on_player = True
game_on_computer = True
end_game = True

def game_bool():
    game_on_player = False
    game_on_computer = False
    end_game = False
    return game_on_player, game_on_computer, end_game

# Prompt to ask user if he/she wants to play a game of blackjack
play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n'.  ").lower()

# Checking the answer given. if 'y' start game, if 'n' end game and greet. If anything other, tell the user 'wrong input, try again'.
if play_game != "y" and play_game != "n":
    print("Wrong input. Try again.")
    game_on_player = False
    game_on_computer = False
    end_game = False
elif play_game == 'n':
    print("Have a nice day!")
    game_on_player = False
    game_on_computer = False
    end_game = False
elif play_game == 'y':
    for i in range(2):
        start_cards_player += [random.choice(cards)]
    cards_dealer += [random.choice(cards)]
    total_score_player = sum(start_cards_player)
    print(art.logo)
    print(f"Your cards: {start_cards_player}, Your current score: ", total_score_player)
    print(f"Computer's first card: {cards_dealer}")
    game_on_player = True
    game_on_computer = True
    end_game = True
    if total_score_player == 21:
        print("21. You win!")
        game_on_player = False
        game_on_computer = False
        end_game = False

while game_on_player:
    extra_card = input("Type 'y' if you want an extra card, or type 'n' if you want to pass. ").lower()

    if extra_card == "n":
        game_on_player = False

    if extra_card == "y":
        start_cards_player += [random.choice(cards)]
        total_score_player = sum(start_cards_player)
        if total_score_player > 21:
            print(f"Your cards: {start_cards_player}, Your final score: ", total_score_player)
            print("You went over. You lose.")
            game_on_player = False
            game_on_computer = False
            end_game = False
        else:
            print(f"Your cards: {start_cards_player}, Your current score: ", total_score_player)
            print(f"Computer's first card: {cards_dealer}")

cards_dealer += [random.choice(cards)]
total_score_dealer = sum(cards_dealer)
total_score_player = sum(start_cards_player)

while game_on_computer:
    if total_score_dealer < 18:
        cards_dealer += [random.choice(cards)]
        total_score_dealer = sum(cards_dealer)
    elif total_score_dealer >= 18 and total_score_dealer <= 21:
        game_on_computer = False
    elif total_score_dealer > 21:
        print("Computer went over, You win!")
        game_on_computer = False

while end_game:
    print(f"Your final cards: {start_cards_player}, Your final score: ", total_score_player)
    print(f"Computer's cards: {cards_dealer}, Computer's final score: {total_score_dealer}")

    if (total_score_player > total_score_dealer and not total_score_player > 21) or (total_score_player < total_score_dealer and total_score_dealer > 21):
        print("You win!")
    else:
        print("You lose!")
    end_game = False