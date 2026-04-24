import random

def play_game():
    options = ["stone", "paper", "scissors"]
    
    print("--- Stone, Paper, Scissors Game ---")
    user_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
    
    if user_choice not in options:
        print("Invalid choice! Please try again.")
        return

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You won! 🎉")
    else:
        print("Computer wins! Better luck next time. 🤖")

# गेम शुरू करने के लिए
play_game()