import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    index_len = len(secret_word)
    user_word = list()
    for _ in range(index_len):
        user_word.append('_ ')
    print(''.join(user_word))

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass

#def good_guess(user_input):


def user_input(prompt):
    user_input = input(prompt)
   
    if len(user_input) >= 2:
        print("sorry, too many letters")
    elif user_input.isalpha():
        print('That is a letter')
    
   
    return user_input

def is_guess_in_word(secret_word):
    # checks if the letter guess is in the secret word
    ltr_guessed = user_input('Guess a letter! ')
    letter_index = [i for i, x in enumerate(secret_word) if x == user_input]
    print(len(letter_index))
    if len(letter_index) > 0:
        print("good guess! ")
        good_guess.append(ltr_guessed)

        return good_guess
    else: 
        print('sorry')
        bad_guess.append(ltr_guessed)
        return False
    print(letter_index)
    print(good_guess)
    print(bad_guess)
    is_word_guessed(secret_word, good_guess)



def spaceman(secret_word):
   
    print(secret_word)
    is_guess_in_word(secret_word)

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
good_guess = list()
bad_guess = list()
spaceman(secret_word)