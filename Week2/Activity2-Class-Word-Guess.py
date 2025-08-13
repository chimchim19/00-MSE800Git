import random
import string

""" update word guessing game in activity 1 with at least one class """

class WordGame:
    def __init__(self):
        self.lives_left = 5
        self.entry_set = set() # initialize an empty set for tried letters
        self.mystery_word = " "

    def random_select(self):
        word_choices = [ 
            "university", "technology", "department", "categories", 
            "foundation", "government", "evaluation", "literature"
        ]
        return random.choice(word_choices) # send back the selected word from the list

    def generate_blanks(self, input_string):
        return [ "_" for char in input_string ] # send back blanks as a list

    def ask_letter(self, entry_set):
        while True: # perform the loop until stopped
            print()
            char = input("Guess a letter:")

            if len(char) != 1:
                print("Invalid input. Please enter a single letter only.")
                continue # try again, continue with loop
            
            if char in entry_set:
                print("You've already guessed that letter. Please guess another.")
                continue # try again, continue with loop

            return char.lower() #exits the loop and the function

    def check_entry(self, word, blanks, letter):
        # default return value is False, and stays False unless letter is found in word
        is_found = False
        for index, char in enumerate(word):
            if char == letter:
                blanks[index] = letter
                is_found = True
        return is_found

    def word_complete(self, blanks):
        # default return value is False
        # will return True if no more "_" is found in blanks
        is_complete = False
        if "_" not in blanks:
            is_complete = True
        return is_complete

def start_game():

    # instantiate the class
    player = WordGame()

    # random selection of word to be guessed
    mystery_word = player.random_select()

    print("\nStart! Let's play a word guessing game.")
    print(f"You've got {player.lives_left} chance(s) left.")
    print(f"Mystery word has {len(mystery_word)} letters.")

    blanks = player.generate_blanks(mystery_word) # receive a list of literals
    print(" ".join(blanks)) # concatenates the list of blanks into a string separated by " " and display
    
    while True: # starts True and loops until it is stopped, e.g. with a 'break'
        letter = player.ask_letter(player.entry_set)
        player.entry_set.add(letter)  # add the new letter to the set of entries

        if player.check_entry(mystery_word, blanks, letter): # function returns True or False
            print("\nYou found a letter!")
            print(" ".join(blanks))

            if player.word_complete(blanks): # returns True if mystery word is completely guessed
                print("\nCongratulations! You guessed the word!")
                print(f"Mystery word is: {mystery_word}")
                print("Thank you for playing the game.")
                break  # end the game

            print(f"You've got {player.lives_left} chance(s) left.")

        else: # check_entry() returned False
            player.lives_left -= 1
            print("\nSorry, that letter is not in the mystery word.")
            print("You've lost a chance.")
            print(f"You've got {player.lives_left} chance(s) left. \n")
            print(" ".join(blanks))
            
            if player.lives_left <= 0:  # all chances have been used up
                print("\nSorry you didn't guess the word.")
                print(f"Mystery word is: {mystery_word}")
                print("Thank you for playing the game.")
                break  # end the game


if __name__ == "__main__":

    start_game()