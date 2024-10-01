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

# ------------------------------------------------- #
'''
import random

def guess_the_number_game():
    # Initialize score tracking
    total_games_played = 0
    total_games_won = 0
    play_again = True

    while play_again:
        total_games_played += 1
        random_number = random.randint(1, 10)
        max_attempts = 3
        attempts_used = 0
        game_won = False

        print("\nWelcome to the Guess the Number Game!")
        print("I have selected a number between 1 and 10.")
        print("You have 3 attempts to guess the number correctly.")

        while attempts_used < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts_used + 1}: Please enter your guess: "))
                if guess < 1 or guess > 10:
                    print("Invalid input. Please enter a whole number between 1 and 10.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            if guess == random_number:
                print(f"Congratulations! You guessed the correct number: {random_number}")
                print("You win the game!")
                total_games_won += 1
                game_won = True
                break
            elif guess < random_number:
                print("Incorrect guess. Hint: The number is higher than your guess.")
            else:
                print("Incorrect guess. Hint: The number is lower than your guess.")

            attempts_used += 1

        if not game_won:
            print("\nSorry, you've used all your attempts.")
            print(f"The correct number was: {random_number}")
            print("Game Over.")

        # Display score tracking
        print(f"\nTotal Games Played: {total_games_played}")
        print(f"Total Games Won: {total_games_won}")

        # Prompt to play again
        while True:
            replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if replay == 'yes':
                play_again = True
                break
            elif replay == 'no':
                play_again = False
                print("Thank you for playing! Goodbye.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    guess_the_number_game()

