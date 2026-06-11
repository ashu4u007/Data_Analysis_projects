import random

def play_hangman():
    # 1. The Wizard's Archive (Our list of secret words)
    word_bank = ["wizard", "griffon", "alchemy", "spellbound", "phoenix", "sorcery"]
    
    # Randomly select the secret word
    secret_word = random.choice(word_bank)
    
    # Create a list of underscores to represent the hidden letters
    guessed_word = ["_"] * len(secret_word)
    
    # 2. The Life Force (Limiting incorrect guesses)
    attempts_left = 6
    guessed_letters = set() # To track letters already guessed

    print("🔮 Welcome to the Magical Kingdom! 🔮")
    print("An evil wizard holds a soul captive. Guess the word to shatter the curse!")
    print(f"The word has {len(secret_word)} letters.")
    print(" ".join(guessed_word))
    print("-" * 40)

    # 3. The Game Loop
    while attempts_left > 0 and "_" in guessed_word:
        guess = input("\nCast your letter guess: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid incantation! Please guess a single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"🔮 You've already tried '{guess}'. The wizard scoffs at your forgetfulness.")
            continue

        # Add to the history of guesses
        guessed_letters.add(guess)

        # 4. Conditionals & String Manipulation
        if guess in secret_word:
            print(f"✨ A match! The letter '{guess}' glows on the parchment.")
            # Update the underscores with the correctly guessed letter
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts_left -= 1
            print(f"💥 Wrong guess! The wizard laughs. Misfortune approaches.")
            print(f"Attempts remaining before doom: {attempts_left}")

        # Show current progress
        print(" ".join(guessed_word))

    # 5. The Resolution
    print("-" * 40)
    if "_" not in guessed_word:
        print(f"🎉 HUZZAH! The word was indeed '{secret_word}'!")
        print("The chains shatter, the wizard vanishes in a puff of logic, and the soul is saved!")
    else:
        print(f"💀 Alas! You ran out of magic. The secret word was '{secret_word}'.")
        print("The prisoner has been turned into a line of commented-out code forever.")

# Run the game
if __name__ == "__main__":
    play_hangman()