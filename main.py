import random
import hangman_art
import hangman_words
from replit import clear
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages = hangman_art.stages
end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guess_list = [] 
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()
    if guess in guess_list: 
      print ("You already guessed this")
    else: 
      guess_list.append(guess)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
       
        lives -= 1
        print(f"The letter {guess} is not in the chosen word")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])