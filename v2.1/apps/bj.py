import random
import os
import keyboard
keyboard.send('F11')
# Card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Function to create and shuffle the deck
def create_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand(hand):
    value = sum(card_values[card] for card in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to display the player's and dealer's hands
def show_hands(player_hand, dealer_hand, hide_dealer_card=True):
    print(f"Player's hand: {', '.join(player_hand)} (Value: {calculate_hand(player_hand)})")
    if hide_dealer_card:
        print(f"Dealer's hand: {dealer_hand[0]}, ?")
    else:
        print(f"Dealer's hand: {', '.join(dealer_hand)} (Value: {calculate_hand(dealer_hand)})")

# Function to load the player's money from file
def load_money():
    if os.path.exists("bjmoney.txt"):
        with open("bjmoney.txt", "r") as file:
            return int(file.read().strip())
    else:
        return 100  # Start with $100 if no file exists

# Function to save the player's money to file
def save_money(money):
    with open("bjmoney.txt", "w") as file:
        file.write(str(money))

# Main game function
def blackjack():
    money = load_money()

    print("Welcome to Blackjack!")
    print(f"You have ${money}.")

    while True:
        if money <= 0:
            print("You're out of money! Game over.")
            return

        try:
            bet = int(input(f"How much would you like to bet? (You have ${money}): "))
            if bet > money:
                print("You cannot bet more than you have.")
                continue
            if bet <= 0:
                print("Bet must be a positive amount.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        deck = create_deck()

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Player's turn
        while True:
            show_hands(player_hand, dealer_hand)
            if calculate_hand(player_hand) == 21:
                print("Blackjack! You win!")
                money += bet
                break
            choice = input("Do you want to [h]it or [s]tand? ").lower()
            if choice == 'h':
                player_hand.append(deck.pop())
                if calculate_hand(player_hand) > 21:
                    show_hands(player_hand, dealer_hand, hide_dealer_card=False)
                    print("Bust! You lose.")
                    money -= bet
                    break
            elif choice == 's':
                break

        # Dealer's turn
        if calculate_hand(player_hand) <= 21:
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            # Show final hands
            show_hands(player_hand, dealer_hand, hide_dealer_card=False)

            # Determine the winner
            player_value = calculate_hand(player_hand)
            dealer_value = calculate_hand(dealer_hand)

            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
                money += bet
            elif player_value < dealer_value:
                print("Dealer wins.")
                money -= bet
            else:
                print("It's a tie! No money lost or gained.")

        save_money(money)
        print(f"You now have ${money}.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print(f"You leave the game with ${money}.")
    save_money(money)

# Run the game
if __name__ == "__main__":
    blackjack()
