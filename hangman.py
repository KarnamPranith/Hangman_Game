
import random


words = ["python", "apple", "chair", "music", "robot"]


secret_word = random.choice(words)


display = ["_"] * len(secret_word)


attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    
    if guess in secret_word:
        print("✅ Correct!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    else:
        print("❌ Wrong!")
        attempts -= 1


if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)

