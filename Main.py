import random

# Deals a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculates the score of the given cards
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to play the game
def play_game(balance):
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    is_game_over = False

    print(f"Your current balance is: ${balance}")
    bet = int(input("How much would you like to bet? $"))
    
    # Checks the user has enough balance
    if bet > balance:
        print("You do not have enough balance to make this bet.")
        return balance  # Exit the game without deducting

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"The dealer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    if user_score == 0:
        print(f"Your final hand is {user_cards}, final score: 21 *** BLACKJACK ***")
    else:   
        print(f"Your final hand is {user_cards}, final score: {user_score}")

    print(f"The dealer's hand is {computer_cards}, final score: {computer_score}")

    # Determine the result and adjust balance
    if user_score > 21:
        print("You lose, you went over 21.")
        balance -= bet
    elif computer_score > 21:
        print("Dealer went over. You win!")
        balance += bet
    elif user_score == 0:
        print("Blackjack! You win 4x your bet!")
        balance += 4 * bet
    elif computer_score == 0:
        print("Dealer has blackjack. You lose.")
        balance -= bet
    elif user_score > computer_score:
        print("You win!")
        balance += bet
    elif user_score < computer_score:
        print("You lose.")
        balance -= bet
    else:
        print("It's a draw. Your bet is returned.")

    print(f"Your new balance is: ${balance}")
    return balance

# Main game loop
def main():
    balance = 0
    while True:
        if balance == 0:
            deposit = int(input("You have no money. How much would you like to deposit? $"))
            balance += deposit
        
        play_again = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if play_again.lower() == "y":
            balance = play_game(balance)
        else:
            print(f"Thanks for playing! Your final balance is: ${balance}")
            break

main()