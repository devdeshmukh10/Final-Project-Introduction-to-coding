import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def perform_calculation():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    
    expression = f"{num1} {operator} {num2}"
    correct_answer = eval(expression)
    
    user_answer = float(input(f"Solve the following: {expression} = "))
    
    if user_answer == correct_answer:
        print("Congratulations! You are correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}. You lose!")

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "Computer wins!":
        print("Uh-oh! You lost. Now, time for a punishment.")
        perform_calculation()

if __name__ == "__main__":
    play_game()
