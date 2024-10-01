# client_tasks.py

import random
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the main window

def main_menu():
    while True:
        choice = simpledialog.askstring("Main Menu",
                                        "Select a task to start:\n"
                                        "1. Guess the Number Game\n"
                                        "2. Find the Spot\n"
                                        "3. Product Package Counter\n"
                                        "4. Exit\n\n"
                                        "Enter your choice (1-4):")
        if choice is None:
            # User closed the dialog
            continue
        choice = choice.strip()
        if choice == '1':
            guess_the_number_game()
        elif choice == '2':
            find_the_spot()
        elif choice == '3':
            product_package_counter()
        elif choice == '4':
            messagebox.showinfo("Goodbye", "Thank you for using the Client Tasks Application. Goodbye!")
            break
        else:
            messagebox.showerror("Invalid Choice", "Please enter a valid option (1-4).")

# Client Task A: Guess the Number Game #
# Add your pseudocode to this file below this line: #
'''
1. Initialize the game
2. Initialize totalGamesPlayed to 0
3. Initialize totalGamesWon to 0
4. Set playAgain to True
5. WHILE playAgain is True DO:
6.     Increment totalGamesPlayed by 1
7.     Generate a random number between 1 and 10 (inclusive)
8.     Initialize the maximum number of attempts to 3
9.     Initialize attemptsUsed to 0
10.    While attemptsUsed < maximum number of attempts DO:
11.        Prompt the player to guess the number
12.        Read the player's input
13.        If the player's input is not a valid integer between 1 and 10:
14.            Print "Invalid input. Please enter a whole number between 1 and 10."
15.            Continue to the next iteration of the loop
16.        If the player's guess is correct:
17.            Print "Congratulations! You guessed the correct number: " + randomNumber
18.            Print "You win the game!"
19.            Increment totalGamesWon by 1
20.            End the current game
21.        Otherwise, inform the player that their guess was incorrect, provide feedback such as "too high" or "too low," and encourage the player to try again
22.        Decrease the number of attempts by 1
23.    If the player has no attempts left:
24.        Print "Sorry, you've used all your attempts."
25.        Print "The correct number was: " + randomNumber
26.        Print "Game Over."
27.    Print "Total Games Played: " + totalGamesPlayed
28.    Print "Total Games Won: " + totalGamesWon
29.    Prompt the player to ask if they want to play again (yes/no)
30.    Read the player's response
31.    If the player's response is "yes":
32.        Set playAgain to True
33.    Else:
34.        Set playAgain to False
35.        Print "Thank you for playing! Goodbye."
'''
def guess_the_number_game():
    """
    Client Task A: Guess the Number Game
    """
    total_games_played = 0
    total_games_won = 0
    play_again = True

    while play_again:
        total_games_played += 1
        random_number = random.randint(1, 10)
        max_attempts = 3
        attempts_used = 0
        game_won = False

        messagebox.showinfo("Guess the Number Game",
                            "Welcome to the Guess the Number Game!\n"
                            "I have selected a number between 1 and 10.\n"
                            "You have 3 attempts to guess the number correctly.")

        while attempts_used < max_attempts:
            guess = simpledialog.askstring("Guess the Number",
                                          f"Attempt {attempts_used + 1}: Please enter your guess (1-10):")
            if guess is None:
                # User canceled the input
                continue
            guess = guess.strip()
            if not guess.isdigit():
                messagebox.showerror("Invalid Input", "Invalid input. Please enter a whole number between 1 and 10.")
                continue
            guess = int(guess)
            if guess < 1 or guess > 10:
                messagebox.showerror("Invalid Input", "Invalid input. Please enter a whole number between 1 and 10.")
                continue

            if guess == random_number:
                messagebox.showinfo("Congratulations!",
                                    f"Congratulations! You guessed the correct number: {random_number}\nYou win the game!")
                total_games_won += 1
                game_won = True
                break
            elif guess < random_number:
                messagebox.showinfo("Hint", "Incorrect guess. Hint: The number is higher than your guess.")
            else:
                messagebox.showinfo("Hint", "Incorrect guess. Hint: The number is lower than your guess.")

            attempts_used += 1

        if not game_won:
            messagebox.showinfo("Game Over",
                                f"Sorry, you've used all your attempts.\nThe correct number was: {random_number}\nGame Over.")

        # Display score tracking
        messagebox.showinfo("Score Tracking",
                            f"Total Games Played: {total_games_played}\nTotal Games Won: {total_games_won}")

        # Prompt to play again
        while True:
            replay = simpledialog.askstring("Play Again", "Would you like to play again? (yes/no):")
            if replay is None:
                # User closed the dialog
                continue
            replay = replay.strip().lower()
            if replay == 'yes':
                play_again = True
                break
            elif replay == 'no':
                play_again = False
                messagebox.showinfo("Goodbye", "Thank you for playing! Goodbye.")
                break
            else:
                messagebox.showerror("Invalid Input", "Invalid input. Please enter 'yes' or 'no'.")

