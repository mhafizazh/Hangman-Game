import hangman_art
import word_list
import random

chosen_word = random.choice(word_list.word_list)
lives = 6
words_length = len(chosen_word)
end_of_game = False

print(chosen_word)

print(hangman_art.logo)


display = []

for _ in range(words_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(words_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives < 1:
            end_of_game = True
            print("you lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(hangman_art.stages[lives])


