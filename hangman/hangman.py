import random
from words import words
from hangman_visual import lives_visual_dict
import string




# This function randomly selects a valid word from the provided list of words
def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses a word from the list
    # Check if the chosen word contains a dash or space
    while '-' in word or ' ' in word:
        word = random.choice(words)  # If it does, choose another word
    return word.upper()  # Return the chosen word in uppercase

# This function contains the main logic for the Hangman game
def hangman():
    word = get_valid_word(words)  # Get a valid word for the game
    word_letters = set(word)  # Create a set of letters in the chosen word
    alphabet = set(string.ascii_uppercase)  # Set of all uppercase letters
    used_letters = set()  # Set to keep track of letters guessed by the user

    lives = 7  # Number of lives the player starts with

    # The game loop continues until either all letters are guessed or lives run out
    while len(word_letters) > 0 and lives > 0:
        # Display remaining lives and used letters
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        # Create a display of the current word (letters guessed or dashes for missing letters)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])  # Display the current state of lives (visual representation)
        print('Current word:', ' '.join(word_list))  # Display the current word to guess

        user_letter = input('Guess a letter: ').upper()  # Get a letter guess from the user and convert it to uppercase

        # Check if the guessed letter is valid (not already guessed and is in the alphabet)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add the letter to the set of used letters
            # Check if the guessed letter is in the chosen word
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove the letter from the set of letters to guess
                print('')  # Print an empty line for formatting

            else:
                lives -= 1  # Decrease lives by 1 if the guess was incorrect
                print('\nYour letter,', user_letter, 'is not in the word.')  # Inform the user

        # If the letter has already been guessed
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')  # Prompt for a new guess

        # If the input is not a valid letter
        else:
            print('\nThat is not a valid letter.')  # Inform the user of invalid input

    # Check if the game ended due to running out of lives
    if lives == 0:
        print(lives_visual_dict[lives])  # Show the final visual representation of lives
        print('You died, sorry. The word was', word)  # Inform the user of the correct word
    else:
        print('YAY! You guessed the word', word, '!!')  # Congratulate the user for winning

# Entry point of the program
if __name__ == '__main__':
    hangman()  # Start the Hangman game
