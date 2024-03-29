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
def input_handler(prompt):
    user_input = input(prompt)
    if len(user_input) != 1:
        return input_handler("Input can only be one letter: ")
    if not user_input.isalpha():
        return input_handler("Input must be a letter: ")
    return user_input.lower()

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

# adds the letter to the guessed array
def add_letter_to_word_guess(char, underscore, indicies):
    for index in indicies:
        underscore[index] = char
    return underscore

# restarts the main function
def restart():
    user_input = input('Would you like to play again? type y, if not type n: ')

    if user_input == "y":
        return main()
    elif user_input == "n":
        print("Thank you for playing!")
    else:
        print("That wasn't one of the prompts!!!!! try again! ")
        return restart()


def main():
    secret_word = load_word()
    word_guess = word_init(secret_word)
    lives = len(secret_word)
    guessed_ltrs = list()
    
    while lives > 0 and secret_word != ''.join(word_guess):
        print(' '.join(word_guess))
        guess = input_handler("Guess a letter! ")
        
        while guess in guessed_ltrs:
            guess = input_handler("Already guessed that letter. try a different one: ")
        guessed_ltrs.append(guess)
        find_index(secret_word, guess)
        indicies = find_index(secret_word, guess)
        
        if len(indicies) > 0:
            add_letter_to_word_guess(guess, word_guess, indicies)
            new_word_guess = add_letter_to_word_guess(guess, word_guess, indicies)
            print(' '.join(new_word_guess))
            print('Congrats you found a letter! ')
        else: 
            print('Sorry thats a bad guess!')
            lives -= 1
            print('You have ' + str(lives) + ' guesses left')
        
        print('You have guessed these letters: ' + ', '.join(guessed_ltrs))
    
    if lives == 0:
        print("Your secret word was: " + secret_word)
        print('Sorry better luck next time!')
        restart()
    else:
        print("congrats you won!")
        restart()


#test
# def test(secret_word):
#     print(secret_word)

#     input_handler("hello! ")

#     word_init(secret_word)




name = input("What is your name? ")
print('Welcome to the spaceman game, ' + name + '!')
main()