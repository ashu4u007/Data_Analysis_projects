import random

def mystical_number_game():
    # The fortune teller channels a magic number between 1 and 100
    magic_number = random.randint(1, 100)
    attempts = 0
    
    print("🔮 THE FORTUNE TELLER'S CHALLENGE 🔮")
    print("I have envisioned a magic number between 1 and 100.")
    print("Do you possess the intuition to see what I see? Let us begin...\n")
    
    while True:
        try:
            # Look into the crystal ball and take a guess
            guess = int(input("Enter your guessed number: "))
            attempts += 1
            
            # The fortune teller evaluates your intuition
            if guess > magic_number:
                print("🔮 'Alas! Your vision climbs too high into the clouds. Try lower.'\n")
            elif guess < magic_number:
                print("🔮 'No, no... your sight drops too low into the valleys. Try higher.'\n")
            else:
                print(f"🌟 AMAZING! The mists clear! The magic number was indeed {magic_number}.")
                print(f"It took you {attempts} attempts to align your third eye with the future.")
                break # Breaks the loop since the correct answer was found
                
        except ValueError:
            # Handles the cosmic disturbance of typing something that isn't an integer
            print("🔮 'The spirits are confused by your input. Please enter a valid number.'\n")

# Run the game
if __name__ == "__main__":
    mystical_number_game()