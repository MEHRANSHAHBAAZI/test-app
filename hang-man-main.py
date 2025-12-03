import random
import hangman_stage


def choose_word():
    word_list = ["cheetah", "zebra", "wolf", "fox", "elephant"]
    chosen_word = random.choice(word_list)
    return chosen_word
chosen_word = choose_word()

word_length = len(chosen_word)
lives = 6
placeholder = ""

for position in range (word_length):
    placeholder += "_"
print(placeholder)

game_over = False 

correct_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"  
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True 
            print("****    You lose.    ****")
    if "_" not in display:
        game_over = True 
        print("****   You win!   ****")
    print (hangman_stage.get_hangman_stage()[6 - lives])
