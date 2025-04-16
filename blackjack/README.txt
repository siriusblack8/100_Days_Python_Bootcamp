# Blackjack Game

This is a simple implementation of the Blackjack card game in Python.

## Description

The game simulates a simplified version of Blackjack, where the user plays against the dealer. The game uses a standard 52-card deck (represented as a dictionary) and randomly selects cards for both the user and the dealer. The goal is to get a hand value as close to 21 as possible without exceeding it.

## Features

-   Random card selection.
-   Calculation of hand values, including handling Aces (1 or 11).
-   User interaction to draw additional cards.
-   Dealer's logic for drawing cards (dealer hits until 17 or more).
-   Win/loss determination based on Blackjack rules.

## How to Run

1.  **Prerequisites:** Python 3.x must be installed on your system.
2.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `blackjack.py`).
3.  **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command:

    ```bash
    python blackjack.py
    ```

4.  **Play the Game:** Follow the on-screen instructions to play the game.

## Game Logic

1.  **Initial Deal:** The user and the dealer are each dealt two cards.
2.  **User's Turn:**
    -   The user can choose to "hit" (draw another card) or "stand" (keep their current hand).
    -   If the user's hand value exceeds 21, they "bust" and lose.
    -   If the user's hand value is exactly 21, they win with a Blackjack (if it happens with the first two cards).
3.  **Dealer's Turn:**
    -   The dealer must hit until their hand value is 17 or more.
    -   If the dealer's hand value exceeds 21, they "bust" and the user wins.
    -   If the dealer gets blackjack on initial deal, the dealer wins.
4.  **Determine the Winner:**
    -   If neither the user nor the dealer busts, the hand with the higher value wins.
    -   If the values are the same, it is a push (tie) (not implemented in this version).

## Code Explanation

-   `random_card_selection()`: Randomly selects a card from the deck and returns its value.
-   `total_card_value(a, b)`: Calculates the total value of a hand, handling Aces as 1 or 11.
-   `blackjack()`: Implements the main game logic.

## Future Improvements

-   Implement betting.
-   Implement a push (tie) condition.
-   Improve the user interface.
-   Add support for multiple players.
-   Add more robust error handling.
-   Add a function to check for blackjack on the initial deal for the dealer.
