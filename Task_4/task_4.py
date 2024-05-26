                        # Rock-Paper-Scissors Game

'''
    User Input: Prompt the user to choose rock, paper, or scissors.
    Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
    Game Logic: Determine the winner based on the user's choice and the computer's choice.
                        Rock beats scissors, scissors beat paper, and paper beats rock.
    Display Result: Show the user's choice and the computer's choice.
                        Display the result, whether the user wins, loses, or it's a tie.
    Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
    Play Again: Ask the user if they want to play another round.
    User Interface: Design a user-friendly interface with clear instructions and feedback.
'''



import random

def get_user_choice():
    while True:
        user_input = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_input in ['rock', 'paper', 'scissors', 'exit']:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