# Client Task B: Find the Spot #
# Add your pseudocode to this file below this line: #
'''
1. Initialize the mapping application
2. Set the starting position to (0, 0)
3. Set the target position to (target_x, target_y)
4. Initialize a flag to indicate if the target is reached (target_reached = False)
5. While target_reached is False:
6.     Print the current position to the player
7.     Prompt the player to move (north, south, east, west) or exit
8.     Read the player's input
9.     If the player's input is 'north':
10.         Increment the Y-coordinate by 1
11.     Else if the player's input is 'south':
12.         Decrement the Y-coordinate by 1
13.     Else if the player's input is 'east':
14.         Increment the X-coordinate by 1
15.     Else if the player's input is 'west':
16.         Decrement the X-coordinate by 1
17.     Else if the player's input is 'exit':
18.         Print "Exiting the application."
19.         End the program
20.     Else:
21.         Print "Invalid direction. Please enter north, south, east, west, or exit."
22.         Continue to the next iteration
23.     If the current position equals the target position:
24.         Print "Congratulations! You have found the spot at (" + target_x + ", " + target_y + ")."
25.         Set target_reached to True
26. Print "Thank you for using the Find the Spot application. Goodbye."
'''
def find_the_spot():
    """
    Client Task B: Find the Spot
    """
    # Initialize starting and target positions
    current_x, current_y = 0, 0
    target_x, target_y = 5, 5  # Example target position
    target_reached = False

    messagebox.showinfo("Find the Spot",
                        f"Welcome to the Find the Spot Application!\n"
                        f"Your starting position is ({current_x}, {current_y}).\n"
                        f"Your target location is ({target_x}, {target_y}).")

    while not target_reached:
        direction = simpledialog.askstring("Find the Spot",
                                           f"Current Position: ({current_x}, {current_y})\n"
                                           "Enter direction to move (north, south, east, west) or 'exit' to quit:")
        if direction is None:
            # User canceled the input
            continue
        direction = direction.strip().lower()

        if direction == 'north':
            current_y += 1
            messagebox.showinfo("Movement", "Moved north.")
        elif direction == 'south':
            current_y -= 1
            messagebox.showinfo("Movement", "Moved south.")
        elif direction == 'east':
            current_x += 1
            messagebox.showinfo("Movement", "Moved east.")
        elif direction == 'west':
            current_x -= 1
            messagebox.showinfo("Movement", "Moved west.")
        elif direction == 'exit':
            messagebox.showinfo("Exit", "Exiting the application.")
            return
        else:
            messagebox.showerror("Invalid Direction", "Invalid direction. Please enter north, south, east, west, or exit.")
            continue

        if (current_x, current_y) == (target_x, target_y):
            messagebox.showinfo("Congratulations!",
                                f"Congratulations! You have found the spot at ({target_x}, {target_y}).")
            target_reached = True

    messagebox.showinfo("Goodbye", "Thank you for using the Find the Spot application. Goodbye.")

# Client Task C: Product Package Counter #
# Add your pseudocode to this file below this line: #
'''
1. Initialize the product package counter
2. Set the number of products per package to 2
3. Set the maximum number of packages per case to 50
4. Print "Product Package Counter Started."
5. Print "Counting products by twos up to 50."
6. Initialize current_count to 2
7. WHILE current_count <= 50 DO:
8.     Print "Products Scanned: " + current_count
9.     Increment current_count by 2
10. Print "Counting Complete."
11. Print "Total Products Scanned: " + (current_count - 2)
12. Print "Total Packages: " + ((current_count - 2) / 2)
13. Print "Total Cases Needed: " + ceil((current_count - 2) / 2 / 50)
14. Print "Thank you for using the Product Package Counter."
'''
def product_package_counter():
    """
    Client Task C: Product Package Counter
    """
    PRODUCTS_PER_PACKAGE = 2
    MAX_PACKAGES_PER_CASE = 50

    messagebox.showinfo("Product Package Counter",
                        "Product Package Counter Started.\n"
                        "Counting products by twos up to 50.")

    current_count = 2

    while current_count <= 50:
        messagebox.showinfo("Counting", f"Products Scanned: {current_count}")
        current_count += 2

    total_products_scanned = current_count - 2
    total_packages = total_products_scanned / PRODUCTS_PER_PACKAGE
    total_cases_needed = math.ceil(total_packages / MAX_PACKAGES_PER_CASE)

    summary = (f"Counting Complete.\n\n"
               f"Total Products Scanned: {total_products_scanned}\n"
               f"Total Packages: {int(total_packages)}\n"
               f"Total Cases Needed: {total_cases_needed}\n\n"
               f"Thank you for using the Product Package Counter.")

    messagebox.showinfo("Summary", summary)

if __name__ == "__main__":
    main_menu()
