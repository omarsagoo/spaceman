import random

#loads a random secret word from words.txt
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word

#Handles all user input with error handling
#Jake Shams showed me this recursive solution
def user_input(prompt):
    user_input =  input(prompt)
    if len(user_input) != 1:
        return user_input("Input can only be one letter: ")
    elif not user_input.isalpha():
        return user_input("Input must be a letter: ")
    return user_input


    

# creates an array to store the Users correct guesses
def word_init(secret_word):
    return ['_'] * len(secret_word)

# returns the index of the letter that is guessed
def find_index(secret_word, guess):
    indicies = list()

    for index, char in enumerate(secret_word):
        if char == guess:
            indicies.append(index)
    
    return indicies

#
def submit_letter(char, underscore, indicies):
    for index in indicies:
        underscore[index] = char
    return underscore


def main(secret_word):
    word_guess = word_init(secret_word)
    lives = 7
    guessed_ltrs = list()
    while lives > 0 and secret_word != ''.join(word_guess):
        guess = user_input("Guess a letter! ")
        guessed_ltrs.append(guess)
        find_index(secret_word, guess)
        indicies = find_index(secret_word, guess)
        if len(indicies) > 0:
            submit_letter(guess, word_guess, indicies)
            new_word_guess = submit_letter(guess, word_guess, indicies)
            print(' '.join(new_word_guess))
            print('Congrats you found a letter! ')
        else: 
            print('Sorry thats a bad guess!')
            lives -= 1
            print('You have ' + str(lives) + ' guesses left')
        print(guessed_ltrs)
    if lives == 0:
        print('Sorry better luck next time!')
    else:
        print("congrats you won!")


#test
def test():
    print(secret_word)

    user_input("hello! ")

    word_init(secret_word)



secret_word = load_word()

# print('Welcome to the spaceman game! ')
# main(secret_word)