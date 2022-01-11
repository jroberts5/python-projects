import random
import hangman_art
import hangman_words

#= Variables
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []

#Prints Game Logo
print(hangman_art.logo)

#Prints initial word blanks
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}\n")

# Game will run while the game isn't over
while not end_of_game:
  #Checks to see if user enters a valid input
  while True:
    try:
        check_or_solve = int(input("Would you like to check a letter or try to solve it?\n Type '1' to check a letter or '2' to solve it: ")) 
        while check_or_solve < 1 or check_or_solve > 2:
          print("\nInvalid. Please enter a menu option between '1' and '2'\n")
          break
    except ValueError:
        print("\nInvalid. Please enter a valid option.")
        continue
    else:
        break
  # Check for if player wants to guess letter
  if check_or_solve == 1:
    letter_guess = input("\nGuess a letter: ").lower()
    if letter_guess in display:
          print(f"You've already guessed {letter_guess}. Try Again")

    # If guessed letter was correct
    if letter_guess in chosen_word:
      print(f"'{letter_guess}' is in the word.\n")
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == letter_guess:
          display[position] = letter
          
    #If guessed letter was incorrect
    if letter_guess not in chosen_word:
        print(f"'{letter_guess}' is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose...")

    #Displays current solved letters (if any)
    print(f"{' '.join(display)}")

    #Checks if all letters were guessed
    if "_" not in display:
        end_of_game = True
        print("You found all of the letters! You win!")

    #Displays hangman status after each guess
    print(hangman_art.stages[lives])

  #Allows player to try to guess the answer - if wrong they just try again
  elif check_or_solve == 2:
    print("\nOkay, what do you think the word is?\n")
    word_guess = input("Type your answer: ")
    #If the guessed word was correct
    if word_guess.lower() == chosen_word:
      end_of_game = True
      print(f"\nCorrect! '{chosen_word}' was right answer. You win!")

      for position in range(word_length):
        letter = chosen_word[position]
        display[position] = letter
      print(f"{' '.join(display)}")
      print(hangman_art.stages[lives])

    #If guessed word was incorrect
    if word_guess.lower() != chosen_word:
      print(f"\nIncorrect. '{word_guess}' was not the correct answer. You lose a life...\n")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose...")
      print(hangman_art.stages[lives])
      continue

    