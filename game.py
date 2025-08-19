import random

def hangman():
    words = {
        'apple': 'A common fruit that keeps the doctor away',
        'banana': 'A long yellow fruit',
        'cherry': 'A small red fruit often on top of desserts',
        'orange': 'A citrus fruit and a color',
        'grape': 'Small round fruit used to make wine'
    }
    word, hint = random.choice(list(words.items()))
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print(f"Hint: {hint}\n")

    while incorrect_guesses < max_incorrect:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word: " + ' '.join(display_word))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.\n")

    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
